from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import webbrowser, time, pyautogui
import pyautogui as pag
import threading

window = Tk()

window.geometry("1920x1080")
window.configure(bg = "#FFFFFF")

def main():
    global image_image_1  # Torna a referência global
    global button_image_1, button_image_2, button_image_3, button_image_4

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Pyprojects-Edu\EyesOn\vFinal\MainCode\interfacev4\assets\frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
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
        x=1426.0,
        y=216.0,
        width=319.0,
        height=204.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: run_screen1(),
        relief="flat"
    )
    button_2.place(
        x=960.0,
        y=216.0,
        width=305.0,
        height=204.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: run_screen2(),
        relief="flat"
    )
    button_3.place(
        x=960.0,
        y=540.0,
        width=305.0,
        height=192.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Zona Morta"),
        relief="flat"
    )
    button_4.place(
        x=1426.0,
        y=540.0,
        width=319.0,
        height=192.0
    )
    window.resizable(False, False)
    window.mainloop()
def screen1():
    global image_image_1  # Torna a referência global
    global button_image_1, button_image_2, button_image_3, button_image_4, button_image_5, button_image_6

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Pyprojects-Edu\EyesOn\vFinal\MainCode\interfacev4\assets\frame1")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
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
        command=main,
        relief="flat"
    )
    button_1.place(
        x=1426.0,
        y=131.0,
        width=317.0,
        height=212.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=openurl,
        relief="flat"
    )
    button_2.place(
        x=945.0,
        y=131.0,
        width=311.0,
        height=212.0
    )

    #Abrindo youtube
    def openyoutube():
        url = f"https://www.youtube.com/"
        webbrowser.open(url)

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=openyoutube,
        relief="flat"
    )
    button_3.place(
        x=945.0,
        y=455.0,
        width=311.0,
        height=210.0
    )

    #Abrir netflix
    def opennetflix():
        url = f"https://www.netflix.com/br/"
        webbrowser.open(url)

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=opennetflix,
        relief="flat"
    )
    button_4.place(
        x=1426.0,
        y=455.0,
        width=328.0,
        height=210.0
    )
    def closetabs_():
      time.sleep(2)
      pyautogui.hotkey('alt', 'tab')
      time.sleep(2)
      pyautogui.hotkey('alt', 'f4')

    #Abrir netflix
    def opentwitter():
        url = f"https://x.com/"
        webbrowser.open(url)

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=closetabs_,
        relief="flat"
    )
    button_5.place(
        x=1421.0,
        y=778.0,
        width=322.0,
        height=215.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=opentwitter,
        relief="flat"
    )
    button_6.place(
        x=945.0,
        y=778.0,
        width=311.0,
        height=215.0
    )

def screen2():
    global image_image_1  # Torna a referência global
    global button_image_1, button_image_2, button_image_3, button_image_4, button_image_5, button_image_6, button_image_7

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Pyprojects-Edu\EyesOn\vFinal\MainCode\interfacev4\assets\frame2")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
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
        x=1424.0,
        y=134.0,
        width=316.0,
        height=208.0
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
        x=936.0,
        y=134.0,
        width=326.0,
        height=208.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=936.0,
        y=458.0,
        width=326.0,
        height=194.0
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
        x=1424.0,
        y=458.0,
        width=326.0,
        height=194.0
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
        x=1424.0,
        y=779.0,
        width=326.0,
        height=205.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    button_6.place(
        x=936.0,
        y=779.0,
        width=326.0,
        height=205.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=main,
        relief="flat"
    )
    button_7.place(
        x=1423.0,
        y=134.0,
        width=317.0,
        height=212.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        1590.0,
        78.0,
        image=image_image_2
    )


def run_screen1():
    pag.moveTo(80, 255)
    run_s1 = threading.Thread(target=screen1)
    run_s1.start()

def run_screen2():
    pag.moveTo(80, 255)
    run_s2 = threading.Thread(target=screen2)
    run_s2.start()



window.resizable(False, False)
main()
window.mainloop()

