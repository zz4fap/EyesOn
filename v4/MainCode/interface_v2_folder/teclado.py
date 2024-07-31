from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
import webbrowser
import pyautogui
import time
from tkinter import Tk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\fapesp-inatel\git_\EyesOn\MainCode\interface_v2_folder\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Teclado():
    def __init__(self) -> None:
        self.tela()
        relative_to_assets(ASSETS_PATH)
    def tela(self):
        window = Tk()

        window.geometry("1366x768")
        window.configure(bg = "#FFFFFF")


        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 900,
            width = 1400,
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
            command=lambda: pyautogui.press('3'),
            relief="flat"
        )
        button_1.place(
            x=420.0,
            y=369.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('2'),
            relief="flat"
        )
        button_2.place(
            x=280.0,
            y=369.6572265625,
            width=140.0,
            height=106.0
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            490.0,
            317.0,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=0.0,
            y=264.0,
            width=980.0,
            height=104.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('6'),
            relief="flat"
        )
        button_3.place(
            x=840.0,
            y=369.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('7'),
            relief="flat"
        )
        button_4.place(
            x=980.0,
            y=369.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('8'),
            relief="flat"
        )
        button_5.place(
            x=1120.0,
            y=369.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('9'),
            relief="flat"
        )
        button_6.place(
            x=1260.0,
            y=369.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('5'),
            relief="flat"
        )
        button_7.place(
            x=700.0,
            y=369.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('e'),
            relief="flat"
        )
        button_8.place(
            x=280.0,
            y=475.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_9 = PhotoImage(
            file=relative_to_assets("button_9.png"))
        button_9 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('r'),
            relief="flat"
        )
        button_9.place(
            x=420.0,
            y=475.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_10 = PhotoImage(
            file=relative_to_assets("button_10.png"))
        button_10 = Button(
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('t'),
            relief="flat"
        )
        button_10.place(
            x=560.0,
            y=475.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_11 = PhotoImage(
            file=relative_to_assets("button_11.png"))
        button_11 = Button(
            image=button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('y'),
            relief="flat"
        )
        button_11.place(
            x=700.0,
            y=475.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_12 = PhotoImage(
            file=relative_to_assets("button_12.png"))
        button_12 = Button(
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('u'),
            relief="flat"
        )
        button_12.place(
            x=840.0,
            y=475.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_13 = PhotoImage(
            file=relative_to_assets("button_13.png"))
        button_13 = Button(
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('i'),
            relief="flat"
        )
        button_13.place(
            x=980.0,
            y=475.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_14 = PhotoImage(
            file=relative_to_assets("button_14.png"))
        button_14 = Button(
            image=button_image_14,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('o'),
            relief="flat"
        )
        button_14.place(
            x=1120.0,
            y=475.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_15 = PhotoImage(
            file=relative_to_assets("button_15.png"))
        button_15 = Button(
            image=button_image_15,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('p'),
            relief="flat"
        )
        button_15.place(
            x=1260.0,
            y=475.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_16 = PhotoImage(
            file=relative_to_assets("button_16.png"))
        button_16 = Button(
            image=button_image_16,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('d'),
            relief="flat"
        )
        button_16.place(
            x=280.0,
            y=581.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_17 = PhotoImage(
            file=relative_to_assets("button_17.png"))
        button_17 = Button(
            image=button_image_17,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('f'),
            relief="flat"
        )
        button_17.place(
            x=420.0,
            y=581.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_18 = PhotoImage(
            file=relative_to_assets("button_18.png"))
        button_18 = Button(
            image=button_image_18,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('g'),
            relief="flat"
        )
        button_18.place(
            x=560.0,
            y=581.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_19 = PhotoImage(
            file=relative_to_assets("button_19.png"))
        button_19 = Button(
            image=button_image_19,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('h'),
            relief="flat"
        )
        button_19.place(
            x=700.0,
            y=581.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_20 = PhotoImage(
            file=relative_to_assets("button_20.png"))
        button_20 = Button(
            image=button_image_20,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('j'),
            relief="flat"
        )
        button_20.place(
            x=840.0,
            y=581.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_21 = PhotoImage(
            file=relative_to_assets("button_21.png"))
        button_21 = Button(
            image=button_image_21,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('k'),
            relief="flat"
        )
        button_21.place(
            x=980.0,
            y=581.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_22 = PhotoImage(
            file=relative_to_assets("button_22.png"))
        button_22 = Button(
            image=button_image_22,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('l'),
            relief="flat"
        )
        button_22.place(
            x=1120.0,
            y=581.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_23 = PhotoImage(
            file=relative_to_assets("button_23.png"))
        button_23 = Button(
            image=button_image_23,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('ç'),
            relief="flat"
        )
        button_23.place(
            x=1260.0,
            y=581.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_24 = PhotoImage(
            file=relative_to_assets("button_24.png"))
        button_24 = Button(
            image=button_image_24,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('c'),
            relief="flat"
        )
        button_24.place(
            x=280.0,
            y=687.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_25 = PhotoImage(
            file=relative_to_assets("button_25.png"))
        button_25 = Button(
            image=button_image_25,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('v'),
            relief="flat"
        )
        button_25.place(
            x=420.0,
            y=687.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_26 = PhotoImage(
            file=relative_to_assets("button_26.png"))
        button_26 = Button(
            image=button_image_26,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('b'),
            relief="flat"
        )
        button_26.place(
            x=560.0,
            y=687.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_27 = PhotoImage(
            file=relative_to_assets("button_27.png"))
        button_27 = Button(
            image=button_image_27,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('n'),
            relief="flat"
        )
        button_27.place(
            x=700.0,
            y=687.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_28 = PhotoImage(
            file=relative_to_assets("button_28.png"))
        button_28 = Button(
            image=button_image_28,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('m'),
            relief="flat"
        )
        button_28.place(
            x=840.0,
            y=687.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_29 = PhotoImage(
            file=relative_to_assets("button_29.png"))
        button_29 = Button(
            image=button_image_29,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('?'),
            relief="flat"
        )
        button_29.place(
            x=980.0,
            y=687.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_30 = PhotoImage(
            file=relative_to_assets("button_30.png"))
        button_30 = Button(
            image=button_image_30,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('.'),
            relief="flat"
        )
        button_30.place(
            x=1260.0,
            y=687.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_31 = PhotoImage(
            file=relative_to_assets("button_31.png"))
        button_31 = Button(
            image=button_image_31,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('!'),
            relief="flat"
        )
        button_31.place(
            x=1120.0,
            y=687.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_32 = PhotoImage(
            file=relative_to_assets("button_32.png"))
        button_32 = Button(
            image=button_image_32,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('4'),
            relief="flat"
        )
        button_32.place(
            x=560.0,
            y=369.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_33 = PhotoImage(
            file=relative_to_assets("button_33.png"))
        button_33 = Button(
            image=button_image_33,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_33 clicked"),
            relief="flat"
        )
        button_33.place(
            x=980.0,
            y=263.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_34 = PhotoImage(
            file=relative_to_assets("button_34.png"))
        button_34 = Button(
            image=button_image_34,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_34 clicked"),
            relief="flat"
        )
        button_34.place(
            x=1120.0,
            y=793.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_35 = PhotoImage(
            file=relative_to_assets("button_35.png"))
        button_35 = Button(
            image=button_image_35,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_35 clicked"),
            relief="flat"
        )
        button_35.place(
            x=1120.0,
            y=263.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_36 = PhotoImage(
            file=relative_to_assets("button_36.png"))
        button_36 = Button(
            image=button_image_36,
            borderwidth=0,
            highlightthickness=0,
            command=window.destroy,
            relief="flat"
        )
        button_36.place(
            x=1260.0,
            y=263.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_37 = PhotoImage(
            file=relative_to_assets("button_37.png"))
        button_37 = Button(
            image=button_image_37,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_37 clicked"),
            relief="flat"
        )
        button_37.place(
            x=0.0,
            y=793.6572265625,
            width=1120.0,
            height=106.0
        )

        button_image_38 = PhotoImage(
            file=relative_to_assets("button_38.png"))
        button_38 = Button(
            image=button_image_38,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_38 clicked"),
            relief="flat"
        )
        button_38.place(
            x=1260.0,
            y=793.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_39 = PhotoImage(
            file=relative_to_assets("button_39.png"))
        button_39 = Button(
            image=button_image_39,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('1'),
            relief="flat"
        )
        button_39.place(
            x=140.0,
            y=370.0,
            width=140.0,
            height=106.0
        )

        button_image_40 = PhotoImage(
            file=relative_to_assets("button_40.png"))
        button_40 = Button(
            image=button_image_40,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('0'),
            relief="flat"
        )
        button_40.place(
            x=0.0,
            y=369.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_41 = PhotoImage(
            file=relative_to_assets("button_41.png"))
        button_41 = Button(
            image=button_image_41,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('s'),
            relief="flat"
        )
        button_41.place(
            x=140.0,
            y=582.0,
            width=140.0,
            height=106.0
        )

        button_image_42 = PhotoImage(
            file=relative_to_assets("button_42.png"))
        button_42 = Button(
            image=button_image_42,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('x'),
            relief="flat"
        )
        button_42.place(
            x=140.0,
            y=687.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_43 = PhotoImage(
            file=relative_to_assets("button_43.png"))
        button_43 = Button(
            image=button_image_43,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('z'),
            relief="flat"
        )
        button_43.place(
            x=0.0,
            y=687.6572265625,
            width=140.0,
            height=106.0
        )

        button_image_44 = PhotoImage(
            file=relative_to_assets("button_44.png"))
        button_44 = Button(
            image=button_image_44,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('a'),
            relief="flat"
        )
        button_44.place(
            x=0.0,
            y=582.0,
            width=140.0,
            height=106.0
        )

        button_image_45 = PhotoImage(
            file=relative_to_assets("button_45.png"))
        button_45 = Button(
            image=button_image_45,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('q'),
            relief="flat"
        )
        button_45.place(
            x=0.0,
            y=476.0,
            width=140.0,
            height=106.0
        )

        button_image_46 = PhotoImage(
            file=relative_to_assets("button_46.png"))
        button_46 = Button(
            image=button_image_46,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyautogui.press('w'),
            relief="flat"
        )
        button_46.place(
            x=140.0,
            y=476.0,
            width=140.0,
            height=106.0
        )
        window.resizable(True, True)
        window.mainloop()
Teclado()