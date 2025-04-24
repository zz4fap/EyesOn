import time
import cv2
import imutils
import dlib
import pyautogui as pag
from imutils import face_utils
from math import hypot
import click



def midpoint(p1, p2):
    return int((p1.x + p2.x) / 2), int((p1.y + p2.y) / 2)


def get_blinking_ratio(eye_points, facial_landmarks):
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

    hor_line_length = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_length = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

    ratio = hor_line_length / ver_line_length
    return ratio


def click_mouse(detector, predictor, frame, trigger_time=1, start_time=None):
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)

    for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        det = shape[36:48]

        left_eye = get_blinking_ratio([36, 37, 38, 39, 40, 41], shape)
        right_eye = get_blinking_ratio([42, 43, 44, 45, 46, 47], shape)
        blinking_ratio = (left_eye + right_eye) / 2
        print(blinking_ratio)

        if blinking_ratio > 5:
            if start_time is None:
                start_time = time.time()
            elif time.time() - start_time >= trigger_time:
                pag.click()
                start_time = time.time()  # Reset start_time to the current time
        else:
            start_time = None

        for (x, y) in det:
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)



def main():
    tra = 0
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        blinking = click.click_mouse(detector, predictor, frame)

        if blinking > 5:
            if ret:
                tra+=1
                print(tra)
                if tra == 16:
                    pag.click()
                    tra = 0
        else:
            tra = 0


        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
