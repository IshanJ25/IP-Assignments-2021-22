num = int(input("Enter a number: "))

prime = True

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            prime = False
            break

if prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
