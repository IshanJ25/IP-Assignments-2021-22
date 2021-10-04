import math

print('ax² + bx + c = 0;  x²≠0')
a = float(input("coefficient of x²: "))
b = float(input("coefficient of x : "))
c = float(input("Constant term    : "))

d = ((b**2)-(4*a*c))

if a == 0:
    print("x² cannot be zero!")
else:
    if d < 0:
        print("no real roots")
    elif d == 0:
        x = (-b + math.sqrt(d)) / (2 * a)
        print("2 equal roots: ", x)
    elif d>0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print("2 roots are: ", x1, "and", x2)
    else:
        print("ERROR: Please try again!")