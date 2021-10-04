n = int(input("Enter a number: "))

facto = 1

if n < 0:
    print("Sorry negative numbers, no factorial for you!")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, n + 1):
        facto *= i
    print("Factorial of", n, "is", facto)
