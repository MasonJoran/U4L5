from turtle import *

turtle = Turtle()
turtle.color('red')
turtle.pensize(4)
turtle.shape('turtle')
turtle.speed(0)


def drawHexagon():		
	for x in range(6):
		turtle.forward(100)
		turtle.left(60)

drawHexagon()

mainloop()