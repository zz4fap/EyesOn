# import the necessary packages
from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
import pyautogui as pag
import time
from math import hypot
import threading

def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

def get_blinking_ratio(eye_points, facial_landmarks):
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

    hor_line_length = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_length = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

    ratio = hor_line_length / ver_line_length
    return ratio

def click_mouse(detector, predictor, frame):
    blinking_ratio = 0
    # resize the frame and convert it to grayscale
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in the grayscale image
    rects = detector(gray, 1)
    #print(rects)
    # loop over the face detections
    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        t = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        det = shape[36:48]

        left_eye = get_blinking_ratio([36, 37, 38, 39, 40, 41], t)
        right_eye = get_blinking_ratio([42, 43, 44, 45, 46, 47], t)
        #blinking_ratio = (left_eye + right_eye) / 2
        blinking_ratio = left_eye
        print(blinking_ratio)
    return blinking_ratio
