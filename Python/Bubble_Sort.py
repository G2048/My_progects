
def RandomArray(n):
	import random
	Array = []
	i = 0
	while i <= n:
		number = random.randint(0,200)
		Array.append(number)
		#print(Array[i])	
		i+=1
	return Array


def SortedArray(n):
	A = n
	for i in range(len(A)-1):
		for z in range(len(A)-i-1):
			print(A)			
			if A[z] > A[z+1]:
				A[z], A[z+1] = A[z+1], A[z]

import random
#n = input('Input the number:')
n = random.randint(2,20)
SortedArray(RandomArray(n))
