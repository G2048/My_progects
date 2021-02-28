import RandomArray
import random

def SortedArray(n):
	A = n
	for i in range(len(A)-1):
		for z in range(len(A)-i-1):
			print(A)
			if A[z] > A[z+1]:
				A[z], A[z+1] = A[z+1], A[z]

#n = input('Input the number:')
#Ar = [5,6,7,9,0,1]

n = random.randint(2,20)

SortedArray(RandomArray.RandomArray(n))
