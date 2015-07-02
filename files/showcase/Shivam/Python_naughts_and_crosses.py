from Tkinter import*
import Tkinter as tk
import sys, Tkinter
tk=Tk()
canvas=Canvas(tk,width=300,height=300)
canvas.pack()
Winner = False
board = [['','',''],
         ['','',''],
         ['','','']]


def hi1():
    canvas.create_rectangle(0,0,100,100,fill="white")
    canvas.create_rectangle(0,100,100,200,fill="white")
    canvas.create_rectangle(0,200,100,300,fill="white")
    canvas.create_rectangle(100,0,200,100,fill="white")
    canvas.create_rectangle(100,100,200,200,fill="white")
    canvas.create_rectangle(100,200,200,300,fill="white")
    canvas.create_rectangle(200,0,300,100,fill="white")
    canvas.create_rectangle(200,100,300,200,fill="white")
    canvas.create_rectangle(200,200,300,300,fill="white")
    Winner = False
b2=Button(tk,text="BLANK PAGE",command=hi1)
b2.pack()


















def hello9():
    global board, Winner
    board = [['','',''],
             ['','',''],
             ['','','']]
    canvas.create_rectangle(0,0,100,100,fill="blue")
    canvas.create_rectangle(0,100,100,200,fill="red")
    canvas.create_rectangle(0,200,100,300,fill="blue")
    canvas.create_rectangle(100,0,200,100,fill="red")
    canvas.create_rectangle(100,100,200,200,fill="blue")
    canvas.create_rectangle(100,200,200,300,fill="red")
    canvas.create_rectangle(200,0,300,100,fill="blue")
    canvas.create_rectangle(200,100,300,200,fill="red")
    canvas.create_rectangle(200,200,300,300,fill="blue")
    Winner = False
btn9=Button(tk,text="REFRESH GAME/ START NEW GAME",command=hello9)
btn9.pack()






def hello():
    if(not Winner and board[0][0]==''):
       canvas.create_text(50,50,text="X")
       board[0][0] = 'x'
    else:
        hello9()
btn=Button(tk,text="X-TOP LEFT",command=hello)
btn.pack()

def hello1():
    if(not Winner and board[0][1]==''):
      canvas.create_text(50,150,text="X",font=100)
      board[0][1] = 'x'
btn1=Button(tk,text="X-MIDDLE LEFT",command=hello1)
btn1.pack()

def hello2():
    if(not Winner and board[0][2]==''):
      canvas.create_text(50,250,text="X")
      board[0][2] = 'x'
btn2=Button(tk,text="X-BOTTOM LEFT",command=hello2)
btn2.pack()

def hello3():
    if(not Winner and board[1][0]==''):
      canvas.create_text(150,50,text="X")
      board[1][0] = 'x'
btn3=Button(tk,text="X-MIDDLE TOP",command=hello3)
btn3.pack()

def hello4():
    if(not Winner and board[1][1]==''):
      canvas.create_text(150,150,text="X")
      board[1][1] = 'x'
btn4=Button(tk,text="X-MIDDLE",command=hello4)
btn4.pack()

def hello5():
    if(not Winner and board[1][2]==''):
      canvas.create_text(150,250,text="X")
      board[1][2] = 'x'
btn5=Button(tk,text="X-MIDDLE BOTTOM",command=hello5)
btn5.pack()

def hello6():
    if(not Winner and board[2][0]==''):
      canvas.create_text(250,50,text="X")
      board[2][0] = 'x'
btn6=Button(tk,text="X-TOP RIGHT",command=hello6)
btn6.pack()

def hello7():
    if(not Winner and board[2][1]==''):
      canvas.create_text(250,150,text="X")
      board[2][1] = 'x'
btn7=Button(tk,text="X-MIDDLE RIGHT",command=hello7)
btn7.pack()

def hello8():
    if(not Winner and board[2][2]==''):
      canvas.create_text(250,250,text="X")
      board[2][2] = 'x'
btn8=Button(tk,text="X-BOTTOM RIGHT",command=hello8)
btn8.pack()









def hello0():
    if(not Winner and board[0][0]==''):
      canvas.create_text(50,50,text="0")
      board[0][0] = '0'
btn0=Button(tk,text="0-TOP LEFT",command=hello0)
btn0.pack()

def hello11():
    if(not Winner and board[0][1]==''):
      canvas.create_text(50,150,text="0")
      board[0][1] = '0'
btn11=Button(tk,text="0-MIDDLE LEFT",command=hello11)
btn11.pack()

def hello22():
    if(not Winner and board[0][2]==''):
      canvas.create_text(50,250,text="0")
      board[0][2] = '0'
btn22=Button(tk,text="0-BOTTOM LEFT",command=hello22)
btn22.pack()

def hello33():
    if(not Winner and board[1][0]==''):
      canvas.create_text(150,50,text="0")
      board[1][0] = '0'
btn33=Button(tk,text="0-MIDDLE TOP",command=hello33)
btn33.pack()

def hello44():
    if(not Winner and board[1][1]==''):
      canvas.create_text(150,150,text="0")
      board[1][1] = '0'
btn44=Button(tk,text="0-MIDDLE",command=hello44)
btn44.pack()

def hello55():
    if(not Winner and board[1][2]==''):
      canvas.create_text(150,250,text="0")
      board[1][2] = '0'
btn55=Button(tk,text="0-MIDDLE BOTTOM",command=hello55)
btn55.pack()

def hello66():
    if(not Winner and board[2][0]==''):
        canvas.create_text(250,50,text="0")
        board[2][0] = '0'
btn66=Button(tk,text="0-TOP RIGHT",command=hello66)
btn66.pack()

def hello77():
    print(Winner)
    if(not Winner and [2][1]==''):
        canvas.create_text(250,150,text="0")
        board[2][1] = '0'
btn77=Button(tk,text="0-MIDDLE RIGHT",command=hello77)
btn77.pack()

def hello88():
    if(not Winner and board[2][2]==''):
      canvas.create_text(250,250,text="0")
      board[2][2] = '0'
btn88=Button(tk,text="0-BOTTOM RIGHT",command=hello88)
btn88.pack()








while 1:


    if(Winner):
        board = [['','',''],
                 ['','',''],
                 ['','','']]
    if(((board[0][0]=='x' and board[0][1]=='x') and (board[0][0]=='x' and board[0][2]=='x')) or ((board[1][0]=='x' and board[1][1]=='x') and (board[1][0]=='x' and board[1][2]=='x')) or ((board[2][0]=='x' and board[2][1]=='x') and (board[2][0]=='x' and board[2][2]=='x')) or ((board[0][0]=='x' and board[1][0]=='x') and (board[0][0]=='x' and board[2][0]=='x')) or ((board[0][1]=='x' and board[1][1]=='x') and (board[0][1]=='x' and board[2][1]=='x')) or ((board[0][2]=='x' and board[1][2]=='x') and (board[0][2]=='x' and board[2][2]=='x')) or ((board[0][0]=='x' and board[1][1]=='x') and (board[0][0]=='x' and board[2][2]=='x')) or ((board[0][2]=='x' and board[1][1]=='x') and (board[2][0]=='x' and board[2][2]=='x'))):
        canvas.create_text(150,275,text="x wins")
        Winner = True

    if(((board[0][0]=='0' and board[0][1]=='0') and (board[0][0]=='0' and board[0][2]=='0')) or ((board[1][0]=='0' and board[1][1]=='0') and (board[1][0]=='0' and board[1][2]=='0')) or ((board[2][0]=='0' and board[2][1]=='0') and (board[2][0]=='0' and board[2][2]=='0')) or ((board[0][0]=='0' and board[1][0]=='0') and (board[0][0]=='0' and board[2][0]=='0')) or ((board[0][1]=='0' and board[1][1]=='0') and (board[0][1]=='0' and board[2][1]=='0')) or ((board[0][2]=='0' and board[1][2]=='0') and (board[0][2]=='0' and board[2][2]=='0')) or ((board[0][0]=='0' and board[1][1]=='0') and (board[0][0]=='0' and board[2][2]=='0')) or ((board[0][2]=='0' and board[1][1]=='0') and (board[2][0]=='0' and board[2][2]=='0'))):
        canvas.create_text(150,275,text="o wins")
        Winner = True
    tk.update_idletasks()
    tk.update()
