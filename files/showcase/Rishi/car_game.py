#import
from Tkinter import *
import Tkinter as tk
import sys, Tkinter, time
tk = Tk()
#the board is defined
board=[[1,1,1,1,1,1,0,1,1,1,0,1],
       [1,0,1,1,0,1,1,1,0,1,1,1],
       [1,1,0,0,0,0,0,0,0,0,0,1],
       [0,1,0,0,0,0,0,0,0,0,1,1],
       [1,1,1,1,0,1,1,1,1,1,1,0],
       [1,0,1,0,0,1,0,0,0,1,1,1],
       [1,1,1,0,0,1,0,0,0,1,0,1],
       [0,1,1,1,1,1,0,0,0,1,1,1],
       [1,1,0,0,1,1,0,0,0,1,1,0],
       [1,0,0,0,0,1,0,0,0,1,1,1],
       [1,1,0,1,1,1,0,1,1,1,0,1],
       [0,1,1,1,0,1,1,1,0,1,1,1]]

sizeofsquare=50

xnumofsquares=len(board[0])
ynumofsquares=len(board)
width=sizeofsquare*xnumofsquares
height=sizeofsquare*ynumofsquares

#canvas created

canvas = Canvas(tk, width=width, height=height,
                bd=0, highlightthickness=0)
canvas.pack()
#board is created
row = 0
while row < ynumofsquares:
    column = 0
    while column < xnumofsquares: 
        if board[row][column]:
            canvas.create_rectangle(column*sizeofsquare,
                                    row*sizeofsquare,
                                    (column+1)*sizeofsquare,
                                    (row+1)*sizeofsquare,
                                    width=0,
                                    fill="black")
        else:
            canvas.create_rectangle(column*sizeofsquare,
                                    row*sizeofsquare,
                                    (column+1)*sizeofsquare,
                                    (row+1)*sizeofsquare,
                                    width=0,
                                    fill="green")
        column=column+1
    row=row+1



class Car(object):
    
    def __init__(self, goleft,goright,goup,godown):

        self.speed=2
        self.direction="Right"
        self.diameter=sizeofsquare*0.4

        self.u_allowed=False
        self.d_allowed=False
        self.l_allowed=False
        self.r_allowed=False

        self.id = canvas.create_oval(0, 0, self.diameter, self.diameter, fill="red")

        canvas.bind_all(goleft,self.left)
        canvas.bind_all(goright,self.right)
        canvas.bind_all(goup,self.up)
        canvas.bind_all(godown,self.down)

    def left(self, command):
        self.direction="Left"
    
    def right(self, command):
        self.direction="Right"
    
    def up(self, command):
        self.direction="Up"
        
    def down(self, command):
        self.direction="Down"

    def allowed(self):
        left, top, right, bottom = canvas.coords(self.id)

        self.u_allowed = True
        self.d_allowed = True
        self.l_allowed = True
        self.r_allowed = True

        left_s = int(left/sizeofsquare)
        right_s = int(right/sizeofsquare)
        top_s = int(top/sizeofsquare)
        bottom_s = int(bottom/sizeofsquare)
        centre_x = int((left+right)/(2*sizeofsquare))
        centre_y = int((top+bottom)/(2*sizeofsquare))

        if left <= 0 or not board[centre_y][left_s]:
            self.l_allowed = False
        if top <= 0 or not board[top_s][centre_x]:
            self.u_allowed=False
        if right >= width or not board[centre_y][right_s]:
            self.r_allowed=False
        if bottom >= height or not board[bottom_s][centre_x]:
            self.d_allowed=False
            
    def move(self):
        if self.direction == "Left" and self.l_allowed:
            canvas.move(self.id, -self.speed,0)
        elif self.direction=="Right" and self.r_allowed:
            canvas.move(self.id, self.speed,0)
        elif self.direction == "Up" and self.u_allowed:
            canvas.move(self.id, 0,-self.speed)
        elif self.direction=="Down" and self.d_allowed:
            canvas.move(self.id, 0, self.speed)

    def carupdate(self):
        self.allowed()
        self.move()
        

car1=Car(goleft="<KeyPress-Left>",
         goright="<KeyPress-Right>",
         goup="<KeyPress-Up>",
         godown="<KeyPress-Down>")
car2=Car(goleft="<KeyPress-a>",
         goright="<KeyPress-d>",
         goup="<KeyPress-w>",
         godown="<KeyPress-s>") 
while True:
    time.sleep(0.01)
    car1.carupdate()
    car2.carupdate()
    tk.update_idletasks()
    tk.update()
