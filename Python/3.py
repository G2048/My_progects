import random

Array_1 = []
i = 0
n = 10000 # Размер массива

while i < n:
	m = random.randint(0, 10)
	Array_1.append(m)
	i +=1

print(Array_1)