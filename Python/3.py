
Array_1 = [5,3,4,7,2,8,6,9,1]

for i in range(len(Array_1)):
	print(Array_1)
	for j in range(i+1):
		if Array_1[i] < Array_1[j]:
			Array_1[i], Array_1[j] = Array_1[j], Array_1[i]

print(Array_1)