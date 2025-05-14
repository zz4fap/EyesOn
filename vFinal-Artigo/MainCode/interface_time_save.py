import threading
from pynput.mouse import Listener
import time
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import webbrowser
import pyautogui as pag
import teclado
import calculadora
import interface_google
import interface_youtube
import csv

# Shared flag to control threads
running = True
ac_tracker = []
last_click_time = time.time()  # Armazena o tempo do último clique

def mouse_listener():
    global ac_tracker
    global last_click_time
    
    def on_click(x, y, button, pressed):
        global last_click_time
        if not pressed or not running:
            return
            
        current_time = time.time()
        time_since_last_click = current_time - last_click_time
        last_click_time = current_time
        
        print(f"Mouse clicked at ({x}, {y}) with {button}")
        print(f"Tempo desde o último clique: {time_since_last_click:.3f} segundos")
        
        # Adiciona à lista de tracking (ajuste conforme suas variáveis globais)
        ac_tracker.append((
            time_since_last_click,
            teclado.keyb_thread_on if 'teclado' in globals() else None,
            calculadora.calc_thread_on if 'calculadora' in globals() else None,
            interface_google.interface_google_on if 'interface_google' in globals() else None
        ))
        print(len(ac_tracker))

    with Listener(on_click=on_click) as listener:
        while running:
            time.sleep(0.1)
        listener.stop()

class Interface:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1920x1080")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)
        
        # Set up a protocol to handle window closing
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        
        self.main()
        self.window.mainloop()

    def on_close(self):
        global running
        running = False  # This will stop the mouse listener thread
        self.window.destroy()

    # [Rest of your Interface class methods remain the same...]
    def main(self):
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\luiz.e_files\EyesOn\vFinal-Artigo\MainCode\interfacev4\assets\frame0")

        pag.moveTo(1595, 345)
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=1080,
            width=1920,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        canvas.create_image(960.0, 540.0, image=self.image_image_1)

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        Button(
            self.window,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.window.destroy,
            relief="flat"
        ).place(x=1426.0, y=216.0, width=319.0, height=204.0)

        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        Button(
            self.window,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.screen1,
            relief="flat"
        ).place(x=960.0, y=216.0, width=305.0, height=204.0)

        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        Button(
            self.window,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.screen2,
            relief="flat"
        ).place(x=960.0, y=540.0, width=305.0, height=192.0)

        self.button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        Button(
            self.window,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Zona Morta"),
            relief="flat"
        ).place(x=1426.0, y=540.0, width=319.0, height=192.0)

    def screen1(self):
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\luiz.e_files\EyesOn\vFinal-Artigo\MainCode\interfacev4\assets\frame1")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        pag.moveTo(1595, 265)
        canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=1080,
            width=1920,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        canvas.create_image(960.0, 540.0, image=self.image_image_1)

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        Button(
            self.window,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.main,
            relief="flat"
        ).place(x=1426.0, y=131.0, width=317.0, height=212.0)

        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        Button(
            self.window,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: interface_google.run_interface_google(),
            relief="flat"
        ).place(x=945.0, y=131.0, width=311.0, height=212.0)

        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        Button(
            self.window,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: interface_youtube.run_interface_youtube(),
            relief="flat"
        ).place(x=945.0, y=455.0, width=311.0, height=210.0)

        self.button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        Button(
            self.window,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.opennetflix,
            relief="flat"
        ).place(x=1426.0, y=455.0, width=328.0, height=210.0)

        self.button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
        Button(
            self.window,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.closetabs_,
            relief="flat"
        ).place(x=1421.0, y=778.0, width=322.0, height=215.0)

        self.button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
        Button(
            self.window,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.opentwitter,
            relief="flat"
        ).place(x=945.0, y=778.0, width=311.0, height=215.0)

    def screen2(self):
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\luiz.e_files\EyesOn\vFinal-Artigo\MainCode\interfacev4\assets\frame2")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        pag.moveTo(1595, 265)

        canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=1080,
            width=1920,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        canvas.create_image(960.0, 540.0, image=self.image_image_1)

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_7.png"))
        Button(
            self.window,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.main,
            relief="flat"
        ).place(x=1424.0, y=134.0, width=316.0, height=208.0)

        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        Button(
            self.window,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        ).place(x=936.0, y=134.0, width=326.0, height=208.0)

        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        Button(
            self.window,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: teclado.run_keyb_thread(),
            relief="flat"
        ).place(x=936.0, y=458.0, width=326.0, height=194.0)

        self.button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        Button(
            self.window,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: calculadora.run_calc_thread(),
            relief="flat"
        ).place(x=1424.0, y=458.0, width=326.0, height=194.0)

        self.button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
        Button(
            self.window,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        ).place(x=1424.0, y=779.0, width=326.0, height=205.0)

        self.button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
        Button(
            self.window,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        ).place(x=936.0, y=779.0, width=326.0, height=205.0)

    def openurl(self):
        webbrowser.open_new("https://google.com")

    def openyoutube(self):
        webbrowser.open_new("https://youtube.com")

    def opennetflix(self):
        webbrowser.open_new("https://netflix.com")

    def opentwitter(self):
        webbrowser.open_new("https://twitter.com")

    def closetabs_(self):
        time.sleep(3)
        pag.hotkey("ctrl", "w")

if __name__ == "__main__":
    # Start the mouse listener thread
    mouse_thread = threading.Thread(target=mouse_listener)
    mouse_thread.daemon = True  # This makes the thread exit when the main program exits
    mouse_thread.start()

    # Start the interface (which runs in the main thread)
    Interface()

    with open('avaliacoes/luiz/ac_tracker_mouse.csv', 'w', newline="") as f:
            # using csv.writer method from CSV package
            write = csv.writer(f)
            write.writerow(['Tempo desde ultimo', 'Teclado ativo', 'Calculadora ativa', 'Google ativo'])
            write.writerows(ac_tracker)

    # When the interface is closed, the running flag will be set to False
    # and the mouse thread will stop