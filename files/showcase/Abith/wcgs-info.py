from Tkinter import*
import Tkinter as tk
import sys, Tkinter
tk = Tk()

def hello():
    canvas.create_text(400, 120, text='hello world')
    canvas.create_text(400, 135, text='Hey! come to WCGS! Its the best school ever!')
    canvas.create_text(400, 155, text='WCGS is a school founded by Walter Hutchins.')
    canvas.create_text(400, 170, text='The best tie you can get in the school is called the Hutchins tie. You get that by being one of the best people in the school.')
    wcgs = PhotoImage(file = '.\wcgs.gif')
    canvas.create_image(130,185, anchor=NW, image=wcgs)
    root.mainloop
    
btn = Button(tk, text="click me to find out all about WCGS!",command=hello)
btn.pack()

canvas = Canvas(tk,width=800, height=800)
canvas.pack()

while 1:
    tk.update_idletasks()
    tk.update()