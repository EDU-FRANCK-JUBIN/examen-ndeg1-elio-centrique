# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 09:23:08 2019

@author: delan
"""

import turtle as tu
import random


# Initialisation du jeu
ts = tu.getscreen()
ts.clear()
ts.bgpic("champcourse2.gif")

ts.title("Bienvenue Ã  la course des tortues !")
ts.setup (width=1400, height=800, startx=0, starty=0)
    
# DÃ©clarez les 5 tortues et positionnez-les sur leurs hexagones respectifs
Michelangelo = tu.Turtle()
Michelangelo.color("orange")
Michelangelo.up()
Michelangelo.shape("turtle")
Michelangelo.goto(-650, 320)
Michelangelo.down()
#make_hexagone(Michelangelo, 0)

Leonardo = tu.Turtle()
Leonardo.color("deep sky blue")
Leonardo.shape("turtle")
Leonardo.up()
Leonardo.goto(-650, 165)
Leonardo.down()
#make_hexagone(Leonardo, 1)

Raphael = tu.Turtle()
Raphael.color("red")
Raphael.up()
Raphael.shape("turtle")
Raphael.goto(-650, 0)
Raphael.down()
#make_hexagone(Raphael, 2)

Donatello = tu.Turtle()
Donatello.color("purple")
Donatello.up()
Donatello.shape("turtle")
Donatello.goto(-650, -145)
Donatello.down()
#make_hexagone(Donatello, 3)

Splinter = tu.Turtle()
Splinter.color("dark slate grey")
Splinter.up()
Splinter.shape("turtle")
Splinter.goto(-650, -300)
Splinter.down()
#make_hexagone(Splinter, 4)

pos = []
print("Faites vos paris !")
for i in range (0,5):
    pos.append(input("tortue N°" + str(i+1) + ": "))

while(Michelangelo.xcor() < 480 or Leonardo.xcor() < 480 or Raphael.xcor() < 480 
      or Donatello.xcor() < 480 or Splinter.xcor() < 480):
    chosen_turtle = random.choice([Michelangelo, Leonardo, Raphael, Donatello, Splinter])
    forward = random.randint(1,5)
    chosen_turtle.forward(forward)
    

turtle_arbitre = tu.Turtle()
turtle_arbitre.goto(-150,0)
turtle_arbitre.color("Black")
turtle_arbitre.write("Le joueur 1 a gagné... peut-être... j'ai pas encore implémenté ça", move=True, align="left", font=("Arial", 16, "normal"))
tu.done()

