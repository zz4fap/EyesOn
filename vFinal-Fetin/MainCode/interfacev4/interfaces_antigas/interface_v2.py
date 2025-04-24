from pathlib import Path
import webbrowser
import pyautogui
import time
from tkinter import Tk, Canvas, Button, PhotoImage

from l2cs import vis
import teclado
import calculadora
import interface_google


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\fapesp-inatel\git_\EyesOn_1\MainCode\interface_v2_folder\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def Abrir_pesquisa():
    webbrowser.open_new_tab("https://www.google.com")


def Trocar_tela():
    time.sleep(1)
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')


def tela(width = 1920, height = 1080):
    window = Tk()
    # Definindo a resolução da tela do usuário para ficar em tela cheia
    #resolucao = f"{width}x{height}"
    #window.geometry(resolucao)
    window.attributes('-fullscreen', True)
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

    # Botão 1 TECLADO VIRTUAL
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: teclado.run_keyb_thread(),
        relief="flat"
    )
    button_1.place(x=0.0, y=height//2, width=largura, height=altura)

    # Botão 2 BLOCO DE NOTAS
    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:interface_google.run_interface_google(),
        relief="flat"
    )
    button_2.place(x=2 * (width//3), y=height//2, width=largura, height=altura)

    # Botão 3 ASSISTENTE CALCULADORA
    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: calculadora.run_calc_thread(),
        relief="flat"
    )
    button_3.place(x=width//3, y=height//2, width=largura, height=altura)

    # Botão 4 FINALIZAR PROGRAMA
    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=window.destroy,
        relief="flat"
    )
    button_4.place(x=0.0, y=0.0, width=largura, height=altura)

    # Botão 5 TROCAR JANELA
    button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=Trocar_tela,
        relief="flat"
    )
    button_5.place(x=2 * (width//3), y=0.0, width=largura, height=altura)

    # Botão 6 PESQUISAR INTERNET
    button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=Abrir_pesquisa,
        relief="flat"
    )
    button_6.place(x=width//3, y=0.0, width=largura, height=altura)

    window.resizable(False, False)
    window.mainloop()

#tela()