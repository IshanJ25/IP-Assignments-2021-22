# smallest and largest number among 3 inputs


while True:
    try:
        a = float(input('1st number: '))
        break
    except ValueError:
        print('Please enter numbers only')
        continue

while True:
    try:
        b = float(input('2nd number: '))
        break
    except ValueError:
        print('Please enter numbers only')
        continue

while True:
    try:
        c = float(input('3rd number: '))
        break
    except ValueError:
        print('Please enter numbers only')
        continue

if a < b and a < c:
    print(a, 'is smallest')
elif b < a and b < c:
    print(b, 'is smallest')
elif c < a and c < b:
    print(c, 'is smallest')
else:
    print('2 or 3 numbers are equal')

if a > b and a > c:
    print(a, 'is largest')
elif b > a and b > c:
    print(b, 'is largest')
elif c > a and c > b:
    print(c, 'is largest')
else:
    print('')
