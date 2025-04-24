import tkinter as tk
from tkinter import ttk
import threading
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 

# Define global variables for Tkinter elements
root = None
entry = None
buttons = None
uppercase = True  # Initial case state to ensure the first letter is uppercase
first_letter = True  # Track if it's the first letter
driver = None  # Selenium WebDriver

# Define the keyboard layout based on the image
keyboard_layout_primary = [
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ç'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', '?', '!', '.']
]

def setup_selenium():
    global driver
    # Iniciar o navegador e ir para o Google
    driver = webdriver.Chrome()
    driver.get("http://www.google.com")

def key_press(key):
    global first_letter, uppercase

    if key == "CA":
        clear()
        return
    elif key == "␣":
        key = " "
    elif key == "⌫":
        entry.delete(len(entry.get()) - 1)
        return
    elif key == "⏎":
        key = "\n"
        minimize_app()
    elif key == "sair":
        close_app()
        return

    if first_letter:
        key = key.upper()
        first_letter = False
        uppercase = False  # After first letter, switch to lowercase
    else:
        if uppercase:
            key = key.upper()
        else:
            key = key.lower()

    # Envia a tecla diretamente para a barra de pesquisa usando Selenium
    search_box = driver.find_element("name", "q")
    search_box.send_keys(key)

    entry.insert(tk.END, key)
    update_keyboard()

def clear():
    global first_letter, uppercase
    entry.delete(0, tk.END)
    first_letter = True  # Reset to initial state
    uppercase = True  # Ensure the first letter is uppercase
    update_keyboard()

def minimize_app():
    root.iconify()  # Minimiza a janela do Tkinter

def close_app():
    root.destroy()
    driver.quit()

def update_keyboard():
    global uppercase
    layout = keyboard_layout_primary
    for i in range(len(layout)):
        for j in range(len(layout[i])):
            key = layout[i][j]
            if uppercase:
                key = key.upper()
            else:
                key = key.lower()
            buttons[i][j].config(text=key, command=lambda k=key: key_press(k))
            buttons[i][j].grid()

def setup_gui():
    global root, entry, buttons

    # Create the main window
    root = tk.Tk()
    root.title("Teclado Virtual")
    root.geometry("1400x900")
    root.configure(bg="#2f2f2f")  # Dark grey background

    style = ttk.Style()
    style.configure("TButton",
                    font=("Arial", 30),
                    padding=5,
                    borderwidth=2,
                    relief="solid",
                    background="#d0d0d0",  # Light grey background
                    foreground="#2f2f2f")  # Dark grey text
    style.map("TButton",
              background=[('active', '#2f2f2f')],  # Darker grey when button is active
              bordercolor=[('focus', '#000000')])

    # Create entry widget and control buttons in the top row
    entry = ttk.Entry(root, font=("Arial", 24))
    entry.grid(row=0, column=0, columnspan=12, padx=20, pady=20, sticky="ew")

    btn_backspace = ttk.Button(root, text="⌫", command=lambda: key_press("⌫"), style="TButton")
    btn_backspace.grid(row=5, column=6, padx=5, pady=5, sticky="nsew")

    btn_clear_all = ttk.Button(root, text="CA", command=clear, style="TButton")
    btn_clear_all.grid(row=5, column=7, padx=5, pady=5, sticky="nsew")

    btn_sair = ttk.Button(root, text="sair", command=close_app, style="TButton")
    btn_sair.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

    # Create a 2D list to hold button objects
    buttons = []

    # Create buttons and place them in the grid with bigger size and closer spacing
    for i in range(len(keyboard_layout_primary)):  # Adjusted to max number of rows in the layout
        button_row = []
        for j in range(len(keyboard_layout_primary[i])):  # Adjusted to max number of columns in the layout
            btn = ttk.Button(root, text="", command=lambda: None, style="TButton")
            btn.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
            button_row.append(btn)
        buttons.append(button_row)

    # Create and configure the space bar
    btn_space = ttk.Button(root, text="␣", command=lambda: key_press("␣"), style="TButton")
    btn_space.grid(row=5, column=1, columnspan=5, padx=5, pady=5, sticky="nsew")

    # Create the enter button
    btn_enter = ttk.Button(root, text="⏎", command=lambda: key_press("\n"), style="TButton")
    btn_enter.grid(row=5, column=8, columnspan=4, padx=5, pady=5, sticky="nsew")

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

def run_gui_in_thread():
    # Setup Selenium in the main thread before running the GUI
    setup_selenium()
    
    # Start the GUI in a separate thread
    gui_thread = threading.Thread(target=setup_gui)
    gui_thread.start()

# Start the GUI and Selenium
run_gui_in_thread()

#