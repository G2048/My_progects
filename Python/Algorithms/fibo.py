num = int(input())

def fibo (n):
	a1 = 1
	a2 = 0

	for i in range(0,n):
		print(a2, end = ' ')
		
		a2, a1 = a1, a1 + a2


fibo (num)


#def fibonacci(n):
#    if n in (1, 2):
#        return 1
#    return fibonacci(n - 1) + fibonacci(n - 2)
#print(fibonacci(10))