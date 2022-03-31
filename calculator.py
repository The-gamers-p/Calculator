from logging import root
from tkinter import *
from tkinter import ttk, Text


root = Tk()
root.title("Calculator")


test = Label(root,
    text = "This is a test label part 1")

test2 = Label(root,
    text = "This is a test label part 2")


## Grid Example
# test.grid(row = 0, column=0)
# test2.grid(row=1, column = 1)


##Pack Example
test.pack(side = LEFT)
test2.pack(side = TOP)


root.mainloop()