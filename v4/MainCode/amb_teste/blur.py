import cv2
import numpy as np

# Carregar o classificador Haar para detecção de rosto
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Capturar a imagem da webcam
cap = cv2.VideoCapture(0)

while True:
    # Ler a imagem da webcam
    ret, frame = cap.read()

    # Converter para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostos
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Criar uma máscara do mesmo tamanho da imagem
    mask = np.zeros_like(frame)

    # Verificar se pelo menos um rosto foi detectado
    if len(faces) > 0:
        # Ordenar rostos com base na área (assumindo que a maior área é o rosto mais próximo)
        faces = sorted(faces, key=lambda x: x[2] * x[3], reverse=True)

        # Pegar o rosto com a maior área (o primeiro na lista ordenada)
        (x, y, w, h) = faces[0]
        mask = cv2.rectangle(mask, (x, y), (x + w, y + h), (255, 255, 255), -1)

    # Aplicar desfoque na imagem inteira
    blurred = cv2.GaussianBlur(frame, (21, 21), 0)

    # Combinar a imagem original com a imagem desfocada usando a máscara
    result = np.where(mask == np.array([255, 255, 255]), frame, blurred)

    # Mostrar o resultado
    cv2.imshow('Video', result)

    # Sair do loop quando a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a captura e destruir todas as janelas
cap.release()
cv2.destroyAllWindows()
