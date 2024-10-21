from pathlib import Path
import webbrowser
import pyautogui
import time
from tkinter import Tk, Canvas, Button, PhotoImage
from calculadora import run_calc_thread
from teclado import run_keyb_thread
from l2cs import vis
import interface_google

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\fapesp-inatel\git_\EyesOn_1\MainCode\interface_v3\interface")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def Abrir_google():
    webbrowser.open_new_tab("https://www.google.com")

def Abrir_youtube():
    webbrowser.open_new_tab("https://www.youtube.com")


def tela(width = 1920, height = 1080):
    window = Tk()
    # Definindo a resolução da tela do usuário para ficar em tela cheia
    resolucao = f"{width}x{height}"
    window.geometry(resolucao)
    window.configure(bg="#F4F4F4")

    largura = width//3
    altura = height//2

    canvas = Canvas(
        window,
        bg="#F4F4F4",
        height=height,
        width=width,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Botão 1 ABRIR YOUTUBE
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=Abrir_youtube,
        relief="flat"
    )
    button_1.place(x=0.0, y=height//2, width=largura, height=altura)

    # Botao 2 ABRIR GOOGLE
    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:interface_google.run_interface_google(),
        relief="flat"
    )
    button_2.place(x=2 * (width//3), y=height//2, width=largura, height=altura)

    # Botão DESCANSO
    button_0 = Button(
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    button_0.place(x=width//3, y=height//2, width=largura, height=altura)

    # Botão 3 TECLADO VIRTUAL
    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: run_keyb_thread(),
        relief="flat"
    )
    button_3.place(x=0.0, y=0.0, width=largura, height=altura)

    # Botão 4 ASSISTENTE CALCULADORA
    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (run_calc_thread()),
        relief="flat"
    )
    button_4.place(x=2 * (width//3), y=0.0, width=largura, height=altura)

    # Botão 4 FINALIZAR PROGRAMA
    button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=window.destroy,
        relief="flat"
    )
    button_5.place(x=width//3, y=0.0, width=largura, height=altura)
    

    window.resizable(False, False)
    window.mainloop()

#tela()