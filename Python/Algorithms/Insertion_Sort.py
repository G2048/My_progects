import RandomArray
import RandomArray
import random

n = random.randint(2,20)
Array_1 = RandomArray.RandomArray(n)

def Insertion_Sort (array):
	for i in range(len(array)):
		print(array)
		for j in range(i+1):
			if array[i] < array[j]:
				array[i], array[j] = array[j], array[i]
	print(array)

Insertion_Sort(Array_1)