while True:
    try:
        num1 = float(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter numbers only!")
        continue

print('Available operations:')
print('1 Add')
print('2 Sub')
print('3 Mul')
print('4 Div')
print('5 Exp')


selection = {1, 2, 3, 4, 5}
opr = 6

while opr not in selection:
    try:
        opr = int(input('What operation do you choose? '))
        break
    except ValueError:
        print("Please select from 1, 2, 3, 4, 5 only!")
        continue


'''opr = int(input('What operation do you choose? '))

    print("Please select from 1, 2, 3, 4, 5 only!")
else:
    opr += 0'''

while True:
    try:
        num2 = float(input("Enter second number: "))
        break
    except ValueError:
        print("Please enter numbers only!")
        continue

while True:
    try:
        if opr == 1:
            ans = num1 + num2
        elif opr == 2:
            ans = num1 - num2
        elif opr == 3:
            ans = num1 * num2
        elif opr == 4:
            ans = num1 / num2
        elif opr == 5:
            ans = num1 ** num2
        else:
            ans = 'error'
        break
    except ValueError:
        print("Error")
        continue
    except ZeroDivisionError:
        print('Division by zero not possible')

print(ans)