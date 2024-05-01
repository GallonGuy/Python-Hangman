# Project 6 - Building the GUI for the Connections Game
# Andrew Russ
# CS 111, Spring 2024, Hayes and Reckinger
# The user interface for a game that has 16 words that belong to four categories with four words in each category

import turtle as t
import math
import random

def drawbox(location, size, color, turtle, text):
    # Moving to starting location
    t.penup()
    t.goto(location)

    # Preparing turtle
    t.fillcolor(color)
    t.pencolor(color)
    t.pendown() # Begins at bottom left and looks right
    t.begin_fill()
    t.left(90) # Rotate to LHS

    # Drawing the box with rounded edges
    t.forward(40)
    t.right(90)
    t.forward(25)
    t.right(45)
    t.forward(5)
    t.left(135)
    t.forward(30)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(70)
    t.right(90)
    t.forward(35)
    t.left(15)
    t.forward(35)
    t.right(75)
    t.forward(20)
        
    # Clearing formatting
    t.end_fill()
    t.penup()

    # Setting the text up in the center of the box
    text_pos = ((location[0] - size/2) - 0,(location[1] + size/2) - 0)
    t.goto(text_pos)

    # Writing the text in the box
    t.pencolor("black")
    t.write(text, align = "center", font = ("Arial", 12, "normal"))
    t.hideturtle()

# Press the green button in the gutter to run the script.

    # Here is a screen object to use
s = t.getscreen()

    # Here is a turtle object to use to draw the box
    # You should create the turtle object outside of your function (like this)
    # and send the box turtle in as an argument
box = t.Turtle()
box.hideturtle()
box.penup()
    
drawbox((-340,310),100,"red",box,"Stoichiometry")

t.mainloop() # DO NOT TOUCH
