import turtle

# Creating a turtle object
pen = turtle.Turtle()

#Defining a metod to draw curve
def curve():
	for i in range(200):
		#Defining step by step curve motion
		pen.right(1)
		pen.forward(1)

#Defining metod to draw a full heart
def heart():
	pen.fillcolor('red')
	#Start filling the color
	pen.begin_fill()
	#Draw the left line
	pen.left(140)
	pen.forward(113)
	#Draw the left curve
	curve()
	pen.left(120)
	#Draw the right curve
	curve()
	pen.forward(112)
	#Ending the fillin of the color
	pen.end_fill()

#Defining method to write text
def txt():
	#Move turtle to air
	pen.up()
	#Move the turtle to a given position
	pen.setpos(-45,95)
	#Move the turtle to the ground
	pen.down()
	#Set the text color to lightgreen
	pen.color('lightgreen')
	#Write the specified text in specified font style and size
	pen.write("I Love You", font=('Verdana', 12, 'bold'))

#Draw a heart
heart()
#Write text
txt()
#To hide turtle	
pen.ht()
input()
