def RandomArray(n):
	import random

	Array = []
	i = 0
	
	while i <= n:
		number = random.randint(0,50)
		Array.append(number)
		#print(Array[i])	
		i+=1
	return Array
