import sys
dev=sys.argv[1]
dev1=sys.argv[2]
dev2=sys.argv[3]

a = int(dev)
b = int(dev1)
c = int(dev2)

D = b ** 2 - 4 * a * c

if D < 0:
  print("Корней нет")
elif D == 0:
  x = -b / 2 * a
  print (x)
else:
  x1=int(((-b) + (D)**(1/2))/(2*a))
  x2=int(((-b) - (D)**(1/2))/(2*a))
  print(x1)
  print(x2)
