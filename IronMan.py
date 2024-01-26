import turtle
import os
import random
import time
import tkinter as tk
from tkinter import messagebox as msg
from turtle import TurtleScreen,RawTurtle

win = tk.Tk()
win.geometry("900x700")
win.resizable(width = False,height=False)
win.title("----IRONMAN HUNTING----")
win['bg']='#180833'

def start():
    canvas = tk.Canvas(win,width = 850,height = 600)
    canvas.place(x = 20,y = 10)

    wn = TurtleScreen(canvas)
    wn.bgpic("D:\\CHIRAG FOLDER\\Stars_Background1.gif")
    wn.width = 800
    wn.height = 600
    wn.register_shape("D:\\CHIRAG FOLDER\\IronMan1.gif")
    wn.register_shape("D:\\CHIRAG FOLDER\\IronMan1.gif")
    wn.register_shape("D:\\CHIRAG FOLDER\\Energy.gif")
    wn.register_shape("D:\\CHIRAG FOLDER\\Meteor.gif")
    wn.tracer(0)
    
    score = 0
    lives = 3
    
    player = RawTurtle(wn)
    #player.speed(0)
    player.shape("D:\\CHIRAG FOLDER\\IronMan1.gif")
    player.color('white')
    player.up()
    player.goto(0,-250)
    player.direction = 'stop'

    good_things =[]

    for i in range(20):
        good_thing=RawTurtle(wn)
        good_thing.speed("slow")
        good_thing.shape("D:\\CHIRAG FOLDER\\Energy.gif")
        good_thing.color("Green")
        good_thing.up()
        good_thing.goto(-100,250)
        good_thing.speed=random.randint(1,1)
        good_things.append(good_thing)

    bad_things =[]

    for i in range(10):
        bad_thing=RawTurtle(wn)
        bad_thing.speed("slow")
        bad_thing.shape("D:\\CHIRAG FOLDER\\Meteor.gif")
        bad_thing.color("red")
        bad_thing.up()
        bad_thing.goto(100,250)
        bad_thing.speed=random.randint(1,1)

        bad_things.append(bad_thing)

    pen = RawTurtle(wn)
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.up()
    pen.ht()
    pen.goto(0,260)
    pen.write("Score:0     Lives:3",align="center",
              font=("Agency FB",20,"normal"))

    def go_left():
        player.direction = "left"
        player.shape("D:\\CHIRAG FOLDER\\IronMan1.gif")

    def go_right():
        player.direction = "right"
        player.shape("D:\\CHIRAG FOLDER\\IronMan1.gif")

    wn.listen()
    wn.onkey(go_left,"Left")
    wn.onkey(go_right,"Right")

    while lives > 0:
        wn.update()

        if player.direction == "left":
            player.setx(player.xcor()-1)

        if player.direction == "right":
            player.setx(player.xcor()+1)

        if player.xcor()<-390:
            player.setx(-390)

        elif player.xcor()>390:
            player.setx(390)

        for good_thing in good_things:
            good_thing.sety(good_thing.ycor()-good_thing.speed)

            if good_thing.ycor()<-300:
                good_thing.goto(random.randint(-250,250),random.randint(400,800))

            if player.distance(good_thing)<40:
                score+=10

                pen.clear()
                pen.write("Score:{} Lives:{}".format(score,lives),
                          align="center",font=("Agency FB",20,"normal"))

                good_thing.goto(random.randint(-250,250),random.randint(400,800))

        for bad_thing in bad_things:
            bad_thing.sety(bad_thing.ycor()-bad_thing.speed)

            if bad_thing.ycor()<-300:
                bad_thing.goto(random.randint(-250,250),random.randint(400,800))

            if player.distance(bad_thing)<40:
                score-=10
                lives-=1
                
                pen.clear()
                pen.write("Score:{} Lives:{}".format(score,lives),align="center",font=("Agency FB",20,"normal"))

                time.sleep(1)
                for bad_thing in bad_things:
                    bad_thing.goto(random.randint(-250,250),random.randint(400,800))

    if lives == 0:
        pen.clear()
        pen.write("Game Over! Score:{}".format(score),align="center",font=("Agency FB",18))
        wn.update()
        time.sleep(5)
        score=0
        lives=3
        pen.clear()
        pen.write("Score:{} Lives:{}".format(score,lives),align="center",font=("Agency FB",18))
        
start_game = tk.Button(win,text = "Start",width=20,height=1,
                       font=("Agency FB",20),bg="#180833",bd=4,
                       fg='white',activeforeground='yellow',command=start)
start_game.place(x=350,y=620)

win.mainloop()
