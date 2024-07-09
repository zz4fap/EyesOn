from pathlib import Path
import webbrowser
import pyautogui
import time
from tkinter import Tk, Canvas, Button, PhotoImage
from calc_thread import run_calc_thread
from keyboard_thread import run_keyboard_thread
from l2cs import vis

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\fapesp-inatel\git_\EyesOn\MainCode\interface_v2_folder\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def Abrir_pesquisa():
    webbrowser.open_new_tab("https://www.google.com")


def Trocar_tela():
    time.sleep(1)
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')


def tela():
    window = Tk()
    # Definindo a resolução da tela do usuário para ficar em tela cheia
    width = 1440
    height = 900
    resolucao = f"{width}x{height}"
    window.geometry(resolucao)
    window.configure(bg="#F4F4F4")

    canvas = Canvas(
        window,
        bg="#F4F4F4",
        height=900,
        width=1440,
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
        command=lambda: run_keyboard_thread(),
        relief="flat"
    )
    button_1.place(x=0.0, y=450.0, width=480.0, height=450.0)

    # Botão 2 BLOCO DE NOTAS
    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print(),
        relief="flat"
    )
    button_2.place(x=960.0, y=450.0, width=480.0, height=450.0)

    # Botão 3 ASSISTENTE CALCULADORA
    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (run_calc_thread()),
        relief="flat"
    )
    button_3.place(x=480.0, y=450.0, width=480.0, height=450.0)

    # Botão 4 FINALIZAR PROGRAMA
    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=window.destroy,
        relief="flat"
    )
    button_4.place(x=0.0, y=0.0, width=480.0, height=450.0)

    # Botão 5 TROCAR JANELA
    button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=Trocar_tela,
        relief="flat"
    )
    button_5.place(x=960.0, y=0.0, width=480.0, height=450.0)

    # Botão 6 PESQUISAR INTERNET
    button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=Abrir_pesquisa,
        relief="flat"
    )
    button_6.place(x=480.0, y=0.0, width=480.0, height=450.0)

    window.resizable(False, False)
    window.mainloop()