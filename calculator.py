from logging import root
from tkinter import *
from tkinter import ttk, Text


root = Tk()
root.title("Calculator")

##You need a text font to change size
test = Label(root,
    text = "This is a test label part 1",
    font = ("helvetica", 20))

test2 = Label(root,
    text = "This is a test label part 2",
    font = (50))


## Grid Example
# test.grid(row = 0, column=0)
# test2.grid(row=1, column = 1)


##Pack Example
## Sides placement when and where are important
test.pack(side = LEFT)
test2.pack(side = TOP)


root.mainloop()