from pathlib import Path
import webbrowser
import pyautogui
import time
from tkinter import Tk, Canvas, Button, PhotoImage
from l2cs import vis
import kb_thread

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\luize\git_\EyesOnv2\MainCode\interface_v2_folder\assets\frame0")


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

    # Botão 1 TECLADO VIRTUAL
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: kb_thread.run_keyboard_thread(),
        relief="flat"
    )
    button_1.place(x=0.0, y=height//2, width=largura, height=altura)


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


    window.resizable(False, False)
    window.mainloop()

#tela()