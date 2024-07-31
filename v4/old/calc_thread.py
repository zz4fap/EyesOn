import tkinter as tk
import threading
from l2cs import vis

calc_thread_on = False

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def quit_application():
    global calc_thread_on
    root.quit()
    calc_thread_on = False


def setup_gui():
    global root, entry

    # Create the main window
    root = tk.Tk()
    root.title("Simple Calculator")

    # Set window size to 1440x900 pixels
    window_width = 1920
    window_height = 1050
    root.geometry(f"{window_width}x{window_height}")

    # Create entry widget
    entry = tk.Entry(root, width=50, borderwidth=5, font=("Arial", 24))
    entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

    # Define buttons
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ('C', 5, 0), ('QUIT', 5, 1)
    ]

    # Create buttons and place them in the grid
    for (symbol, row, column) in buttons:
        if symbol == '=':
            btn = tk.Button(root, text=symbol, padx=40, pady=20, command=calculate, font=("Arial", 32))
        elif symbol == 'C':
            btn = tk.Button(root, text=symbol, padx=40, pady=20, command=clear, font=("Arial", 32))
        elif symbol == 'QUIT':
            btn = tk.Button(root, text=symbol, padx=40, pady=20, command=quit_application, font=("Arial", 32), fg="red")
        else:
            btn = tk.Button(root, text=symbol, padx=40, pady=20, command=lambda s=symbol: button_click(s), font=("Arial", 32))
        btn.grid(row=row, column=column, padx=10, pady=10)

    # Run the main event loop
    root.mainloop()

def run_calc_thread():
    global calc_thread_on
    gui_thread = threading.Thread(target=setup_gui())
    gui_thread.start()
    calc_thread_on = True

# Start the GUI in a separate thread
#run_calc_thread()
