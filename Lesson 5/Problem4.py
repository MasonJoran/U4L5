from turtle import *

turtle = Turtle()
turtle.color('red')
turtle.pensize(4)
turtle.shape('turtle')
turtle.speed(0)


def drawHexagon(side):		
	for x in range(6):
		turtle.forward(side)
		turtle.left(60)

for y in range(25, 225, 25):
	drawHexagon(y)



mainloop()