#------------------GUI Creation of tkinter--------------------------
import tkinter as tk
from PIL import Image,ImageTk

screen = tk.Tk()
screen.title("----My Games----")
screen.geometry("1000x600")
screen.resizable(width = False,height = False)
screen["bg"] = "#070436"

#-----------Fit Image in background------------
path = "D:\\CHIRAG FOLDER\\Main_Gui_bg.gif"
image1 = tk.PhotoImage(file = path)
w = 1000
h = 600
screen.geometry("%dx%d+0+0"%(w,h))
lx = tk.Label(screen,image = image1)
lx.pack(side = "top",fill = "both",expand = "yes")
    
#----------------Games bar-----------------
l1 = tk.Label(screen,text = "Turtle Based Games",font = ("Agency FB",28),
              bd = 4,bg = "#060245",fg = "cyan")
l1.place(x = 350,y = 5)

from Game_Area import *
button1 = tk.Button(screen,text = "Cannon",bg = "#070436",fg = "cyan",
                    activeforeground = "yellow",font = ("Agency FB",18),
                    relief = "groove",width = 8,height = 1,command = canon,bd = 4)
button1.place(x = 100,y = 80)

button2 = tk.Button(screen,text = "Bird",bg = "#070436",fg = "cyan",
                    activeforeground = "yellow",font = ("Agency FB",18),
                    relief = "groove",width = 8,height = 1,command = Bird,bd = 4)
button2.place(x = 450,y = 80)

button3 = tk.Button(screen,text = "FootBall",bg = "#070436",fg = "cyan",
                    activeforeground = "yellow",font = ("Agency FB",18),
                    relief = "groove",width = 8,height = 1,command = FootBall,bd = 4)
button3.place(x = 800,y = 80)

button4 = tk.Button(screen,text = "IronMan",bg = "#070436",fg = "cyan",
                    activeforeground = "yellow",font = ("Agency FB",18),
                    relief = "groove",width = 8,height = 1,command = Iron,bd = 4)
button4.place(x = 100,y = 230)

button5 = tk.Button(screen,text = "Snake",bg = "#070436",fg = "cyan",
                    activeforeground = "yellow",font = ("Agency FB",18),
                    relief = "groove",width = 8,height = 1,command = Snake,bd = 4)
button5.place(x = 450,y = 230)

button6 = tk.Button(screen,text = "Alien",bg = "#070436",fg = "cyan",
                    activeforeground = "yellow",font = ("Agency FB",18),
                    relief = "groove",width = 8,height = 1,command = Alien,bd = 4)
button6.place(x = 800,y = 230)

button7 = tk.Button(screen,text = "Race",bg = "#070436",fg = "cyan",
                    activeforeground = "yellow",font = ("Agency FB",18),
                    relief = "groove",width = 8,height = 1,command = Race,bd = 4)
button7.place(x = 100,y = 380)

button8 = tk.Button(screen,text = "TicTacToe",bg = "#070436",fg = "cyan",
                    activeforeground = "yellow",font = ("Agency FB",18),
                    relief = "groove",width = 8,height = 1,command = TicTacToe,bd = 4)
button8.place(x = 450,y = 380)

button9 = tk.Button(screen,text = "RPS",bg = "#070436",fg = "cyan",
                    activeforeground = "yellow",font = ("Agency FB",18),
                    relief = "groove",width = 8,height = 1,command = RPS,bd = 4)
button9.place(x = 800,y = 380)

button10 = tk.Button(screen,text = "Ball",bg = "#070436",fg = "cyan",
                    activeforeground = "yellow",font = ("Agency FB",18),
                    relief = "groove",width = 8,height = 1,command = Ball,bd = 4)
button10.place(x = 450,y = 530)

screen.mainloop()
