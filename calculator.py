from logging import root
from tkinter import *
from tkinter import ttk, Text


root = Tk()
root.title("Calculator")

width = 500
height = 700
root.geometry(f'{width}x{height}')
root.resizable(False, False)

def Copy(t):
    screen1.config(text=text1.get(1.0, 'end-1c'))
    screen1.update()


screen1 = Label(root,
    text = "",)
screen1.grid(row=0, column=0)

text1 = Text(width = 20, height=1)
text1.grid(row = 1, column = 0)
    
button = Button(root,
    text = "Copy")
button.grid(row = 2, column = 0)

button.bind("<Button-1>",Copy)

root.mainloop()