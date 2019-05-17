from tkinter import *


class Calculator:
    def __init__(self, master):
        self.scr = " "
        self.tot = StringVar()
        self.tot.set("0")

        lb1 = Label(master, textvariable=self.tot, bg="grey", width=32, relief=SUNKEN, anchor=E, height=2, fg="Dark blue").grid(row=0, column=0, columnspan=5, sticky=NSEW)

        self.bt9 = Button(master, text="9", command=lambda: self.buttonsprs(9), width=5, bg="light blue").grid(row=1, column=0, sticky=W)
        self.bt8 = Button(master, text="8", command=lambda: self.buttonsprs(8), width=5, bg="light blue").grid(row=1, column=1, sticky=W)
        self.bt7 = Button(master, text="7", command=lambda: self.buttonsprs(7), width=5, bg="light blue").grid(row=1, column=2, sticky=E)
        self.bt6 = Button(master, text="6", command=lambda: self.buttonsprs(6), width=5, bg="light blue").grid(row=1, column=3, sticky=N)
        self.bt5 = Button(master, text="5", command=lambda: self.buttonsprs(5), width=5, bg="light blue").grid(row=2, sticky=N)
        self.bt4 = Button(master, text="4", command=lambda: self.buttonsprs(4), width=5, bg="light blue").grid(row=2, column=1, sticky=N)
        self.bt3 = Button(master, text="3", command=lambda: self.buttonsprs(3), width=5, bg="light blue").grid(row=2, column=2, sticky=N)
        self.bt2 = Button(master, text="2", command=lambda: self.buttonsprs(2), width=5, bg="light blue").grid(row=2, column=3, sticky=N)
        self.bt1 = Button(master, text="1", command=lambda: self.buttonsprs(1), width=5, bg="light blue").grid(row=3, sticky=N)
        self.bt0 = Button(master, text="0", command=lambda: self.buttonsprs(0), width=5, bg="light blue").grid(row=3, column=1, sticky=N)
        self.bt_mi = Button(master, text="-", command=lambda: self.buttonsprs("-"), width=5, bg="magenta").grid(row=1, column=4, sticky=W)
        self.bt_pls = Button(master, text="+", command=lambda: self.buttonsprs("+"), height=3, width=5, bg="magenta").grid(row=2, column=4, rowspan=2, sticky=N)
        self.bt_dot = Button(master, text=".", command=lambda: self.buttonsprs("."), width=5, bg="light blue").grid(row=3, column=2, sticky=N)
        self.btc = Button(master, text="AC", command=lambda: self.clear(), width=5, bg="brown").grid(row=3, column=3, sticky=N)
        self.btm = Button(master, text="X", command=lambda: self.buttonsprs("*"), width=5, bg="magenta").grid(row=4, sticky=N)
        self.btd = Button(master, text="÷", command=lambda: self.buttonsprs("/"), width=5, bg="magenta").grid(row=4, column=1, sticky=N)
        self.bteq = Button(master, text="=", command=lambda: self.equal(), width=5, bg="Dark green").grid(row=4, column=3, sticky=N)
        self.btr = Button(master, text="REM", command=lambda: self.buttonsprs("%"), width=5, bg="magenta").grid(row=4, column=2, sticky=N)
        self.bte = Button(master, text="EXIT", command=lambda: exit(), width=5, bg="red").grid(row=4, column=4, sticky=N)

        self.lb = Label(master, text="Developed by Ashim", bg="grey", width=32).grid(row=5, columnspan=5)

    def clear(self):
        self.scr = ""
        self.tot.set("0")

    def equal(self):
        eq = eval(str(self.scr))
        self.tot.set(eq)

    def buttonsprs(self, n):
        self.scr += str(n)
        self.tot.set(self.scr)
        

a = Tk()
b = Calculator(a)
a.title("Calculator")
a.resizable(0, 0)
a.minsize(200, 150)
a.attributes("-topmost", -1)
a.attributes("-toolwindow", -TRUE)
a.mainloop()
