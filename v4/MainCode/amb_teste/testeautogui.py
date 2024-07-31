import pyautogui


def move_cursor(direction):
    step_size = 25
    current_x, current_y = pyautogui.position()

    if direction == 1:  # Move left
        new_x = current_x - step_size
        pyautogui.moveTo(new_x, current_y)
    elif direction == 2:  # Move right
        new_x = current_x + step_size
        pyautogui.moveTo(new_x, current_y)
    elif direction == 3:  # Move up
        new_y = current_y - step_size
        pyautogui.moveTo(current_x, new_y)
    elif direction == 4:  # Move down
        new_y = current_y + step_size
        pyautogui.moveTo(current_x, new_y)
    else:
        print("Invalid direction. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    direction = 0
    while direction != 5:
        try:
            direction = int(input("Enter direction (1=left, 2=right, 3=up, 4=down): "))
            move_cursor(direction)
        except ValueError:
            print("Invalid input. Please enter a number.")
