import turtle
import random
import time
import tkinter as tk
from turtle import TurtleScreen,RawTurtle

#creating gui
wn = tk.Tk()
wn.geometry("900x700")
wn.resizable(width = False,height = False)
wn.title("----Balancing Ball----")
wn["bg"] = "#180833"

#Canvas
def start():
    canvas = tk.Canvas(wn,width = 850,height = 600,bg = "black")
    canvas.place(x = 20,y = 10)
    win = TurtleScreen(canvas)
    win.addshape("D:\\CHIRAG FOLDER\\Strawberry_2.gif")
    win.addshape("D:\\CHIRAG FOLDER\\Balance_background.gif")
    win.addshape("D:\\CHIRAG FOLDER\\Ball.gif")

    win.width = 800
    win.height = 600
    win.bgcolor("#27d676")
    win.bgpic("D:\\CHIRAG FOLDER\\Balance_background.gif")
    win.tracer(0)
    paddle = RawTurtle(win)
    paddle.shape("square")
    paddle.shapesize(stretch_len = 5,stretch_wid = 1)
    paddle.penup()
    paddle.goto(0,-270)

    #ball
    ball = RawTurtle(win)
    ball.dx=5
    ball.dy=5
    ball.shape("D:\\CHIRAG FOLDER\\Ball.gif")
    ball.color("silver")
    ball.penup()

    #pen
    pen = RawTurtle(win)
    pen.color("black")
    pen.penup()
    pen.ht()
    pen.goto(310,-220)
    pen.write("Score:0",align = "center",font = ("Agency FB",24,"normal"))
    colors = ["red","blue","green","cyan","purple","yellow","orange"]
    score = 0

    def paddle_right():
        if paddle.xcor()<350:
            paddle.setx(paddle.xcor()+80)

    def paddle_left():
        if paddle.xcor()>-350:
            paddle.setx(paddle.xcor()-80)

    def border_check():
        if ball.ycor()>280:
            ball.dy *= -1
        if ball.xcor()>380 or ball.xcor()<-380:
            ball.dx *= -1

    def paddle_check():
        if ball.ycor()-10<=paddle.ycor()+10 and ball.dy<0:
            if ball.xcor()-10<=paddle.xcor()+50 and ball.xcor()+10>=paddle.xcor()-50:
                ball.dy *= -1

    def falling_block():
        for i in block_list:
            if i.state == "falling":
                i.shape("circle")
                i.l = i.xcor()-10
                i.r = i.xcor()+10
                i.shapesize(1,1)
                i.goto(i.xcor(),i.ycor()+i.dy)

    win.listen()
    win.onkey(paddle_right,"Right")
    win.onkey(paddle_left,"Left")

    x_list = [-340,-230,-120,-10,100,210,320]
    y_list = [280,255,230,205,180]
    block_list = []

    for i in y_list:
        for j in x_list:
            block = RawTurtle(win)
            block.shape("D:\\CHIRAG FOLDER\\Strawberry_2.gif")
            block.shapesize(stretch_len = 5,stretch_wid = 1)
            block.c = (random.choice(colors))
            block.color(block.c)
            block.penup()
            block.goto(j,i)
            block.state = "ready"
            block.l = block.xcor()-50
            block.r = block.xcor()+50
            block_list.append(block)

    block_count = len(block_list)

    x = 0.015
    while block_count>0:
        if score<=10:
            x = 0.015
        else:
            x = 0.011

        time.sleep(x)

        win.update()
        ball.goto(ball.xcor()+ball.dx,ball.ycor()+ball.dy)
        border_check()
        paddle_check()
        falling_block()

        #Autopilot
        #if ball.xcor()>-350 and ball.xcor()<350:
            #paddle.setx(ball.xcor())

        if ball.ycor()<=-300:
            ball.goto(0,0)
            if score>0:
                score -= 1
            pen.clear()
            pen.write(f"Score:{score}",align = "center",font = ("Agency FB",24,"normal"))

        #Block collisions
        for i in block_list:
            if(i.l<=ball.xcor()<=i.r) and (i.ycor()-10<=ball.ycor()<=i.ycor()+10) and i.state=="ready":
                ball.dy*=-1
                i.state="falling"
                i.dy=-2
                score += 1
                pen.clear()
                paddle.color(i.c)
                pen.clear()
                pen.write(f"Score:{score}",align = "center",font = ("Agency FB",24,"normal"))

            if(paddle.xcor()-50<i.xcor()<paddle.xcor()+50) and (paddle.ycor()-10<i.ycor()<=paddle.ycor()+10) and i.dy<0:
                i.dy *= -1
            if i.ycor()<-320 or i.ycor()>320:
                block_list.remove(i)
                block_count = len(block_list)


    #Game Over
    pen.clear()
    pen.goto(0,0)
    pen.write(f"GAME OVER\nScore:{score}",align = "center",font = ("Agency FB",24,"normal"))
    

start_game = tk.Button(wn,text = "Start",width = 20,height = 1,
             font = ("Agency FB",26),bg = "#180833",
             fg = "Green",activebackground = "yellow",bd = 4,command = start)
start_game.place(x = 350,y = 620)
wn.mainloop()
