import turtle
import random as r
import tkinter as tk
from turtle import TurtleScreen,RawTurtle
from tkinter import messagebox as msg
import time

#creating gui
wn = tk.Tk()
wn.geometry("900x700")
wn.resizable(width = False,height = False)
wn.title("---Flappy Bird---")
wn["bg"] = "#2d065c"

l = ["red","blue","green","cyan","purple","yellow","orange"]
#canvas
def start():
    canvas = tk.Canvas(wn,width = 850,height = 600,bg = "black")
    canvas.place(x = 20,y = 10)
    win = TurtleScreen(canvas)
    win.register_shape("D:\\CHIRAG FOLDER\\Flappy_Bird.gif")
    win.register_shape("D:\\CHIRAG FOLDER\\Sky.gif")
    win.bgcolor("blue")
    win.bgpic("D:\\CHIRAG FOLDER\\Sky.gif")
    win.width = 450
    win.height = 500
    win.tracer(0)

    #pen
    pen = RawTurtle(win)
    pen.speed(0)
    pen.ht()
    pen.penup()
    pen.color("white")
    pen.goto(0,250)
    pen.write("0",move = False,align = "left",font = ("Arial",32,"normal"))

    #player
    player = RawTurtle(win)
    player.speed(0)
    player.penup()
    player.shape("D:\\CHIRAG FOLDER\\Flappy_Bird.gif")
    player.goto(-200,0)
    player.dx = 0
    player.dy = 1
    
    #obstacles
    pipe1_top = RawTurtle(win)
    pipe1_top.speed(0)
    pipe1_top.penup()
    r.shuffle(l)
    pipe1_top.color(l[0])
    pipe1_top.shape("square")
    pipe1_top.shapesize(stretch_wid = 18,stretch_len = 3,outline = None)
    pipe1_top.goto(300,250)
    pipe1_top.dx = -2
    pipe1_top.dy = 0
    pipe1_top.value = 1

    pipe1_bottom = RawTurtle(win)
    pipe1_bottom.speed(0)
    pipe1_bottom.penup()
    r.shuffle(l)
    pipe1_bottom.color(l[0])
    pipe1_bottom.shape("square")
    pipe1_bottom.shapesize(stretch_wid = 18,stretch_len = 3,outline = None)
    pipe1_bottom.goto(300,-250)
    pipe1_bottom.dx = -2
    pipe1_bottom.dy = 0

    pipe2_top = RawTurtle(win)
    pipe2_top.speed(0)
    pipe2_top.penup()
    r.shuffle(l)
    pipe2_top.color(l[0])
    pipe2_top.shape("square")
    pipe2_top.shapesize(stretch_wid = 18,stretch_len = 3,outline = None)
    pipe2_top.goto(600,280)
    pipe2_top.dx = -2
    pipe2_top.dy = 0
    pipe2_top.value = 1

    pipe2_bottom = RawTurtle(win)
    pipe2_bottom.speed(0)
    pipe2_bottom.penup()
    r.shuffle(l)
    pipe2_bottom.color(l[0])
    pipe2_bottom.shape("square")
    pipe2_bottom.shapesize(stretch_wid = 18,stretch_len = 3,outline = None)
    pipe2_bottom.goto(600,-220)
    pipe2_bottom.dx = -2
    pipe2_bottom.dy = 0
    
    pipe3_top = RawTurtle(win)
    pipe3_top.speed(0)
    pipe3_top.penup()
    r.shuffle(l)
    pipe3_top.color(l[0])
    pipe3_top.shape("square")
    pipe3_top.shapesize(stretch_wid = 18,stretch_len = 3,outline = None)
    pipe3_top.goto(900,320)
    pipe3_top.dx = -2
    pipe3_top.dy = 0
    pipe3_top.value = 1

    pipe3_bottom = RawTurtle(win)
    pipe3_bottom.speed(0)
    pipe3_bottom.penup()
    r.shuffle(l)
    pipe3_bottom.color(l[0])
    pipe3_bottom.shape("square")
    pipe3_bottom.shapesize(stretch_wid = 18,stretch_len = 3,outline = None)
    pipe3_bottom.goto(900,-180)
    pipe3_bottom.dx = -2
    pipe3_bottom.dy = 0

    gravity = -0.3
    def go_up():
        player.dy+=6

        if player.dy>6:
            player.dy = 6

    #On tap
    def tap(x,y):
        player.dy+=6

        if player.dy>6:
            player.dy = 6

    #Keyboard binding
    win.listen()
    win.onkey(go_up,"space")

    win.onscreenclick(tap,btn = 1)

    #initialize game variable
    player.score = 0
    pipes = [(pipe1_top,pipe1_bottom),(pipe2_top,pipe2_bottom),(pipe3_top,pipe3_bottom)]

    #main game loop
    while True:
        #Pause
        time.sleep(0.02)
        #update the screen
        win.update()

        #Add gravity
        player.dy += gravity

        #Move Player
        y = player.ycor()
        y += player.dy
        player.sety(y)

        #Bottom Border
        if player.ycor()<-390:
            player.dy = 0
            player.sety(-390)

        #iterate through pipes
        for pipe_pair in pipes:
            pipe_top = pipe_pair[0]
            pipe_bottom = pipe_pair[1]

            #Move Pipe 1
            x = pipe_top.xcor()
            x += pipe_top.dx
            pipe_top.setx(x)

            x = pipe_bottom.xcor()
            x += pipe_bottom.dx
            pipe_bottom.setx(x)

            #Return pipes to start
            if pipe_top.xcor()<-350:
                pipe_top.setx(600)
                pipe_bottom.setx(600)
                pipe_top.value = 1

            #Check for collisions with pipes
            #Pipe 1
            if(player.xcor()+10>pipe_top.xcor()-30) and (player.xcor()-10<pipe_top.xcor()+30):
                if(player.ycor()+10>pipe_top.ycor()-180) or (player.ycor()-10<pipe_bottom.ycor()+180):
                    pen.clear()
                    pen.write("Game Over",move = False,align = "center",font = ("Arial",16,"normal"))
                    win.update()
                    time.sleep(2)
                    #Reset Score
                    player.score = 0
                    #Move Pipes back
                    pipe_top.setx(450)
                    pipe_bottom.setx(450)
                    #Move Player back
                    player.goto(-200,0)
                    player.dy = 0
                    #Reset the pen
                    pen.clear()
                    pen.write("0",move = False,align = "center",font = ("Agency FB",16,"normal"))

            #check for score
            if pipe_top.xcor()+30<player.xcor()-10:
                player.score += pipe_top.value
                pipe_top.value = 0
                pen.clear()
                pen.write(player.score,move = False,align = "center",font = ("Agency FB",32,"normal"))
                
                
start_game = tk.Button(wn,text = "Start",width = 8,height = 1,
             font = ("Agency FB",26),bg = "#180833",
             fg = "Green",activebackground = "yellow",bd = 4,command = start)
start_game.place(x = 400,y = 600)
wn.mainloop()
