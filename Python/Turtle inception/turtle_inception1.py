import turtle

turtle.speed(100)
turtle.pensize(3)
turtle.up() #"поднятие" черепахи
turtle.setposition(-30, -30) # смещение  черепахи по координатной сетке
turtle.down()

#n = int(input())
length = 100

def polygon(n, length):
	sumAngle = 180 * (n - 2)
	if sumAngle % n == 0:
		angle = sumAngle // n
		for i in range(n): # задаем кол-во углов
			turtle.forward(length)
			turtle.left(180 - angle)

for i in range (3,11):
	polygon(i, length)

turtle.exitonclick()