import turtle

#turtle.mainloop()
turtle.hideturtle() # to hide the painter
#turtle.tracer(0)
turtle.up()
turtle.setposition(0, 30)
turtle.down()
turtle.pensize(2)
turtle.speed(1000)

axiom = 'F+F+F+F'
tempAx = ''

for k in range(3):
	ln = len(axiom)
	for i in range(ln):
		if axiom[i] == '+':
			turtle.right(90)
			tempAx += '+'
		elif axiom[i] == '-':
			turtle.left(90)
			tempAx += '-'
		else:
			turtle.forward(11)
			tempAx += 'F+F-F-F+F'
	axiom = tempAx
	tempAx = ''

#turtle.update()
turtle.done()
print(axiom)