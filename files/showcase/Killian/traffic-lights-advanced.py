from Tkinter import *
import Tkinter as tk
import sys, Tkinter
import time
tk = Tk()

def red():
    canvas.create_oval(10,10,90,90, fill="#000000")
def yellow():
    canvas.create_oval(10,110,90,190, fill="#000000")
def green():
    canvas.create_oval(10,210,90,290, fill="#000000")
def clear():
    canvas.create_oval(10,10,90,90, fill="#FF0000")
    canvas.create_oval(10,110,90,190, fill="#FFFF00")
    canvas.create_oval(10,210,90,290, fill="#00FF00")


canvas = Canvas(tk, width=300, height=400)
canvas.pack()
canvas.create_oval(10,10,90,90, fill="#FF0000")
canvas.create_oval(10,110,90,190, fill="#FFFF88")
canvas.create_oval(10,210,90,290, fill="#00FF00")

btn = Button(tk, text="Red", command=red)
btn.pack()
btn = Button(tk, text="Yellow", command=yellow)
btn.pack()
btn = Button(tk, text="Green", command=green)
btn.pack()
btn = Button(tk, text="Clear", command=clear)
btn.pack()




while 1:
    tk.update_idletasks()
    tk.update()
 
