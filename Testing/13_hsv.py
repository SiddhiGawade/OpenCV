import cv2 as c
import numpy as np

def nothing(x):
    pass

cap = c.VideoCapture(0)

c.namedWindow('Tracking')
c.resizeWindow('Tracking', 600, 400)
c.createTrackbar('LH', 'Tracking', 0, 255, nothing)
c.createTrackbar('LS', 'Tracking', 0, 255, nothing)
c.createTrackbar('LV', 'Tracking', 0, 255, nothing)
c.createTrackbar('UH', 'Tracking', 255, 255, nothing)
c.createTrackbar('US', 'Tracking', 255, 255, nothing)
c.createTrackbar('UV', 'Tracking', 255, 255, nothing)

while(1):
    # frame = c.imread('smarties.jpg',1)
    _, frame = cap.read()
    frame = c.flip(frame, 1)  # Flip horizontally to correct mirror image


    hsv = c.cvtColor(frame, c.COLOR_BGR2HSV)

    l_h = c.getTrackbarPos('LH', 'Tracking')
    l_s = c.getTrackbarPos('LS', 'Tracking')
    l_v = c.getTrackbarPos('LV', 'Tracking')

    u_h = c.getTrackbarPos('UH', 'Tracking')
    u_s = c.getTrackbarPos('US', 'Tracking')
    u_v = c.getTrackbarPos('UV', 'Tracking')

    lower = np.array([l_h, l_s, l_v])
    upper = np.array([u_h, u_s, u_v])

    mask = c.inRange(hsv, lower, upper)
    res = c.bitwise_and(frame, frame, mask=mask)
    
    # l_blue = np.array([110, 50, 50])
    # u_blue = np.array([130, 255, 255])

    # mask = c.inRange(hsv, l_blue, u_blue)
    # res = c.bitwise_and(frame, frame, mask=mask)

    frame = c.resize(frame, (600, 400))
    mask = c.resize(mask, (600, 400))
    res = c.resize(res, (600, 400))

    c.imshow('frame', frame)
    c.imshow('mask', mask)
    c.imshow('res', res)

    key = c.waitKey(1) & 0xFF
    if key ==27:
        break
cap.release()
c.destroyAllWindows()