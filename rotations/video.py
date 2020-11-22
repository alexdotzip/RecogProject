
import argparse


parser = argparse.ArgumentParser()


parser.add_argument("video_path", help="path to the gameplay file")
args = parser.parse_args()

# Create a VideoCapture object. argument is the video file name:
capture = cv2.VideoCapture(args.video_path)
 
# Check if the video is opened successfully
if capture.isOpened()is False:
    print("Error opening the video file!")
 
# Read until video is completed, or 'q' is pressed
while capture.isOpened():
    # Capture frame-by-frame from the video file
    ret, frame = capture.read()

    if ret is True:
        # Display the resulting frame
        cv2.imshow('Original frame from the video file', frame)

        # Convert the frame from the video file to grayscale:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the grayscale frame
        cv2.imshow('Grayscale frame', gray_frame)
 
        # Press q on keyboard to exit the program
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break
 
# Release everything
capture.release()
cv2.destroyAllWindows()