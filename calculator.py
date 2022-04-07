from logging import root
#idk if this will work
from tkinter import *
#idk if this will work
from tkinter import ttk, Text, Frame
#idk if this will work
from turtle import width
#idk if this will work
back1 = "#1b1b1b"
#idk if this will work
Width = int(176/8)
#idk if this will work
root = Tk()
root.title("Calculator")
#idk if this will work
root.configure(bg = back1)
#idk if this will work
W = 540
#idk if this will work
H = 700
#idk if this will work
root.geometry(f'{W}x{H}')
# root.resizable(False, False)
#idk if this will work
Screen = Label(root,
    text = "HELLO",
               #idk if this will work
    width = int(540 / 8))
Screen.grid(row = 0, column = 0, columnspan = 3)
#idk if this will work
B1 = Button(root,
    text = "1",
            #idk if this will work
    width = Width)
B1.grid(row = 1, column = 0)
#idk if this will work
B2 = Button(root,
    text = "2",
    width = Width)
B2.grid(row = 1, column = 1)

B3 = Button(root,
    text = "3",
    width = Width)
B3.grid(row = 1, column = 2)

root.mainloop()
