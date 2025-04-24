from pathlib import Path
import webbrowser
import pyautogui
import subprocess
import time
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\fapesp-inatel\git_\EyesOn\MainCode\gui_inicial\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class App():

    def Abrir_pesquisa(self):
        webbrowser.open_new_tab("https://www.google.com")

    def Trocar_tela(self):
        time.sleep(1)
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')

    def __init__(self):
        self.tela()
    

    def tela(self):
        window = Tk()
        window.geometry("540x600")
        window.configure(bg = "#F4F4F4")
        canvas = Canvas(
            window,
            bg = "#F4F4F4",
            height = 600,
            width = 540,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: window.destroy(),
            relief="flat"
        )
        button_1.place(
            x=275.0,
            y=261.0,
            width=240.0,
            height=240.0
        )

        canvas.create_text(
            186.0,
            528.0,
            anchor="nw",
            text="Guia de acessibilidade",
            fill="#4F5258",
            font=("MavenPro ExtraBold", 15 * -1)
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Botao de mais opcoes"),
            relief="flat"
        )
        button_2.place(
            x=24.0,
            y=16.0,
            width=240.0,
            height=240.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.Abrir_pesquisa(),
            relief="flat"
        )
        button_3.place(
            x=24.0,
            y=261.0,
            width=240.0,
            height=240.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.Trocar_tela(),
            relief="flat"
        )
        button_4.place(
            x=275.0,
            y=16.0,
            width=240.0,
            height=240.0
        )
        window.resizable(False, False)
        window.mainloop()

App()