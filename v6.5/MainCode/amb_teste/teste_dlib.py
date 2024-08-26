# import the necessary packages
from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
import pyautogui as pag
import time

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# start the video stream and allow the camera to warm up
video_stream = cv2.VideoCapture(0)

start_time = None
trigger_time = 2  # seconds

while True:
    # capture the frame from the video stream
    ret, frame = video_stream.read()

    # check if frame is captured properly
    if not ret:
        break

    # resize the frame and convert it to grayscale
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in the grayscale image
    rects = detector(gray, 1)
    #print(rects)
    # loop over the face detections
    for (i, rect) in enumerate(rects):
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # draw the face landmarks on the frame
        #print(shape)
        #fds = shape[38:41]
        l1, l2 = shape[37], shape[38]
        l3, l4 = shape[41], shape[40]

        r1, r2 = shape[43], shape[44]
        r3, r4 = shape[47], shape[46]
        fds = [l1, l2, l3, l4, r1, r2, r3, r4]
        #print(fds)
        #print(l1[1] - l3[1])
        #print(l2[1] - l4[1])

        left_eye = (l1[1] - l3[1] + l2[1] - l4[1])/2
        right_eye = (r1[1] - r3[1] + r2[1] - r4[1])/2

        if left_eye >= -4:
            if start_time is None:
                start_time = time.time()  # start the timer
            elif time.time() - start_time >= trigger_time:
                pag.click()  # trigger the click if the condition is met for the required time
                start_time = None  # reset the timer after the action is triggered
        else:
            start_time = None  # reset the timer if the condition is not met


        #print(left_eye)
        print(right_eye)
        for (x, y) in fds:
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

    # show the frame
    cv2.imshow("Frame", frame)

    # if the 'q' key is pressed, break from the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cleanup
video_stream.release()
cv2.destroyAllWindows()
