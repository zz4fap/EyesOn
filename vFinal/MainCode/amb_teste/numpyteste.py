import cv2


def open_webcam():
    # Captura de vídeo a partir da webcam (índice 0 geralmente corresponde à webcam integrada)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erro: Não foi possível acessar a webcam.")
        return

    while True:
        # Captura frame a frame
        ret, frame = cap.read()

        if not ret:
            print("Erro: Não foi possível capturar o vídeo.")
            break

        # Exibe o frame na janela
        cv2.imshow('Webcam', frame)
        print(frame)

        # Sai do loop se a tecla 'q' for pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera a captura e fecha todas as janelas
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    open_webcam()
