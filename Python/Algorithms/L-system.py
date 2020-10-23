import turtle

turtle.shape('turtle') # painter
turtle.shapesize(2,2,2) # size of painter
turtle.pensize(3) # size of lines
turtle.speed(5) 
n = 20

for i in range(50):
	turtle.forward(n)
	turtle.right(80)
	n += 10

turtle.mainloop()	# does not close the window