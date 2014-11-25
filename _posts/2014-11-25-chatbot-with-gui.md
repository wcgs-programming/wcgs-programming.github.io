---
title: "Chatbot with GUI (WIP)"
layout: post
published: true
categories: showcase vithurun-vasanthakumar
---

> A work-in-progress at the moment, this program talks to the user through a GUI (window with coloured text + buttons). It uses the skills that Vithurun is learning in Mr Joyce's CS classes at the moment.

> Take a look at the code:

    import sys, Tkinter
    sys.modules['tkinter'] = Tkinter # put the module where python looks first for modules
    from tkinter import *
    tk = Tk()
    def hello():
        canvas.create_text(400, 120, text='Hello.What is your name', fill="maroon")
        canvas.create_text(400, 140, text='Hi .......................................!', fill="white")
        canvas.create_text(400, 160, text='What do you like most about yourself?', fill="maroon")
        canvas.create_text(400, 180, text='Oh I see, well I personaly like chating to people!', fill="white")
        canvas.create_text(400, 200, text='Well my name is .C.H.A.T.', fill="maroon")
        canvas.create_text(400, 220, text='Which means Chatty.Heroic.Acrobatic.Telegram', fill="white")
        canvas.create_text(400, 240, text='Follow me on instagram @The_Man_Of_Everything', fill="maroon")

    btn=Button(tk,text="CLICK ME:):):):):):):):):):):):):)", command = hello)
    btn.pack()
    canvas=Canvas(tk, width=800,height=800)
    canvas.pack()

    myimage = PhotoImage(file='u:\\Robot for chatbot.gif')
    canvas.create_image(0, 0, anchor=NW, image=myimage)

    while 1:
          tk.update_idletasks()
          tk.update()
