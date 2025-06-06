import tkinter as tk
from tkinter import ttk
import threading

calc_thread_on = False
def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

def clear():
    entry.delete(0, tk.END)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        # Replace '^' with '**' for power calculation
        expression = expression.replace('^', '**')
        # Evaluate the expression
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def setup_gui():
    global root, entry

    # Create the main window
    root = tk.Tk()
    root.title("Calculadora")
    root.attributes('-fullscreen', True)
    root.configure(bg="#000000")  # Black background

    style = ttk.Style()
    style.configure("TButton", font=("Arial", 24), padding=15)
    style.map("TButton", foreground=[("pressed", "red"), ("active", "blue")])

    # Create entry widget
    entry = ttk.Entry(root, font=("Arial", 24))
    entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20, sticky="ew")

    # Define standard buttons
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('(', 4, 1), (')', 4, 2), ('+', 4, 3),
        ('.', 5, 0), ('C', 5, 1), ('CE', 5, 2), ('=', 5, 3)
    ]

    # Create buttons and place them in the grid
    for (symbol, row, column) in buttons:
        if symbol == '=':
            btn = ttk.Button(root, text=symbol, command=calculate)
        elif symbol == 'C':
            btn = ttk.Button(root, text=symbol, command=clear)
        elif symbol == 'CE':
            btn = ttk.Button(root, text=symbol, command=clear_entry)
        else:
            btn = ttk.Button(root, text=symbol, command=lambda s=symbol: button_click(s))
        btn.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

    # Configure grid weights to make buttons expand
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)
    for i in range(6):
        root.grid_rowconfigure(i, weight=1)

    # Run the main event loop
    root.mainloop()

def run_calc_thread():
    global calc_thread_on
    gui_thread = threading.Thread(target=setup_gui())
    gui_thread.start()
    calc_thread_on = True

# Start the GUI in a separate thread

