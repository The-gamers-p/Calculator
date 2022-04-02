from logging import root
from tkinter import *
from tkinter import ttk, Text, Frame
from turtle import width

back1 = "#1b1b1b"
Width = int(176/8)

root = Tk()
root.title("Calculator")
root.configure(bg = back1)

W = 540
H = 700
root.geometry(f'{W}x{H}')
# root.resizable(False, False)

Screen = Label(root,
    text = "HELLO",
    width = int(540 / 8))
Screen.grid(row = 0, column = 0, columnspan = 3)

B1 = Button(root,
    text = "1",
    width = Width)
B1.grid(row = 1, column = 0)

B2 = Button(root,
    text = "2",
    width = Width)
B2.grid(row = 1, column = 1)

B3 = Button(root,
    text = "3",
    width = Width)
B3.grid(row = 1, column = 2)

root.mainloop()