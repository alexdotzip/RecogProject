import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser()


parser.add_argument("video_path", help="path to the gameplay file")
args = parser.parse_args()

cap = cv2.VideoCapture(args.video_path)

if cap.isOpened()is False:
    print("Error opening the video file!")

while True:
    ret, frame = cap.read()
    # (height, width) = frame.shape[:2]

    if ret is True:
        map = frame[750:1080, 45:600]
        cv2.imshow('Video', map)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break

cap.release()
cv2.destroyAllWindows()