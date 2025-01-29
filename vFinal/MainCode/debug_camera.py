import torch
print(torch.cuda.is_available())

'''import cv2

def activate_webcam():
    # Open the webcam (0 is usually the default webcam)
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('Webcam', frame)

        # Wait for 1 millisecond per frame, 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture when done
    cap.release()
    cv2.destroyAllWindows()

# Call the function to activate the webcam
activate_webcam()'''
