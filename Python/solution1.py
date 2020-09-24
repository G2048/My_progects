import sys

digit_string = sys.argv[1]

i=0
p=0

while i < len(digit_string) :
    a=int(digit_string[i])
    p=a+p
    i+=1

print (p)
