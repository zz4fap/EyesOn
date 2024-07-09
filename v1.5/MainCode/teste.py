import cv2

def main():
    # Initialize the camera
    cap = cv2.VideoCapture(0)  # Change the argument to 1 or -1 if you have multiple cameras

    if not cap.isOpened():
        print("Error: Couldn't open camera.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Couldn't read frame.")
            break

        # Display the resulting frame
        cv2.imshow('Camera', frame)

        # Check for user input to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


'''
    x, y = pag.position()
    if dx >= 20 and dy <= 50:
        print("ESQUERDA SUPERIOR")
        if x != 360 or y != 225:
            pag.moveTo(360, 225)

    elif dx > 20 and dy > 50:
        print("ESQUERDA INFERIOR")
        if x != 360 or y != 675:
            pag.moveTo(360, 675)

    elif dx <= -15 and dy <= 50:
        print("DIREITA SUPERIOR")
        if x != 1080 or y != 225:
            pag.moveTo(1080, 225)

    elif dx <= -15 and dy > 50:
        print("DIREITA INFERIOR")
        if x != 1080 or y != 675:
            pag.moveTo(1080, 675)

    else:
        print("Centro")
        
        
        
        
    if left and top:
        print("ESQUERDA SUPERIOR")
        if x != 360 or y != 225:
            pag.moveTo(360, 225)

    elif left and bottom:
        print("ESQUERDA INFERIOR")
        if x != 360 or y != 675:
            pag.moveTo(360, 675)

    elif right and top:
        print("DIREITA SUPERIOR")
        if x != 1080 or y != 225:
            pag.moveTo(1080, 225)

    elif right and bottom:
        print("DIREITA INFERIOR")
        if x != 1080 or y != 675:
            pag.moveTo(1080, 675)

    elif center:
        print("Centro")
        
'''

if left:
    print("LEFT")
if right:
    print("RIGHT")
if top:
    print("TOP")
if bottom:
    print("BOTOM")