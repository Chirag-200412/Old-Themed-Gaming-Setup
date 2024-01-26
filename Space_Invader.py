import turtle
import random
import time
import tkinter as tk
from turtle import TurtleScreen,RawTurtle
from tkinter import messagebox as msg
#import os #Only for linux
import math
import winsound

#creating gui
wn = tk.Tk()
wn.geometry("800x750")
wn.resizable(width = False,height = False)
wn.title("----Space Invader----")
wn['bg'] = "#180833"


def start():
    canvas = tk.Canvas(wn,width = 750,height = 650)
    canvas.place(x = 20,y = 10)
    #set up the screen
    win = TurtleScreen(canvas)

    #Register the shapes
    win.register_shape("D:\\CHIRAG FOLDER\\Stars_Background1.gif")
    win.register_shape("D:\\CHIRAG FOLDER\\Alien.gif")
    win.register_shape("D:\\CHIRAG FOLDER\\SpaceShip.gif")
    win.register_shape("D:\\CHIRAG FOLDER\\GameOver.gif")

    win.bgpic("D:\\CHIRAG FOLDER\\Stars_Background1.gif")
    
    #set the score to 0
    score = 0

    #draw the pen
    score_pen = RawTurtle(win)
    score_pen.speed(0)
    score_pen.color("yellow")
    score_pen.penup()
    score_pen.setpos(-370,290)
    scorestring = "Score:%s" %score
    score_pen.write(scorestring,False,align = "left",font = ("Arial",14,"normal"))
    score_pen.ht()

    #Create the player turtle
    player = RawTurtle(win)
    player.shape("D:\\CHIRAG FOLDER\\SpaceShip.gif")
    player.penup()
    player.speed(0)
    player.setpos(0,-250)
    player.setheading(90)

    playerspeed = 25

    #Choose a number of enemies
    number_of_enemies = 10
    #create an empty list of enemies
    enemies = []

    #Add enemies to the list
    for i in range(number_of_enemies):
        #create the enemies
        enemies.append(RawTurtle(win))

    for enemy in enemies:
        enemy.shape("D:\\CHIRAG FOLDER\\Alien.gif")
        enemy.penup()
        enemy.speed(0)
        x = random.randint(-200,200)
        y = random.randint(100,250)
        enemy.setpos(x,y)
    enemyspeed = 5

    #create the player's bullet
    bullet = RawTurtle(win)
    bullet.color("yellow")
    bullet.shape("triangle")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(1.0,1.0)
    bullet.ht()

    bulletspeed = 150

    #Move the player left and right
    def move_left():
        x = player.xcor()
        x -= playerspeed
        if x<-280:
            x = -280
        player.setx(x)

    def move_right():
        x = player.xcor()
        x += playerspeed
        if x>280:
            x = 280
        player.setx(x)

    #bullet state fix
    global bulletstate
    bulletstate = "ready"

    def fire_bullet():
        #Declare bulletstate as a global if it needs changed
        global bulletstate
        if bulletstate == "ready":
            bulletstate = "fire"
            #Move the bullet to the just above the player
            winsound.PlaySound("D:\\CHIRAG FOLDER\\Bullet.wav",winsound.SND_ASYNC)

            x = player.xcor()
            y = player.ycor()+10
            bullet.setpos(x,y)
            bullet.showturtle()
            
    #For Collision between enemy and bullet
    def isCollision_enemy_bullet(t1,t2):
        distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        if distance<35:
            return True
        else:
            return False

    #For Collision between enemy and player
    def isCollision_enemy_player(t1,t2):
        distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        if distance<100:
            return True
        else:
            return False
        
    #Create keyboard bindings
    win.listen()
    win.onkey(move_left,"Left")
    win.onkey(move_right,"Right")
    win.onkey(fire_bullet,"space")

    #main game loop
    Game_Over = False
    missed_enemies = 0
    while True:
        for enemy in enemies:
            #Move the enemies
            x = enemy.xcor()
            x+=enemyspeed
            enemy.setx(x)

            #move the enemy back and down
            if enemy.xcor()>270:
                #Move all enemies down
                for e in enemies:
                    y = e.ycor()
                    y-=40
                    e.sety(y)
                    if e.ycor()<-285 and Game_Over == False:
                        e.ht()
                        missed_enemies += 1
                        if missed_enemies == 5:
                            Game_Over = True
                        x = random.randint(-200,200)
                        y = random.randint(100,250)
                        e.setpos(x,y)
                        e.showturtle()
                #change enemy direction
                enemyspeed *= -1

            if enemy.xcor()<-270:
                #Move all enemies down
                for e in enemies:
                    y = e.ycor()
                    y-=40
                    e.sety(y)
                    if e.ycor()<-285 and Game_Over == False:
                        e.ht()
                        missed_enemies += 1
                        if missed_enemies == 5:
                            Game_Over = True
                        x = random.randint(-200,200)
                        y = random.randint(100,250)
                        e.setposition(x,y)
                        e.showturtle()
                #change enemy direction
                enemyspeed*=-1

            #check for a collision between the bullet and the enemy
            if isCollision_enemy_bullet(bullet,enemy):
                time.sleep(0.05)
                winsound.PlaySound("D:\\CHIRAG FOLDER\\Boom.wav",winsound.SND_ASYNC)

                #Reset the bullet
                bullet.ht()
                bulletstate = "ready"
                bullet.setposition(0,-400)
                #Reset the enemy
                x = random.randint(-200,200)
                y = random.randint(100,250)
                enemy.setpos(x,y)
                enemyspeed+=0.5
                #update the score
                score+=10
                scorestring = "Score:%s" %score
                score_pen.clear()
                score_pen.write(scorestring,False,align="left",font = ("Arial",14,"normal"))

            #check for a collision between the player and the enemy
            if isCollision_enemy_player(player,enemy):
                winsound.PlaySound("D:\\CHIRAG FOLDER\\Boom1.wav",winsound.SND_ASYNC)

                Game_Over = True
            if Game_Over == True:
                player.ht()
                bullet.ht()
                for e in enemies:
                    e.ht()
                win.bgpic("D:\\CHIRAG FOLDER\\GameOver.gif")
                break

        #Move the bullet
        if bulletstate == "fire":
            y = bullet.ycor()
            y+=bulletspeed
            bullet.sety(y)

        #check to see if the bullet has gone to the top
        if bullet.ycor()>275:
            bullet.ht()
            bulletstate = "ready"
            
start_game = tk.Button(wn,text = "Start",width = 20,height = 1,
             font = ("Agency FB",26),bg = "#180833",
             fg = "Green",activebackground = "yellow",bd = 4,command = start)
start_game.place(x = 300,y = 680)
wn.mainloop()
