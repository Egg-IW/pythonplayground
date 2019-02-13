nterms = int(input("How many numbers of a fibonacci sequence do you want?"))

n1 = 0
n2 = 1
count = 0

if nterms <= 0:
    print("Please enter a positive value!")
    nterms = input("How many numbers of a fibonnaci sequence do you want?")

elif nterms == 1:
    print("Fibonacci sequence up to: " + str(nterms))
    print(n1)

else:
    print("Fibonacci sequence upto", nterms, ":")
    while count < nterms:
        print(n1, end=' , ')
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
