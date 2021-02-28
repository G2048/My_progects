
class F:

	def swap (self, x, y):
		x = x ^ y
		y = x ^ y
		x = x ^ y
		return print (x,y)

	def even_or_odd (self, x, y):

		if (x & 1) == 0:
			print("x is even!")

		if (y & 1) == 0:
			print("y is even!")




a = input().split()

F().swap(int(a[0]), int(a[1]))

F().even_or_odd(int(a[0]), int(a[1]))

