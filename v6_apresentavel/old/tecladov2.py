import tkinter as tk
from tkinter import ttk
import threading

# Define global variables for Tkinter elements
root = None
entry = None
buttons = None
uppercase = True  # Initial case state to ensure the first letter is uppercase
first_letter = True  # Track if it's the first letter
is_secondary = False  # Track if the secondary keyboard is active
keyb_thread_on = False

# Define keyboard layouts
keyboard_layout_primary = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ç'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'Alt Keyboard']
]

keyboard_layout_secondary = [
    ['á', 'à', 'ã', 'â', '?', ','],
    ['é', 'è', 'ê', '!'],
    ['í', 'ì', 'î', '.'],
    ['ó', 'ò', 'õ', 'ô', 'ú', 'ù', 'û']
]

def key_press(key):
    global first_letter, uppercase
    if first_letter:
        key = key.upper()
        first_letter = False
        uppercase = False  # After first letter, switch to lowercase
    else:
        if uppercase:
            key = key.upper()
        else:
            key = key.lower()
    entry.insert(tk.END, key)
    update_keyboard()

def clear():
    global first_letter, uppercase
    entry.delete(0, tk.END)
    first_letter = True  # Reset to initial state
    uppercase = True  # Ensure the first letter is uppercase
    update_keyboard()

def toggle_case():
    global uppercase
    uppercase = not uppercase
    update_keyboard()

def toggle_keyboard():
    global is_secondary
    is_secondary = not is_secondary
    update_keyboard()

def update_keyboard():
    global is_secondary
    layout = keyboard_layout_secondary if is_secondary else keyboard_layout_primary
    for i in range(len(layout)):
        for j in range(len(layout[i])):
            key = layout[i][j]
            if uppercase:
                key = key.upper()
            else:
                key = key.lower()
            buttons[i][j].config(text=key, command=lambda k=key: key_press(k))
            buttons[i][j].grid()
        # Hide any remaining buttons in the row for the secondary layout
        if is_secondary:
            for j in range(len(layout[i]), 10):
                buttons[i][j].grid_remove()
    # Hide any remaining rows for the secondary layout
    if is_secondary:
        for i in range(len(layout), len(buttons)):
            for j in range(10):
                buttons[i][j].grid_remove()
    else:
        # Make sure all buttons are shown for the primary layout
        for i in range(len(layout), len(buttons)):
            for j in range(10):
                buttons[i][j].grid()

def setup_gui():
    global root, entry, buttons

    # Create the main window
    root = tk.Tk()
    root.title("Teclado Virtual")
    root.geometry("1920x1080")
    root.configure(bg="#2f2f2f")  # Dark grey background

    style = ttk.Style()
    style.configure("TButton", font=("Arial", 18), padding=15, borderwidth=2, relief="solid",
                    background="#ffffe0", foreground="black")
    style.map("TButton", background=[('active', '#ffffb0')], bordercolor=[('focus', '#000000')])

    # Create entry widget
    entry = ttk.Entry(root, font=("Arial", 24))
    entry.grid(row=0, column=0, columnspan=15, padx=20, pady=20, sticky="ew")

    # Create a 2D list to hold button objects
    buttons = []

    # Create buttons and place them in the grid with bigger size and closer spacing
    for i in range(4):  # Adjusted to max number of rows in any layout
        button_row = []
        for j in range(10):  # Adjusted to max number of columns in any layout
            btn = ttk.Button(root, text="", command=lambda: None, style="TButton")
            btn.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
            button_row.append(btn)
        buttons.append(button_row)

    # Additional buttons for special characters and actions
    btn_clear = ttk.Button(root, text="Limpar tudo", command=clear, style="TButton")
    btn_clear.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    btn_space = ttk.Button(root, text="Espaço", command=lambda: key_press(" "), style="TButton")
    btn_space.grid(row=5, column=2, columnspan=4, padx=5, pady=5, sticky="nsew")

    btn_backspace = ttk.Button(root, text="Deletar", command=lambda: entry.delete(len(entry.get()) - 1), style="TButton")
    btn_backspace.grid(row=5, column=6, columnspan=2, padx=5, pady=5, sticky="nsew")

    btn_case = ttk.Button(root, text="Capslock", command=toggle_case, style="TButton")
    btn_case.grid(row=5, column=8, padx=5, pady=5, sticky="nsew")

    btn_enter = ttk.Button(root, text="Enter", command=lambda: key_press("\n"), style="TButton")
    btn_enter.grid(row=5, column=9, padx=5, pady=5, sticky="nsew")

    btn_toggle_keyboard = ttk.Button(root, text="Alternar teclado", command=toggle_keyboard, style="TButton")
    btn_toggle_keyboard.grid(row=4, column=7, columnspan=3, padx=5, pady=5, sticky="nsew")

    # Set initial case state
    global uppercase
    uppercase = True

    # Update keyboard to initial case state
    update_keyboard()

    # Configure grid weights to make buttons expand
    for i in range(15):
        root.grid_columnconfigure(i, weight=1)
    for i in range(6):  # Adjusted to total number of rows including action buttons
        root.grid_rowconfigure(i, weight=1)

    # Run the main event loop
    root.mainloop()

def run_keyb_thread():
    global keyb_thread_on
    gui_thread = threading.Thread(target=setup_gui)
    gui_thread.start()
    keyb_thread_on = True

# Start the GUI in a separate thread
#run_gui_in_thread()