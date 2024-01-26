import turtle as t
import tkinter as tk
from tkinter import messagebox as msg
from turtle import TurtleScreen,RawTurtle
import random

win = tk.Tk()
win.geometry("800x600")
win.resizable(width=False,height=False)
win.title("-----Turtle Race-----")
win['bg']='green'

canvas = tk.Canvas(win,width=750,height=455)
canvas.place(x=20,y=10)
title=tk.Label(canvas,text="Turtle Race",width=20,height=1,font=("Agency FB",40))
title.place(x=200,y=10)
chance=""

def start():

    #Player 1
    s1 = TurtleScreen(canvas)
    s1.bgcolor('white')
    player_one = RawTurtle(s1)

    player_one.color('red')
    player_one.shape('turtle')
    player_one.up()
    player_one.goto(-200,100)

    #Player 2 Clone of Player 1
    player_two = player_one.clone()
    player_two.color('black')
    player_two.up()
    player_two.goto(-200,-100)

    #setup victory line for both players
    player_one.goto(300,60)
    player_one.down()
    player_one.circle(40)
    player_one.up()
    player_one.goto(-200,100)

    player_two.goto(300,-140)
    player_two.down()
    player_two.circle(40)
    player_two.up()
    player_two.goto(-200,-100)

    die = [1,2,3,4,5,6]

    def play():
        for i in range(20):
            global chance
            if chance!='A':
                chance = 'A'
                if player_one.pos()>=(300,50):
                    print("Player One Wins!")
                    win.destroy()
                    msg.showwarning("Congratulations","Player One Win this game")

                    break
                else:
                    die_outcome=random.choice(die)
                    player_one.fd(20*die_outcome)
                    print("player_one position===>",player_one.pos())
            else:
                msg.showwarning("Alert","Its not your turn")
            break
        
    def play2():
            for i in range(20):
                global chance
                if chance!='B':
                    chance = 'B'
                    if player_two.pos()>=(300,-50):
                        print("Player Two Wins!")
                        win.destroy()
                        msg.showwarning("Congratulations","Player Two Win this game")

                        break
                    else:
                        die_outcome=random.choice(die)
                        player_two.fd(20*die_outcome)
                        print("player_two position===>",player_two.pos())
                else:
                    msg.showwarning("Alert","Its not your turn")
                break

    player1 = tk.Button(canvas,text='Player 1',bg='green',fg='white',
                        activeforeground='yellow',
                        font=('Agency FB',18),
                        relief='ridge',width=8,height=1,command=play)
    player1.place(x=230,y=420)

    player2 = tk.Button(canvas,text='Player 2',bg='green',fg='white',
                        activeforeground='yellow',
                        font=('Agency FB',18),
                        relief='ridge',width=8,height=1,command=play2)
    player2.place(x=500,y=420)

start_button = tk.Button(canvas,text='Start',bg='green',fg='white',
                         activeforeground='yellow',
                         font=('Agency FB',18),command=start,
                         relief='ridge',width=8,height=1)
start_button.place(x = 200,y = 20)

stop_button = tk.Button(canvas,text='Stop',bg='green',fg='white',
                         activeforeground='yellow',
                         font=('Agency FB',18),command=win.destroy,
                         relief='ridge',width=8,height=1)
stop_button.place(x = 500,y = 20)
win.mainloop()
