from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\fapesp-inatel\git_\EyesOn\MainCode\interface_v2_folder\assets\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Calculadora():
    def __init__(self) -> None:
        self.tela()
    def tela(self):
        window = Tk()

        window.geometry("1400x900")
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
        canvas.create_rectangle(
            0.0,
            476.0,
            1400.0,
            900.0,
            fill="#1E1E1E",
            outline="")

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
            x=422.0,
            y=476.0,
            width=140.0,
            height=106.0
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
            x=282.0,
            y=476.0,
            width=140.0,
            height=106.0
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            492.0,
            423.3427734375,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=2.0,
            y=370.3427734375,
            width=980.0,
            height=104.0
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
            x=842.0,
            y=476.0,
            width=140.0,
            height=106.0
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
            x=982.0,
            y=476.0,
            width=140.0,
            height=106.0
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
            x=702.0,
            y=476.0,
            width=140.0,
            height=106.0
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
            x=282.0,
            y=582.0,
            width=140.0,
            height=106.0
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
            x=422.0,
            y=582.0,
            width=140.0,
            height=106.0
        )

        button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        button_8.place(
            x=562.0,
            y=582.0,
            width=140.0,
            height=106.0
        )

        button_image_9 = PhotoImage(
            file=relative_to_assets("button_9.png"))
        button_9 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat"
        )
        button_9.place(
            x=702.0,
            y=582.0,
            width=140.0,
            height=106.0
        )

        button_image_10 = PhotoImage(
            file=relative_to_assets("button_10.png"))
        button_10 = Button(
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_10 clicked"),
            relief="flat"
        )
        button_10.place(
            x=842.0,
            y=582.0,
            width=140.0,
            height=106.0
        )

        button_image_11 = PhotoImage(
            file=relative_to_assets("button_11.png"))
        button_11 = Button(
            image=button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_11 clicked"),
            relief="flat"
        )
        button_11.place(
            x=982.0,
            y=582.0,
            width=140.0,
            height=106.0
        )

        button_image_12 = PhotoImage(
            file=relative_to_assets("button_12.png"))
        button_12 = Button(
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_12 clicked"),
            relief="flat"
        )
        button_12.place(
            x=282.0,
            y=688.0,
            width=140.0,
            height=106.0
        )

        button_image_13 = PhotoImage(
            file=relative_to_assets("button_13.png"))
        button_13 = Button(
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_13 clicked"),
            relief="flat"
        )
        button_13.place(
            x=422.0,
            y=688.0,
            width=140.0,
            height=106.0
        )

        button_image_14 = PhotoImage(
            file=relative_to_assets("button_14.png"))
        button_14 = Button(
            image=button_image_14,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_14 clicked"),
            relief="flat"
        )
        button_14.place(
            x=562.0,
            y=688.0,
            width=140.0,
            height=106.0
        )

        button_image_15 = PhotoImage(
            file=relative_to_assets("button_15.png"))
        button_15 = Button(
            image=button_image_15,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_15 clicked"),
            relief="flat"
        )
        button_15.place(
            x=842.0,
            y=688.0,
            width=140.0,
            height=106.0
        )

        button_image_16 = PhotoImage(
            file=relative_to_assets("button_16.png"))
        button_16 = Button(
            image=button_image_16,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_16 clicked"),
            relief="flat"
        )
        button_16.place(
            x=982.0,
            y=688.0,
            width=140.0,
            height=106.0
        )

        button_image_17 = PhotoImage(
            file=relative_to_assets("button_17.png"))
        button_17 = Button(
            image=button_image_17,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_17 clicked"),
            relief="flat"
        )
        button_17.place(
            x=282.0,
            y=794.0,
            width=140.0,
            height=106.0
        )

        button_image_18 = PhotoImage(
            file=relative_to_assets("button_18.png"))
        button_18 = Button(
            image=button_image_18,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_18 clicked"),
            relief="flat"
        )
        button_18.place(
            x=422.0,
            y=794.0,
            width=140.0,
            height=106.0
        )

        button_image_19 = PhotoImage(
            file=relative_to_assets("button_19.png"))
        button_19 = Button(
            image=button_image_19,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_19 clicked"),
            relief="flat"
        )
        button_19.place(
            x=562.0,
            y=794.0,
            width=140.0,
            height=106.0
        )

        button_image_20 = PhotoImage(
            file=relative_to_assets("button_20.png"))
        button_20 = Button(
            image=button_image_20,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_20 clicked"),
            relief="flat"
        )
        button_20.place(
            x=702.0,
            y=794.0,
            width=140.0,
            height=106.0
        )

        button_image_21 = PhotoImage(
            file=relative_to_assets("button_21.png"))
        button_21 = Button(
            image=button_image_21,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_21 clicked"),
            relief="flat"
        )
        button_21.place(
            x=982.0,
            y=794.0,
            width=140.0,
            height=106.0
        )

        button_image_22 = PhotoImage(
            file=relative_to_assets("button_22.png"))
        button_22 = Button(
            image=button_image_22,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_22 clicked"),
            relief="flat"
        )
        button_22.place(
            x=562.0,
            y=476.0,
            width=140.0,
            height=106.0
        )

        button_image_23 = PhotoImage(
            file=relative_to_assets("button_23.png"))
        button_23 = Button(
            image=button_image_23,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_23 clicked"),
            relief="flat"
        )
        button_23.place(
            x=982.0,
            y=370.0,
            width=140.0,
            height=106.0
        )

        button_image_24 = PhotoImage(
            file=relative_to_assets("button_24.png"))
        button_24 = Button(
            image=button_image_24,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_24 clicked"),
            relief="flat"
        )
        button_24.place(
            x=1122.0,
            y=370.0,
            width=140.0,
            height=106.0
        )

        button_image_25 = PhotoImage(
            file=relative_to_assets("button_25.png"))
        button_25 = Button(
            image=button_image_25,
            borderwidth=0,
            highlightthickness=0,
            command=window.destroy,
            relief="flat"
        )
        button_25.place(
            x=1262.0,
            y=370.0,
            width=140.0,
            height=106.0
        )

        button_image_26 = PhotoImage(
            file=relative_to_assets("button_26.png"))
        button_26 = Button(
            image=button_image_26,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_26 clicked"),
            relief="flat"
        )
        button_26.place(
            x=842.0,
            y=794.0,
            width=140.0,
            height=106.0
        )

        button_image_27 = PhotoImage(
            file=relative_to_assets("button_27.png"))
        button_27 = Button(
            image=button_image_27,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_27 clicked"),
            relief="flat"
        )
        button_27.place(
            x=702.0,
            y=688.0,
            width=140.0,
            height=106.0
        )
        window.resizable(False, False)
        window.mainloop()

Calculadora()