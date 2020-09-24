v = int(input())
t = int(input())
s = int(v * t)

if s < 0:
    print('0')
if s > 108:
    print(108)
else:
    print(s)
