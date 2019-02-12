from turtle import *

turtle = Turtle()
turtle.color('red')
turtle.pensize(4)

turtle.speed(0)

#Starting point for the row

turtle.penup()
turtle.goto(-300, 200)
turtle.pendown()
#############################
xvalue = -300
yvalue = 200
Coordinates = (xvalue , yvalue)

#Starting point for the row

def drawStar():
	for x in range(5):
		turtle.forward(50)
		turtle.left(144)


def drawRow():
	for y in range(3):
		drawStar()
		turtle.penup()
		turtle.forward(300)
		turtle.pendown()
	
	turtle.penup()
	turtle.back(900)
	turtle.pendown()

for z in range(6):
	drawRow()
	yvalue = yvalue - 100
	Coordinates = (xvalue , yvalue)
	turtle.penup()
	turtle.goto(xvalue , yvalue)
	turtle.pendown()





mainloop()


