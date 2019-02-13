from random import randint

input1 = input("Would you like to roll a dice? (y/n)")
state = True

while state:
    x = randint(1, 6)
    if input1.lower() == "y":
        state = True
        print("The number is: " + str(x))
        input1 = input("Would you like to roll again?")
    else:
        print("bye!")
        state = False
