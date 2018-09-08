# screenshot every 15 seconds

import time
from tkinter import *
import PIL.ImageGrab
import os
import datetime

def quiting(event=None):
    root.quit()


root = Tk()
root.geometry("350x150+450+200")
frame1 = Frame(root, width=350, height=80, bg="grey40")
frame2 = Frame(root, width=350, height=70, bg="grey40")
Canvas(frame2, width=51, height=24).place(x=149, y=19)
btn = Button(frame2, border=0, command=quiting, text="  Close   ", padx=2, pady=3, bg="grey40", fg="white")
btn.bind("<Return>", quiting)
btn.place(x=150, y=20)
i = 1


def filename():
    nm = "screeshot-"
    exe = ".png"
    dat = datetime.datetime.now()
    ch = str(dat)[:19]
    ch = ch.replace(":", "-")
    ch = ch.replace(" ", "-")
    name = nm + ch + exe
    return name

def dir():
    dirs = os.getcwd()
    if not os.path.exists(dirs+"/shots"):
        os.mkdir("shots")
    os.chdir(dirs+"/shots")

dir()

while True:

    time.sleep(15)
    img1 = PIL.ImageGrab.grab()
    name = filename()
    print(name)
    img1.save(name)
    lb = Label(frame1, text="Total screenshot  :  " + str(i), bg="grey40", fg="white", font=("consolas", 15, "bold")).place(x=20, y=50)
    i += 1

frame1.pack()
frame2.pack()
root.mainloop()
