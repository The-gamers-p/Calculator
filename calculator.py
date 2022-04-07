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
<insert, (https://www.google.com/search?q=meme&safe=active&rlz=1C1GCEA_enUS970US970&tbm=isch&source=iu&ictx=1&vet=1&fir=lLODzzlfHmoxSM%252C8LkjXcth-iXjoM%252C_%253B1I3YUd6Rqat65M%252C9Ehz_jcjm7QqIM%252C_%253BwXtYAEnozRQchM%252CMBHNDokt4PmVyM%252C_%253BA18Nir-EY2_TPM%252CEPPrysuzhQq0gM%252C_%253BzNnnTXYa2w2HgM%252C1gZnhsCCbJocmM%252C_%253BpzV0ztCWgU6DIM%252CM2oO48Ctjd1x-M%252C_%253B2N5jpWk7H5vM2M%252CouxhlMJ6Wd5Z3M%252C_%253Bq_FM4j1yoi95TM%252CIukVfdJ7FuvyBM%252C_%253B9CV-A4-HmBucuM%252COMjNzY78xqi8UM%252C_%253BOZ24umErdeCU7M%252CuXaz4eeNo9tPwM%252C_%253Bf5LIRonCfmdBcM%252CXPvQzNI14Ma_xM%252C_%253Bd9WKpkE_WCrlZM%252CTTbbgwaa3l9PcM%252C_%253Bv6VQ8drhkMCkdM%252CYWYsH9tTXoTJrM%252C_&usg=AI4_-kTd9zmKE3Qsp4FHxFJV-8C6JvMxJQ&sa=X&ved=2ahUKEwiUpJahx4L3AhXNomoFHa4qA0YQ9QF6BAgSEAE#imgrc=pzV0ztCWgU6DIM)>
          
root.mainloop()
