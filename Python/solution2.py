import sys

digit_string = sys.argv[1]

a=int(digit_string)
p='#'
s= " "

i=1
while i <= a:
    f=s*(a-i)
    d=p*i
    i+=1
    print (f+d)
input ()
