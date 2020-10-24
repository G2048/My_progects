import turtle

joi = turtle.Turtle()
joi.speed (1000)
joi.pensize(2)
joi.color('blue')

colors = ['red', 'green', 'blue', 'brown']

def sq(n):
	for i in range(4):
		joi.color(colors[i % 4])
		joi.forward(n)
		joi.left(90)

length = 5
for i in range(100):
    #sq(length)
    joi.circle(length)
    joi.right(10)
    length += 2

turtle.exitonclick()