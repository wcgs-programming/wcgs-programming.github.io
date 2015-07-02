---
title: "Rectangles"
layout: post
published: true
categories: showcase pranav
---

> Using his Python skills, Pranav has drawn some rectangles.
> You can download it [here](/files/showcase/Pranav/rectangle.py).

> This is the code Pranav wrote to do it:

	from Tkinter import *
	import Tkinter as tk
	import sys, Tkinter
	tk = Tk()

	canvas = Canvas(tk, width=400,height=400)
	canvas.pack()
	canvas.create_rectangle(100, 100, 200, 200, fill="blue",outline="black")

	canvas.create_rectangle(200, 200, 300, 300, fill="red",outline="black")

	canvas.create_rectangle(300, 300, 400, 400, fill="dark blue",outline="black")

	while 1:
		tk.update_idletasks()
		tk.update()