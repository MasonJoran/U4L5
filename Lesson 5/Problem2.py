from turtle import *

turtle = Turtle()
turtle.color('red')
turtle.pensize(4)
turtle.shape('turtle')
turtle.speed(0)


def drawTriangle():
	for x in range(3):
		turtle.forward(100)
		turtle.right(120)


for y in range(12):
	drawTriangle()
	turtle.left(30)

mainloop()