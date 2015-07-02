from Tkinter import *
import Tkinter as tk
import sys, Tkinter
tk = Tk()

canvas = Canvas(tk, width=400,height=400)
canvas.pack()
canvas.create_oval(10,10,90,90,fill='red')
canvas.create_oval(10,110,90,190,fill='orange')
canvas.create_oval(10,210,90,290,fill='green')
    
while 1:
    tk.update_idletasks()
    tk.update()