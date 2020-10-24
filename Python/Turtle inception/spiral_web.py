import turtle

t = turtle.Turtle()
t.speed(1000)
colors =['red', 'yellow', 'green', 'purple', 'blue', 'orange']


turtle.bgcolor('black')

for x in range(350):
	t.pencolor(colors[x%6])
	t.width(x/100 + 1)
	t.forward(x)
	t.left(59)
turtle.exitonclick()