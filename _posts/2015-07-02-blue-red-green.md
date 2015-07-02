---
title: "Blue, Red, Green!"
layout: post
published: true
categories: showcase shivam
---

> Shivam has put a twist on the game of rock-paper-scissors by writing this Python program (using the GUI toolkit TKinter) of "Blue, Red, Green!"

> The file can be downloaded [here](/files/showcase/Shivam/Python_BLUE_RED_GREEN.py)

> Take a look at the code that went into it below:

    from Tkinter import*
    import Tkinter as tk
    import sys, Tkinter
    import random
    tk=Tk()
    
    canvas=Canvas(tk,width=700,height=700,background='cyan')
    canvas.pack()
    
    canvas.create_text(510,50,text='YOU',font='1000')
    canvas.create_text(180,50,text='ME/COMPUTER',font='1000')
    
    canvas.create_text(350,690,text='Blue beats red,    red beats green   and green beats blue',font='1000')
    
    def game():
            canvas.create_rectangle(0,0,700,700,fill='cyan',outline='cyan')
            canvas.create_text(510,50,text='YOU',font='1000')
            canvas.create_text(180,50,text='ME/COMPUTER',font='1000')
            canvas.create_text(350,690,text='Blue beats red,    red beats green   and green beats blue',font='1000')
            
            canvas.create_rectangle(500,150,550,175,fill='blue')
            canvas.create_rectangle(500,350,550,375,fill='red')
            canvas.create_rectangle(500,550,550,575,fill='green')
            canvas.create_rectangle(150,150,200,175,fill='blue')
            canvas.create_rectangle(150,350,200,375,fill='red')
            canvas.create_rectangle(150,550,200,575,fill='green')
            
            canvas.create_rectangle(575,150,625,175,fill='cyan',outline='cyan')
            canvas.create_rectangle(575,350,625,375,fill='cyan',outline='cyan')
            canvas.create_rectangle(575,550,625,575,fill='cyan',outline='cyan')
    
            canvas.create_rectangle(75,550,125,575,fill='cyan',outline='cyan')
            canvas.create_rectangle(75,350,125,375,fill='cyan',outline='cyan')
            canvas.create_rectangle(75,150,125,175,fill='cyan',outline='cyan')
            
    btn=Button(tk,text="Start a new game",command=game)
    btn.pack()
    
    def computor(human):
        choice=random.choice(["blue","red","green"])
        if choice=="blue":
            canvas.create_rectangle(75,150,125,175,fill='yellow')
            winner(human,choice)
        if choice=="red":
            canvas.create_rectangle(75,350,125,375,fill='yellow')
            winner(human,choice)
        if choice=="green":
            canvas.create_rectangle(75,550,125,575,fill='yellow')
            winner(human,choice)
          
    def hello():
        canvas.create_rectangle(575,150,625,175,fill='yellow')
        computor('blue')
    
    btn=Button(tk,text="BLUE",command=hello)
    btn.pack()
    
    def hello2():
          canvas.create_rectangle(575,350,625,375,fill='yellow')
          computor('red')
    
    btn=Button(tk,text="RED",command=hello2)
    btn.pack()
    
    def hello3():
          canvas.create_rectangle(575,550,625,575,fill='yellow')
          computor('green')
          
    btn=Button(tk,text="GREEN",command=hello3)
    btn.pack()
    
    def winner(human,computer):
            if human=='blue' and computer=='blue':
                    canvas.create_text(350,350,text='ITS AT TIE, DARE TO GO AGAIN !!!',fill='red',font='1000')
            if human=='blue' and computer=='red':
                    canvas.create_text(350,350,text='YOU WIN!!!',fill='red',font='1000')
            if human=='blue' and computer=='green':
                    canvas.create_text(350,350,text='HAHA I WIN !!!',fill='red',font='1000')
            if human=='red' and computer=='blue':
                    canvas.create_text(350,350,text='HAHA I WIN !!!',fill='red',font='1000')
            if human=='red' and computer=='red':
                    canvas.create_text(350,350,text='ITS AT TIE, DARE TO GO AGAIN !!!',fill='red',font='1000')
            if human=='red' and computer=='green':
                    canvas.create_text(350,350,text='YOU WIN!!!',fill='red',font='1000')
            if human=='green' and computer=='blue':
                    canvas.create_text(350,350,text='YOU WIN!!!',fill='red',font='1000')
            if human=='green' and computer=='red':
                    canvas.create_text(350,350,text='HAHA I WIN!!!',fill='red',font='1000')
            if human=='green' and computer=='green':
                    canvas.create_text(350,350,text='ITS AT TIE, DARE TO GO AGAIN !!!',fill='red',font='1000')
    
    while 1:
        tk.update_idletasks()
        tk.update()
