from tkinter import *
from tkinter import ttk
import sys


class Calc:
    """"This Class mainly creates Buttons, Labels with functions for a calculator app.
        This app is created by Ashim.
         This class mainly have 3 functions i.e., btn_press(), clear_all(), equate()."""
    def __init__(self, master):
        """"This method mainly creates all the required widgets in app."""

        # Initialisation.

        self.scr =""
        self.text = StringVar()
        # Functions

        def close():
            sys.exit(0)

        def btn_press(num):
            self.scr += str(num)
            self.text.set(self.scr)

        def equate():
            self.total = str(eval(self.scr))
            self.text.set(self.total)
            self.scr = ""

        def clear_all():
            self.scr = ""
            self.text.set(self.scr)

        # Frames and Labels

        self.fr1 = ttk.Frame(master).grid(sticky=N, row=0)
        self.fr2 = ttk.Frame(master).grid(sticky=S, row=1)
        self.lb = Label(self.fr1, textvariable=self.text, width=25, anchor=E, bg="GREY",fg="DARK BLUE", relief=SUNKEN, height=3).grid(row=0, columnspan=20, sticky=NW)
        self.lb1 = Label(master, text="©This is made by Ashim.", bg="magenta", width=25).grid(row=6, columnspan=20)

        # Buttons for 1 to 9 numbers.

        Button(self.fr1, text="1", width=5, command=lambda: btn_press("1"), bg="light blue").grid(row=2, column=0)
        Button(self.fr1, text="2", width=5, command=lambda: btn_press("2"), bg="light blue").grid(row=2, column=1)
        Button(self.fr1, text="3", width=5, command=lambda: btn_press("3"), bg="light blue").grid(row=2, column=2)

        Button(self.fr1, text="4", width=5, command=lambda: btn_press("4"), bg="light blue").grid(row=3, column=0)
        Button(self.fr1, text="5", width=5, command=lambda: btn_press("5"), bg="light blue").grid(row=3, column=1)
        Button(self.fr1, text="6", width=5, command=lambda: btn_press("6"), bg="light blue").grid(row=3, column=2)

        Button(self.fr1, text="7", width=5, command=lambda: btn_press("7"), bg="light blue").grid(row=4, column=0)
        Button(self.fr1, text="8", width=5, command=lambda: btn_press("8"), bg="light blue").grid(row=4, column=1)
        Button(self.fr1, text="9", width=5, command=lambda: btn_press("9"), bg="light blue").grid(row=4, column=2)

        # Buttons for symbols and 0.

        Button(self.fr1, text="÷", width=5, command=lambda: btn_press("/"), bg="yellow").grid(row=1, sticky=E, column=4)
        Button(self.fr1, text="AC", width=5, command=lambda: clear_all(), bg="yellow").grid(row=1, sticky=W, column=1)
        Button(self.fr1, text="REM", width=5, command=lambda: btn_press("%"), bg="yellow").grid(row=1, sticky=NE, column=2)
        Button(self.fr1, text="Exit", width=5, command=lambda: close(), bg="red").grid(row=1, sticky=NW, column=0)
        Button(self.fr2, text="0", width=12, command=lambda: btn_press("0"), bg="light blue").grid(row=5, columnspan=3, sticky=SW)
        Button(self.fr2, text=".", width=5, command=lambda: btn_press("."), bg="light blue").grid(row=5, column=2, sticky=NE)
        Button(self.fr2, text="=", width=5, command=lambda: equate(), bg="yellow").grid(row=5, column=4, sticky=SE)
        Button(self.fr1, text="-", width=5, command=lambda: btn_press("-"), bg="yellow").grid(row=2, column=4, sticky=E)
        Button(self.fr1, text="+", width=5, command=lambda: btn_press("+"), bg="yellow").grid(row=3, column=4, sticky=NE)
        Button(self.fr1, text="x", width=5, command=lambda: btn_press("*"), bg="yellow").grid(row=4, column=4, sticky=NE)


a = Tk()
b = Calc(a)
a.resizable(0, 0)
a.title("Calculator")
a.attributes("-topmost", TRUE)
a.attributes("-toolwindow", 1) #creates close button on toolbar
a.minsize(170, 150)
a.mainloop()
