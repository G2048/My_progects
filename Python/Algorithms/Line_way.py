import RandomArray
import random

n = random.randint(2,20)
Array_1 = RandomArray.RandomArray(n)


def Line_way(Array, j):
	#print('\n'.join(str(Array)))
	for i in range(len(Array)):
		if Array[j] < Array[i]:
			Array [i], Array[j] = Array[j], Array [i]

	print(Array)
		
for k in range(len(Array_1)):
	Line_way(Array_1, k)