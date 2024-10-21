from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import webbrowser, time, pyautogui
import teclado
import calculadora
import interface_google

window = Tk()

window.geometry("340x480")
window.configure(bg = "#FFFFFF")                        

def main():
    global image_image_1  # Torna a referência global
    global button_image_1, button_image_2, button_image_3, button_image_4

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\fapesp-inatel\git_\EyesOn_1\MainCode\interfacev4\assets\frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 480,
        width = 340,
        bd = 0,
        highlightthickness=0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        170.0,
        240.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=window.destroy,
        relief="flat"
    )
    button_1.place(
        x=197.0,
        y=156.0,
        width=104.0,
        height=69.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=screen1,
        relief="flat"
    )
    button_2.place(
        x=41.0,
        y=156.0,
        width=104.0,
        height=69.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=screen2,
        relief="flat"
    )
    button_3.place(
        x=41.0,
        y=260.0,
        width=104.0,
        height=69.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=200.0,
        y=260.0,
        width=104.0,
        height=69.0
    )
def screen1():
    global image_image_1  # Torna a referência global
    global button_image_1, button_image_2, button_image_3, button_image_4, button_image_5, button_image_6

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\fapesp-inatel\git_\EyesOn_1\MainCode\interfacev4\assets\frame1")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 480,
    width = 340,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        170.0,
        240.0,
        image=image_image_1
    )

    #Abrindo guia de pesquisa
    def openurl():
        url = f"https://www.google.com"
        webbrowser.open(url)
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=openurl,
        relief="flat"
    )
    button_1.place(
        x=40.0,
        y=105.0,
        width=104.0,
        height=69.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=main,
        relief="flat"
    )
    button_2.place(
        x=196.0,
        y=105.0,
        width=104.0,
        height=69.0
    )

    #Botão responsável por abrir mais uma guia da internet
    def opennewtab():
        url = f"https://www.google.com"
        webbrowser.open_new_tab(url)

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=opennewtab,
        relief="flat"
    )
    button_3.place(
        x=39.0,
        y=208.0,
        width=104.0,
        height=69.0
    )


    #Botão responsável por fechar a guia da internet atual
    def closetab():
        time.sleep(2)
        pyautogui.hotkey('alt', 'tab')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'w')
    
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=closetab,
        relief="flat"
    )
    button_4.place(
        x=196.0,
        y=208.0,
        width=104.0,
        height=69.0
    )

    #Botão que alterna as guias da internet
    def switchtabs():
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'tab')

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=switchtabs,
        relief="flat"
    )
    button_5.place(
        x=39.0,
        y=312.0,
        width=104.0,
        height=69.0
    )

    def closetabs_():

        time.sleep(2)
        pyautogui.hotkey('ctrl', 'shift', 'w')

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=closetabs_,
        relief="flat"
    )
    button_6.place(
        x=196.0,
        y=312.0,
        width=104.0,
        height=69.0
    )

def screen2():
    global image_image_1  # Torna a referência global
    global button_image_1, button_image_2, button_image_3, button_image_4, button_image_5, button_image_6, button_image_7

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\fapesp-inatel\git_\EyesOn_1\MainCode\interfacev4\assets\frame2")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 480,
        width = 340,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        170.0,
        240.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=40.0,
        y=34.0,
        width=104.0,
        height=69.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=main,
        relief="flat"
    )
    button_2.place(
        x=196.0,
        y=34.0,
        width=104.0,
        height=69.0
    )

#TECLADO
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: teclado.run_keyb_thread(),
        relief="flat"
    )
    button_3.place(
        x=40.0,
        y=138.0,
        width=104.0,
        height=69.0
    )

    #Abrir explorador de arquivos
    def explorer():
        time.sleep(2)
        pyautogui.hotkey('win', 'e')

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=explorer,
        relief="flat"
    )
    button_4.place(
        x=196.0,
        y=138.0,
        width=104.0,
        height=69.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=40.0,
        y=242.0,
        width=104.0,
        height=69.0
    )

#CALCULADORA
    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: calculadora.run_calc_thread(),
        relief="flat"
    )
    button_6.place(
        x=196.0,
        y=243.0,
        width=104.0,
        height=69.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    button_7.place(
        x=196.0,
        y=349.0,
        width=104.0,
        height=69.0
    )
    
window.resizable(False, False)
main()
window.mainloop()

