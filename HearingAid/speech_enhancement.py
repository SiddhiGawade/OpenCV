import numpy as np
import librosa
import tensorflow as tf
import soundfile as sf
import os

# Paths
model1_path = os.path.join("models", "model_quant_1.tflite")
model2_path = os.path.join("models", "model_quant_2.tflite")
input_audio = os.path.join("audio", "audio_dirty.wav")
output_audio = os.path.join("audio", "enhanced_output.wav")

# Load audio
audio, sr = librosa.load(input_audio, sr=16000)

# Ensure length is divisible by 512 for framing
if len(audio) % 512 != 0:
    pad_len = 512 - (len(audio) % 512)
    audio = np.pad(audio, (0, pad_len))

# === Stage 1: Time-domain enhancement using model 1 ===

# Load model 1 first to get the expected input shape
interpreter1 = tf.lite.Interpreter(model_path=model1_path)
interpreter1.allocate_tensors()
input_details1 = interpreter1.get_input_details()
output_details1 = interpreter1.get_output_details()

# Print model 1 input details for debugging
print("Model 1 Input Shape:", input_details1[0]['shape'])
print("Model 1 Input Type:", input_details1[0]['dtype'])
expected_shape = input_details1[0]['shape']

# Prepare audio based on model's expected shape
enhanced_stage1 = []

# Get frequency domain representation if the model expects 257 features
if expected_shape[2] == 257:
    # Convert to frequency domain using STFT
    stft = librosa.stft(audio, n_fft=512, hop_length=256)
    mag = np.abs(stft).T.astype(np.float32)  # [frames, 257]
    phase = np.angle(stft)
    
    # Process each frame through model 1
    for frame in mag:
        # Reshape to match model input requirements
        input_tensor = frame[np.newaxis, np.newaxis, :]  # shape [1, 1, 257]
        interpreter1.set_tensor(input_details1[0]['index'], input_tensor)
        interpreter1.invoke()
        enhanced_frame = interpreter1.get_tensor(output_details1[0]['index'])[0, 0, :]
        enhanced_stage1.append(enhanced_frame)
    
    # Convert back to time domain
    enhanced_mag = np.array(enhanced_stage1).T  # [257, frames]
    enhanced_stft = enhanced_mag * np.exp(1j * phase)
    enhanced_audio_stage1 = librosa.istft(enhanced_stft, hop_length=256)
else:
    # Frame the audio for time-domain processing: shape [num_frames, 512]
    frames = np.reshape(audio, (-1, 512)).astype(np.float32)
    
    for frame in frames:
        # Process time domain signal with appropriate reshaping
        if expected_shape[1] == 1 and expected_shape[2] == 1:
            # Model expects single values
            for sample in frame:
                input_tensor = np.array([[[sample]]], dtype=np.float32)
                interpreter1.set_tensor(input_details1[0]['index'], input_tensor)
                interpreter1.invoke()
                enhanced_sample = interpreter1.get_tensor(output_details1[0]['index'])[0, 0, 0]
                enhanced_stage1.append(enhanced_sample)
        else:
            # Try to adapt to whatever shape the model expects
            print(f"Attempting to reshape frame to {expected_shape}")
            input_tensor = np.zeros(expected_shape, dtype=np.float32)
            min_len = min(expected_shape[-1], len(frame))
            
            if expected_shape[1] == 1:
                input_tensor[0, 0, :min_len] = frame[:min_len]
            else:
                input_tensor[0, :min_len, 0] = frame[:min_len]
                
            interpreter1.set_tensor(input_details1[0]['index'], input_tensor)
            interpreter1.invoke()
            enhanced_frame = interpreter1.get_tensor(output_details1[0]['index'])
            
            # Flatten the output to match original dimensions
            if expected_shape[1] == 1:
                enhanced_stage1.append(enhanced_frame[0, 0, :])
            else:
                enhanced_stage1.append(enhanced_frame[0, :, 0])
    
    # Flatten time-domain enhanced output if we processed in time domain
    if expected_shape[2] != 257:
        enhanced_audio_stage1 = np.reshape(enhanced_stage1, (-1,))

# Flatten time-domain enhanced output
if not 'enhanced_audio_stage1' in locals():
    enhanced_audio_stage1 = np.reshape(enhanced_stage1, (-1,))

# === Stage 2: Frequency-domain enhancement using model 2 ===

# Compute STFT of stage-1 enhanced signal
stft = librosa.stft(enhanced_audio_stage1, n_fft=512, hop_length=128, win_length=512)
magnitude, phase = np.abs(stft), np.angle(stft)

# Convert to log scale
log_mag = np.log1p(magnitude).T.astype(np.float32)  # [frames, freq_bins]

# Load model 2
interpreter2 = tf.lite.Interpreter(model_path=model2_path)
interpreter2.allocate_tensors()
input_details2 = interpreter2.get_input_details()
output_details2 = interpreter2.get_output_details()

# Print model 2 input details for debugging
print("Model 2 Input Shape:", input_details2[0]['shape'])
print("Model 2 Input Type:", input_details2[0]['dtype'])
expected_shape2 = input_details2[0]['shape']

# Run model 2 on each frame of the log magnitude spectrogram
enhanced_mag_log = []

# Adapt to model's expected input shape
for frame in log_mag:
    # Reshape to match model requirements
    if expected_shape2[1] == 1:
        # Model expects [batch, 1, features]
        input_tensor = frame[np.newaxis, np.newaxis, :]
    else:
        # Model expects [batch, features, channels]
        input_tensor = frame[np.newaxis, :, np.newaxis]
        
    # Check if we need to reshape
    if input_tensor.shape != tuple(expected_shape2):
        print(f"Reshaping from {input_tensor.shape} to {expected_shape2}")
        # Create a properly shaped tensor
        temp_tensor = np.zeros(expected_shape2, dtype=np.float32)
        # Copy as much data as will fit
        if expected_shape2[1] == 1:
            min_len = min(input_tensor.shape[2], expected_shape2[2])
            temp_tensor[0, 0, :min_len] = input_tensor[0, 0, :min_len]
        else:
            min_len = min(input_tensor.shape[1], expected_shape2[1])
            temp_tensor[0, :min_len, 0] = input_tensor[0, :min_len, 0]
        input_tensor = temp_tensor
        
    interpreter2.set_tensor(input_details2[0]['index'], input_tensor)
    interpreter2.invoke()
    
    # Extract output based on shape
    if expected_shape2[1] == 1:
        enhanced_frame = interpreter2.get_tensor(output_details2[0]['index'])[0, 0, :]
    else:
        enhanced_frame = interpreter2.get_tensor(output_details2[0]['index'])[0, :, 0]
        
    enhanced_mag_log.append(enhanced_frame)

# Inverse log to get enhanced magnitude
enhanced_mag_raw = np.expm1(np.array(enhanced_mag_log)).T  # transpose back to [freq_bins, frames]

# Fix the shape mismatch between enhanced magnitude and original phase
print(f"Enhanced magnitude shape: {enhanced_mag_raw.shape}, Phase shape: {phase.shape}")
# Resize enhanced_mag to match phase dimensions
if enhanced_mag_raw.shape[0] != phase.shape[0]:
    # Truncate or pad to match the original size
    enhanced_mag = np.zeros_like(phase)
    min_freq_bins = min(enhanced_mag_raw.shape[0], phase.shape[0])
    enhanced_mag[:min_freq_bins, :] = enhanced_mag_raw[:min_freq_bins, :]
else:
    enhanced_mag = enhanced_mag_raw

# Reconstruct STFT using enhanced magnitude and original phase
enhanced_stft = enhanced_mag * np.exp(1j * phase)
enhanced_waveform = librosa.istft(enhanced_stft, hop_length=128, win_length=512)

# Save output
sf.write(output_audio, enhanced_waveform, samplerate=sr)
print("Enhanced audio saved at:", output_audio)