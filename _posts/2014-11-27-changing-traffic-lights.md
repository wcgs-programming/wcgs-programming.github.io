---
title: "Changing Traffic Lights"
layout: post
published: true
categories: showcase mathushun
---

> Using his Python skills, Mathushun has drawn a simple version of changing traffic Lights.
> You can download it [here](/files/showcase/Mathushun/changing-traffic-lights.py).

> This is the code Mathushun wrote to do it:
	from Tkinter import*
	import Tkinter as tk
	import sys, Tkinter
	tk = Tk()

	canvas = Canvas(tk,width=500,height=500)
	canvas.pack()
	canvas.create_oval(10, 10,110,110, fill="red")
	canvas.create_oval(10,110,110,210, fill="orange")
	canvas.create_oval(10,210,110,310, fill="grey")

	def change():
		canvas = Canvas(tk,width=500,height=500)
		canvas.pack()
		canvas.create_oval(10, 10,110,110, fill="grey")
		canvas.create_oval(10,110,110,210, fill="grey")
		canvas.create_oval(10,210,110,310, fill="green")    

	btn = Button(tk,text="Click to change colours...",command=change)
	btn.pack()

	while 1:
		tk.update_idletasks()
		tk.update()