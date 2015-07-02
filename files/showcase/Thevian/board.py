from Tkinter import*
import Tkinter as tk
import sys, Tkinter
tk = Tk()

def hello():
    canvas.create_rectangle(0, 0,100,100, fill = "yellow")
    canvas.create_rectangle(0, 100, 100, 200, fill="blue")
    canvas.create_rectangle(0, 200, 100, 300, fill="yellow")
    canvas.create_rectangle(100, 0, 200, 100, fill="blue")
    canvas.create_rectangle(100,100,200,200, fill="yellow")
    canvas.create_rectangle(100,200,200,300, fill="blue")
    canvas.create_rectangle(200,0,300,100 ,fill="yellow")
    canvas.create_rectangle(200,100,300,200, fill="blue")
    canvas.create_rectangle(200,200,300,300, fill="yellow")

btn=Button(text="click", command=hello)
btn.pack()
canvas = Canvas(tk, width=900,height=900)
canvas.pack()



while 1:
    tk.update_idletasks()
    tk.update()
    
