import cv2
import numpy as np
import os


cap = cv2.VideoCapture('video.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frames
    ret, frame = cap.read()

    # Saves image of current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

cap.release()
cv2.destroyAllWindows
