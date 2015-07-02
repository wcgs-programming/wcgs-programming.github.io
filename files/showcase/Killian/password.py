import getpass
from Tkinter import *
import Tkinter as tk
import sys, Tkinter
tk = Tk()

un = raw_input("Username: ")
if un == "bob":
   pw = getpass.getpass("Password: ")
   if pw == "bob":
       canvas = Canvas(tk, width=100, height=100)
       canvas.pack()
       canvas.create_rectangle(10,10,110,120, fill="#00FF00")
       while 1:
          tk.update_idletasks()
          tk.update()
   else:
       canvas = Canvas(tk, width=100, height=100)
       canvas.pack()
       canvas.create_rectangle(10, 10, 110, 120, fill="#FF0000")
       while 1:
          tk.update_idletasks()
          tk.update()
       
else:
   canvas = Canvas(tk, width=100, height=100)
   canvas.pack()
   canvas.create_rectangle(10, 10, 110, 120, fill="#FF0000")
   while 1:
       tk.update_idletasks()
       tk.update()
