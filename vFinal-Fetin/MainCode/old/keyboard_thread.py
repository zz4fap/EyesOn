import tkinter as tk
import threading
import time

# Define global variables for Tkinter elements
root = None
entry = None
buttons = None
keyboard_layout = None
uppercase = False  # Initial case state
keyb_thread_on = False

def key_press(key):
    if uppercase:
        key = key.upper()
    else:
        key = key.lower()
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def toggle_case():
    global uppercase
    uppercase = not uppercase
    update_keyboard()

def update_keyboard():
    global keyboard_layout, uppercase
    if keyboard_layout:
        for i in range(len(keyboard_layout)):
            for j in range(len(keyboard_layout[i])):
                key = keyboard_layout[i][j]
                if uppercase:
                    key = key.upper()
                else:
                    key = key.lower()
                buttons[i][j].config(text=key)

def quit():
    global keyb_thread_on
    root.quit()
    keyb_thread_on = False

def setup_gui():
    global root, entry, buttons, keyboard_layout

    # Create the main window
    root = tk.Tk()
    root.title("Virtual Keyboard")
    root.geometry("1440x900")

    # Create entry widget
    entry = tk.Entry(root, width=95, borderwidth=5, font=("Arial", 24))
    entry.grid(row=0, column=0, columnspan=14, padx=0, pady=40)

    # Define keyboard layout for letters and numbers
    keyboard_layout = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    ]

    # Create a 2D list to hold button objects
    buttons = []

    # Create buttons and place them in the grid with bigger size and closer spacing
    for i in range(len(keyboard_layout)):
        button_row = []
        for j in range(len(keyboard_layout[i])):
            key = keyboard_layout[i][j]
            btn = tk.Button(root, text=key, width=4, height=2, padx=10, pady=10, command=lambda k=key: key_press(k), font=("Arial", 14))
            btn.grid(row=i+1, column=j, padx=5, pady=5)
            button_row.append(btn)
        buttons.append(button_row)

    # Additional buttons for special characters
    btn_clear = tk.Button(root, text="Clear", width=10, height=2, padx=10, pady=10, command=clear, font=("Arial", 14))
    btn_clear.grid(row=len(keyboard_layout) + 1, column=0, columnspan=2, padx=0, pady=10)

    btn_space = tk.Button(root, text="Space", width=20, height=2, padx=0, pady=10, command=lambda: key_press(" "), font=("Arial", 14))
    btn_space.grid(row=len(keyboard_layout) + 1, column=0, columnspan=8, padx=0, pady=10)

    btn_backspace = tk.Button(root, text="Backspace", width=10, height=2, padx=10, pady=10, command=lambda: entry.delete(len(entry.get()) - 1), font=("Arial", 14))
    btn_backspace.grid(row=len(keyboard_layout) + 1, column=3, columnspan=4, padx=5, pady=10)

    btn_case = tk.Button(root, text="Toggle Case", width=10, height=2, padx=10, pady=10, command=toggle_case, font=("Arial", 14))
    btn_case.grid(row=len(keyboard_layout) + 1, column=5, columnspan=4, padx=5, pady=10)

    # Quit button
    btn_quit = tk.Button(root, text="QUIT", width=10, height=2, padx=10, pady=10, command=quit, font=("Arial", 14), fg="red")
    btn_quit.grid(row=len(keyboard_layout) + 1, column=5, columnspan=2, padx=5, pady=10)

    # Set initial case state
    global uppercase
    uppercase = False

    # Update keyboard to initial case state
    update_keyboard()

    # Run the main event loop
    root.mainloop()

def run_keyboard_thread():
    global keyb_thread_on
    gui_thread = threading.Thread(target=setup_gui)
    gui_thread.start()
    keyb_thread_on = True

# Start the GUI in a separate thread
#run_keyboard_thread()
