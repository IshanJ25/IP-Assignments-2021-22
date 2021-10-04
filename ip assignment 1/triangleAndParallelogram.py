# Python program to calculate area of triangle and ||gm
import math

# flg1 = "0"
flg2 = -1

flg1 = input("Is your shape a Triangle (y/n)? ")
if flg1.lower() == "y":
    flg2 = 0
elif flg1.lower() == "n":
    flg1 = input("Is your shape a Parallelogram (y/n)? ")
    if flg1.lower() == "y":
        flg2 = 1
    elif flg1.lower() == "n":
        print("ERR-001: Sorry! Only 2 shapes available.")
        flg2 = 2
    else:
        print("ERR-002: Invalid input!")
        flg2 = 2
else:
    print("ERR-002: Invalid input!")
    flg2 = 2

if flg2 == 0:
    a = int(input("1st side in cm: "))
    b = int(input("2nd side in cm: "))
    c = int(input("3rd side in cm: "))
    s = (a+b+c)/2
    ar = math.sqrt(s*(s-a)*(s-b)*(s-c))
    p = a+b+c
    print("ar = ", ar, "; p =", p)
elif flg2 == 1:
    b = float(input("Base   of ||gm in cm: "))
    h = float(input("Height of ||gm in cm: "))
    s = float(input("Side   of ||gm in cm: "))
    ar = (b*h)
    p = 2*(b+s)
    print("ar = ", ar, "; p =", p)
else:
    print("ERR-003: Please try again or with different data!")
