from pathlib import Path
import webbrowser
import pyautogui
import subprocess
import time
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\fapesp-inatel\git_\EyesOn\MainCode\interface\assets\frame0")


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
        #Definindo a resolução da tela do usuario para por em tela cheia
        window = Tk()
        window.geometry("1440x900")
        window.configure(bg = "#F4F4F4")
        canvas = Canvas(
            window,
            bg = "#F4F4F4",
            height = 900,
            width = 1440,
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
            x=720.0, #1018
            y=450.0, #550
            width=700.0, #900
            height=400.0 #530
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=720.0,
            y=0.0,
            width=700.0,
            height=400.0
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
            x=0.0,
            y=450.0,
            width=700.0,
            height=400.0
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
            x=0.0,
            y=0.0,
            width=700.0,
            height=400.0
        )
        window.resizable(False, False)
        window.mainloop()

App()