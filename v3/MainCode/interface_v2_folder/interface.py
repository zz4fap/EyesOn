from pathlib import Path
import webbrowser
import pyautogui
import time
from tkinter import Tk, Canvas, Button, PhotoImage
from teclado import Teclado
import subprocess
from calculadora import Calculadora as c

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\fapesp-inatel\git_\EyesOn\MainCode\interface_v2\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Interface:
    notepad_path = "notepad.exe"

    def __init__(self):
        self.tela()

    def Abrir_pesquisa(self):
        webbrowser.open_new_tab("https://www.google.com")

    def Trocar_tela(self):
        time.sleep(1)
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')

    def tela(self):
        window = Tk()
        # Definindo a resolução da tela do usuário para ficar em tela cheia
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        resolucao = f"{width}x{height}"
        window.geometry(resolucao)
        window.configure(bg="#F4F4F4")

        canvas = Canvas(
            window,
            bg="#F4F4F4",
            height=1080,
            width=1920,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        # Botão 1
        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: window.winfo_toplevel(Teclado()),
            relief="flat"
        )
        button_1.place(x=0.0, y=540.0, width=640.0, height=540.0)

        # Botão 2
        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: subprocess.Popen([self.notepad_path]),
            relief="flat"
        )
        button_2.place(x=1280.0, y=540.0, width=640.0, height=540.0)

        # Botão 3
        button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: c(),
            relief="flat"
        )
        button_3.place(x=640.0, y=540.0, width=640.0, height=540.0)

        # Botão 4
        button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=window.destroy,
            relief="flat"
        )
        button_4.place(x=0.0, y=0.0, width=640.0, height=540.0)

        # Botão 5
        button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.Trocar_tela,
            relief="flat"
        )
        button_5.place(x=1280.0, y=0.0, width=640.0, height=540.0)

        # Botão 6
        button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.Abrir_pesquisa,
            relief="flat"
        )
        button_6.place(x=640.0, y=0.0, width=640.0, height=540.0)

        window.resizable(False, False)
        window.mainloop()

Interface()