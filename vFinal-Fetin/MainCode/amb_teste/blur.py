import cv2
import numpy as np

# Carregar o classificador Haar para detecção de rosto
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Capturar a imagem da webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    mask = np.zeros_like(frame)

    if len(faces) > 0:
        faces = sorted(faces, key=lambda x: x[2] * x[3], reverse=True)
        (x, y, w, h) = faces[0]
        mask[y:y + h, x:x + w] = (255, 255, 255)

    mask_bool = mask.astype(bool)
    bg_black = np.where(mask_bool, frame, 0)

    cv2.imshow('Video', bg_black)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
