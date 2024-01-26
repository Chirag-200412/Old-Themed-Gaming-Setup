#doubt
import turtle
import time
import tkinter as tk
from tkinter import messagebox as msg
from turtle import TurtleScreen,RawTurtle
import random

#creating gui
win = tk.Tk()
win.geometry("1050x680")
win.resizable(width = False,height = False)
win.title("----Football----")
win["bg"] = "#180833"

def start():
    canvas = tk.Canvas(win,width = 1000,height = 560)
    canvas.place(x = 20,y = 10)
    #set up the screen
    mscreen = TurtleScreen(canvas)
    mscreen.register_shape("D:\\CHIRAG FOLDER\\Stadium.gif")
    mscreen.register_shape("D:\\CHIRAG FOLDER\\Football.gif")
    mscreen.width = 1000
    mscreen.height = 560
    mscreen.bgcolor("green")
    mscreen.bgpic("D:\\CHIRAG FOLDER\\Stadium.gif")

    #line boundry
    l = RawTurtle(mscreen)
    l.hideturtle()
    l.speed(0)
    l.color("black")
    l.pensize(10)
    l.lt(90)
    l.fd(270)
    l.lt(90)
    l.fd(500)
    l.lt(90)
    l.fd(540)
    l.lt(90)
    l.fd(990)
    l.lt(90)
    l.fd(540)
    l.lt(90)
    l.fd(490)
    l.lt(90)
    l.fd(540)
    l.setpos(0,0)

    #start circle
    cir = RawTurtle(mscreen)
    cir.speed(0)
    cir.ht()
    cir.rt(90)
    cir.penup()
    cir.fd(54)
    cir.pendown()
    cir.lt(90)
    cir.pensize(10)
    cir.color("silver")
    cir.circle(40)

    #ball
    ball = RawTurtle(mscreen)
    ball.ht()
    ball.rt(90)
    ball.penup()
    ball.fd(13)
    ball.showturtle()
    ball.shape("D:\\CHIRAG FOLDER\\Football.gif")
    ball.shapesize(2)
    ball.left(45)
    ball.speed(5)
    ball.dx = 2
    ball.dy = -2

    #player 1
    player1 = RawTurtle(mscreen)
    player1.ht()
    player1.shape("square")
    player1.shapesize(2,4)
    player1.color("white")
    player1.lt(90)
    player1.penup()
    player1.goto(300,0)
    player1.showturtle()

    #player 2
    player2 = RawTurtle(mscreen)
    player2.ht()
    player2.shape("square")
    player2.shapesize(2,4)
    player2.color("white")
    player2.lt(90)
    player2.penup()
    player2.goto(-300,0)
    player2.showturtle()

    #pen
    pen = RawTurtle(mscreen)
    pen.ht()
    pen.color("white")
    pen.pensize(10)
    pen.penup()
    pen.goto(0,150)
    pen.pendown()

    #score board variable
    s1 = RawTurtle(mscreen)
    s1.ht()
    s1.pensize(10)
    s2 = RawTurtle(mscreen)
    s2.ht()
    s2.pensize(10)

    def up1():
        player1.speed(0)
        player1.fd(30)
    def up2():
        player2.speed(0)
        player2.fd(30)
    def down1():
        player1.speed(0)
        player1.bk(30)
    def down2():
        player2.speed(0)
        player2.bk(30)

    #functions
    mscreen.listen()
    mscreen.onkey(up1,'Up')
    mscreen.onkey(up2,'w')
    mscreen.onkey(down1,'Down')
    mscreen.onkey(down2,'s')

    #pad boundary collision
    def boom():
        if player1.ycor()>=190:
            player1.setpos(300,180)
    def boom2():
        if player1.ycor()<=-190:
            player1.setpos(300,-180)
    def boom1():
        if player2.ycor()>=190:
            player2.setpos(-300,180)
    def boom3():
        if player2.ycor()<=-190:
            player2.setpos(-300,-180)

    #boundary collision with ball
    def collide():
        if ball.ycor()<=-230 and ball.xcor()>0:
            ball.sety(-230)
            ball.dy *= -1

        elif ball.ycor()<=-230 and ball.xcor()<0:
            ball.sety(-230)
            ball.dy *= -1

        elif ball.ycor()>=230 and ball.xcor()>0:
            ball.sety(230)
            ball.dy *= -1

        elif ball.ycor()>=230 and ball.xcor()<0:
            ball.sety(230)
            ball.dy *= -1

        elif ball.xcor()<=-500 and ball.ycor()<270 and ball.ycor()>135:
            ball.speed(1)
            ball.home()

        elif ball.xcor()>=500 and ball.ycor()<270 and ball.ycor()>135:
            ball.speed(1)
            ball.home()

        elif ball.xcor()<=-500 and ball.ycor()>-270 and ball.ycor()<-135:
            ball.speed(1)
            ball.home()

        elif ball.xcor()>=500 and ball.ycor()>-270 and ball.ycor()<-135:
            ball.speed(1)
            ball.home()

    #ball and pad collision
    def padoball():
        if player1.xcor() == ball.xcor() and player1.ycor() == ball.ycor() or ball.xcor()<player1.xcor()+10 and ball.xcor()>player1.xcor()-10 and ball.ycor()<player1.ycor()+10 and ball.ycor()>player1.ycor()-10:
            ball.setx(230)
            ball.dx *= -1
    def padoball1():
        if player2.xcor() == ball.xcor() and player2.ycor() == ball.ycor() or ball.xcor()<player2.xcor()+10 and ball.xcor()>player2.xcor()-10 and ball.ycor()<player2.ycor()+10 and ball.ycor()>player2.ycor()-10:
            ball.setx(-230)
            ball.dx *= -3

    score = 0
    scoree = 0

    while True:
        ball.setx(ball.xcor()+ball.dx)
        ball.sety(ball.ycor()+ball.dy)
        boom()
        boom2()
        boom1()
        boom3()
        collide()
        padoball()
        padoball1()
        padoball()
        padoball1()

        #Goal for player 2
        if ball.xcor()<=-400 and ball.xcor()>=-500 and ball.ycor()<=135 and ball.ycor()>=-135:
            pen.write("GOAL BY PLAYER 2!",align='center',font = ('arial',26,'normal'))
            time.sleep(2)
            pen.undo()
            ball.speed(1)
            ball.home()
            ball.right(120)
            padoball()
            padoball1()
            score+=1
            s1.undo()
            s1.penup()
            s1.pensize(10)
            s1.goto(200,270)
            s1.color('crimson')
            scoreq = "GOAL:%s" %score
            s1.write(scoreq,False,align = "left",font = ('courier',16,'normal'))
            if score>=3:
                pen.write("PLAYER 2 WINS",align = 'center',font = ("arial",26,"normal"))
                time.sleep(2)

        #Goal for player 1
        if ball.xcor()>=400 and ball.xcor()>=500 and ball.ycor()<=135 and ball.ycor()>=-135:
            pen.write("GOAL BY PLAYER 1!",align='center',font = ('arial',26,'normal'))
            time.sleep(2)
            pen.undo()
            ball.speed(1)
            ball.home()
            ball.left(120)
            padoball()
            padoball1()
            scoree+=1
            s1.undo()
            s1.penup()
            s1.pensize(10)
            s1.goto(-200,270)
            s1.color('blue')
            scorea = "GOAL:%s" %scoree
            s1.write(scorea,False,align = "left",font = ('courier',16,'normal'))
            if scoree>=3:
                pen.write("PLAYER 1 WINS",align = 'center',font = ("arial",26,"normal"))
                time.sleep(2)

start_game = tk.Button(win,text = "Start",width = 20,height = 1,
font = ("Agency FB",20),bg = "#180833",bd = 4,
fg = "white",activebackground = "yellow",command = start)
start_game.place(x = 400,y = 600)
win.mainloop()
