import tkinter as tk
from tkinter import messagebox as msg
from turtle import TurtleScreen,RawTurtle
import random
import os
import time
import winsound

#creating gui
wn = tk.Tk()
wn.geometry("900x700")
wn.resizable(width = False,height = False)
wn.title("----Canon Shooting----")
wn["bg"] = "#180833"

def start():
    canvas = tk.Canvas(wn,width = 850,height = 600)
    canvas.place(x = 20,y = 10)
    #Set up the screen
    win = TurtleScreen(canvas)
    win.width = 700
    win.height = 500
    win.bgpic("D:\\CHIRAG FOLDER\\Stars_Background1.gif")
    win.register_shape("D:\\CHIRAG FOLDER\\Cannon.gif")
    win.register_shape("D:\\CHIRAG FOLDER\\Dragi.gif")
    win.tracer(20)
    win.listen()    #For Key Presses

    cannon = RawTurtle(win)
    cannon.shape("D:\\CHIRAG FOLDER\\Cannon.gif")
    cannon.penup()  #Lift pen up(command turtle don't want to draw)
    cannon.goto(-380,-250)

    bomb = RawTurtle(win)
    bomb.shape("arrow")
    bomb.shapesize(1,1)
    bomb.color("red")
    bomb.lt(50)
    bomb.up()
    bomb.goto(-350,-222)
    bomb.state = "ready"

    pen = RawTurtle(win)
    pen.up()
    pen.hideturtle()
    pen.color("green")
    pen.goto(200,-275)
    pen.write("Score:0",font = ("Courier",24,"normal"))

    def shoot():
        bomb.state = "fire"

    def bomb_shot():
        bomb.fd(20)
        if bomb.ycor()<-300 or bomb.ycor()>300 or bomb.xcor()>400:
            bomb.goto(-340,-240)
            bomb.state = "ready"

    def turn_right():
        if bomb.state == "ready":
            bomb.rt(10)

    def turn_left():
        if bomb.state == "ready":
            bomb.lt(10)

    win.onkey(shoot,"space")
    win.onkey(turn_left,"Left")
    win.onkey(turn_right,"Right")

    enemy_list = []
    game_over = False
    score = 0

    while not game_over:
        win.update()
        time.sleep(0.010)

        if bomb.state == "fire":
            bomb_shot()

        #Create enemies if there is less than 10
        delay = random.random() #Creates probability 0-1
        if len(enemy_list)<10 and delay<0.05:   #Can play with the delay
            enemy = RawTurtle(win)
            enemy.shape("D:\\CHIRAG FOLDER\\Dragi.gif")

            enemy.penup()
            enemy.goto(420,random.randint(0,280))
            enemy_list.append(enemy)

        for i in enemy_list:
            #enemies move left
            i.goto(i.xcor()-0.5,i.ycor())

            #if enemy out on the left - game over
            if i.xcor()<-420:
                winsound.PlaySound("D:\\CHIRAG FOLDER\\Boom.wav",winsound.SND_ASYNC)
                i.goto(1000,1000) #hide off screen

                enemy_list.remove(i)
                game_over = True
                pen.goto(0,0)
                pen.clear()
                pen.write(f"GAME OVER\nScore:{score}",align = "center",
                          font = ("Agency FB",36,"normal"))


            if bomb.distance(i)<30:
                winsound.PlaySound("D:\\CHIRAG FOLDER\\Bullet.wav",winsound.SND_ASYNC)
                i.goto(1000,1000) #hide off screen
                enemy_list.remove(i)
                bomb.goto(-340,-240)
                bomb.state = "ready"
                score+=1
                pen.clear()
                pen.write(f"Score:{score}",font = ("Agency FB",24,"normal"))

start_game = tk.Button(wn,text = "Start",width = 20,height = 1,
                       font = ("Agency FB",20),bg = "#180833",bd = 4,
                       fg = "white",activebackground = "yellow",command = start)
start_game.place(x = 350,y = 620)
wn.mainloop()
