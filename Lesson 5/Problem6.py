from turtle import *

turtle = Turtle()
turtle.color('red')
turtle.pensize(4)
turtle.shape('turtle')
turtle.speed(0)


def drawStar():
	for x in range(5):
		turtle.forward(50)
		turtle.left(144)

for y in range(3):
	drawStar()
	turtle.penup()
	turtle.forward(100)
	turtle.pendown()
	




mainloop()