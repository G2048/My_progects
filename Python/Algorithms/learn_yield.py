
Array_q = [3,5,8,1,2,9,4,7,6]
Array_w = []

def Merge_sort (ar):
	count = 0
	s = len(ar)
	#print(s)

	for i in range(s):
		print('count = {}'.format(count))
		count = 1 + count
		if count > 7:
			break
		yield i


it = Merge_sort(Array_q)

print('{}{}{}{}'.format(next(it),next(it),next(it),next(it)))
print(type(it))
#for b in Merge_sort(Array_q):
#	print(b)