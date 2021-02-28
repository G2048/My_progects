
age = int(input())

if age % 100 == 0:
    if (age / 100) % 4 == 0:
        print('YES')
    else:
        print('NO')
elif age % 4 == 0:
    print('YES')
else:
    print('NO')
