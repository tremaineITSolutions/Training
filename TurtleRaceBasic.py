# import libraries to create game
from random import *
from turtle import *

penup()

"""
basically makes sure that the moving object that you've created does not draw anything on the window.
So if you have a ball and you want it to move around and draw anything on the window, then you use the penup ().

"""
winner = ""

goto(-210,140) #positioning the pen
write("START", font=('Arial',14))
goto(-140,140) #positioning the pen


for sp in range(30): #loop for creating the lines labelled with number
   
 speed(25)          #setting the speed
 write(sp)          #writing the int
 right(90)          #setting right at 90 degrees
 forward(10)        #forward at 10 units
 pendown()          #ready to draw
 forward(150)       #forward at 150 units
 penup()            #not ready to draw
 backward(160)      #back at 160 units
 left(90)           #left set at 90 degrees
 forward(20)        #forward at 20 units

'''
This is a IF Statement
A IF Statement checks if something is true
If the statement is true, it will do whatever is after the if statement
== means equal
and the code underneath the If statement must be indented
'''
if sp==29: #only if line is 29
    write("FINISH", font=('Arial',14))



RedTurtle = Turtle() #inheriting the turtle
RedTurtle.color("red") #setting the color to red for the first turtle
RedTurtle.shape('turtle') #setting the shape to "turtle"
RedTurtle.penup() #not ready to draw
RedTurtle.goto(-160,100) #positioning the turtle
RedTurtle.pendown() #ready todraw


BlueTurtle = Turtle() #inheriting another turtle
BlueTurtle.color('blue') #setting the color of the turtle to blue
BlueTurtle.shape('turtle') #declaring the shape of the turtle to "turtle"
BlueTurtle.penup() #not ready to draw
BlueTurtle.goto(-160,60) #positioning
BlueTurtle.pendown() #ready to draw

GreenTurtle = Turtle() #inheriting the last turtle
GreenTurtle.color('green') #setting the color of the turtle as "green"
GreenTurtle.shape('turtle') #declaring the shape of the turtle
GreenTurtle.penup() #not ready to draw
GreenTurtle.goto(-160,20) #positioning
GreenTurtle.pendown() #ready


for turn in range(100): #loop for the race

  rannum1 = randint(1,10)
  rannum2 = randint(1,10)
  rannum3 = randint(1,10)


  RedTurtle.forward(rannum1) #setting the speed randomly with the "random" module
  BlueTurtle.forward(rannum2) #setting the speed randomly with the "random" module
  GreenTurtle.forward(rannum3) #setting the speed randomly with the "random" module

# this creates a variable called redPos
# and sets redPos to the current position of the red turle on the screen
redPos = RedTurtle.pos()[0]
bluePos = BlueTurtle.pos()[0]
greenPos = GreenTurtle.pos()[0]


if ((redPos > bluePos) and (redPos > greenPos)):
    winner = "Red"
elif ((bluePos > redPos) and (bluePos > greenPos)):
    winner = "Blue"
else:
    winner = "Green"


goto(-190,-80) #positioning the pen
print("red ", redPos)
print("blue ", bluePos)
print("green ", greenPos)

write("And the winner is: " + winner, font=('Arial',14))



