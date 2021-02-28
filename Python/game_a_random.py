import random

number = random.randint (1, 100)

while True:
    answer = int(input('Enter the number:', ))
    print(answer)
    print(type(answer))

    if answer == "exit":
        break

    if type(answer) == str(answer):
        print("Enter enother number")
        continue

    if answer < number :
        print("The entered number is less")
    elif answer > number :
        print("The entered number is more")
    else:
        print("You guessed!")
        break
