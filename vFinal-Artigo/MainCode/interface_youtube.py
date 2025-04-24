import tkinter as tk
from tkinter import ttk
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import teclado
import pyautogui as pag
# Define global variables for Tkinter elements
root = None
teclado.keyb_thread_on = None
root2 = None
entry = None
buttons = None
uppercase = True  # Initial case state to ensure the first letter is uppercase
first_letter = True  # Track if it's the first letter
is_secondary = False  # Track if the secondary keyboard is active
driver = None  # Selenium WebDriver
interface_youtube_on = False

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

def setup_selenium():
    global driver
    # Configurar opções para o Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")  # Inicia o navegador maximizado
    chrome_options.add_argument("--kiosk")  # Inicia o navegador em tela cheia

    # Iniciar o navegador com as opções configuradas e ir para o Google
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://www.youtube.com")
    time.sleep(1)  # Aguarda o carregamento da página

def key_press(key):
    global first_letter, uppercase, interface_google_on
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

    if key == "\n":
        #minimize_app()  # Minimiza a interface ao pressionar Enter
        root.withdraw()
        teclado.keyb_thread_on = False
        interface_youtube_on = True
        pag.moveTo( (1920//4) * 1 - 230, (1080//3) * 2 + 280) #ALTERAR PARA A INTERFACE NO CANTO INFERIOR DA TELA +475 -> move
        interface2_gui()
    else:
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

def minimize_app():
    root.iconify()  # Minimiza a janela do Tkinter

def close_app():
    global interface_youtube_on
    pag.moveTo(1595, 265)
    interface_youtube_on = False
    root2.destroy()
    driver.quit()

def enter_key():
    pyautogui.press('enter')

def send_navigation_key(key):
    global driver
    if driver:
        body = driver.find_element("tag name", "body")
        body.send_keys(key)

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


def interface2_gui():
    global root2

    root2 = tk.Tk()
    root2.title("Interface de Navegação")

    #focus_search_bar()

    screen_width = root2.winfo_screenwidth()
    screen_height = root2.winfo_screenheight()

    height = screen_height // 5
    x_position = 0
    y_position = screen_height - height

    root2.geometry(f"{screen_width}x{height}+{x_position}+{y_position}")
    root2.attributes("-topmost", True)
    root2.configure(bg="#000000")

    style = ttk.Style()
    style.configure("TButton", font=("Arial", 24), padding=15, background="#ffffe0", foreground="black")
    style.map("TButton", foreground=[("pressed", "red"), ("active", "blue")])

    buttons = [
        ('↑', 0, 1, lambda: send_navigation_key(Keys.UP)),
        ('↓', 0, 2, lambda: send_navigation_key(Keys.DOWN)),
        ('🔍', 0, 3, enter_key)
    ]

    sair_button = ttk.Button(root2, text="Sair", command=close_app)
    sair_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    for (symbol, row, column, cmd) in buttons:
        btn = ttk.Button(root2, text=symbol, command=lambda s=symbol, c=cmd: c())
        btn.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

    for i in range(4):
        root2.grid_columnconfigure(i, weight=1)
    root2.grid_rowconfigure(0, weight=1)

    root2.mainloop()

def setup_gui():
    global root, entry, buttons

    # Create the main window
    root = tk.Tk()
    root.title("Teclado Virtual")
    root.attributes('-fullscreen', True)
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
            btn.grid(row=i+1, column=j, padx=10, pady=10, sticky="nsew")
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

    btn_sair = ttk.Button(root, text="Sair", command=quit, style="TButton")
    btn_sair.grid(row=6, column=0, columnspan=15, padx=5, pady=5, sticky="nsew")

    # Set initial case state
    global uppercase
    uppercase = True

    # Update keyboard to initial case state
    update_keyboard()

    # Configure grid weights to make buttons expand
    for i in range(15):
        root.grid_columnconfigure(i, weight=1)
    for i in range(7):  # Adjusted to total number of rows including action buttons
        root.grid_rowconfigure(i, weight=1)

    # Run the main event loop
    root.mainloop()

def run_interface_youtube():
    # Setup Selenium in the main thread before running the GUI
    setup_selenium()
    # Start the GUI in a separate thread
    gui_thread = threading.Thread(target=setup_gui)
    gui_thread.start()
    pag.moveTo(80, 255)
    teclado.keyb_thread_on = True

# Start the GUI and Selenium
#run_interface_youtube()


#TECLADO NO PRIMEIRO PLANO