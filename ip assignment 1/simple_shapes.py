pi = 3.14159265359

print('Select a shape:')
print('1 Circle')
print('2 Rectangle')


while True:
    try:
        shape = int(input('What shape do you select (1/2)? '))
        break
    except ValueError or shape != 1 or shape != 2:
        print('Please enter a valid value!')
        continue

if shape == 1:
    r = float(input('Radius of circle (cm): '))
    ar = pi * r * r
    pm = 2 * pi * r
    print('area =', ar, 'perimeter =', pm)
elif shape == 2:
    b = float(input('Enter 1st side (cm): '))
    h = float(input('Enter 2nd side (cm): '))
    ar = b * h
    pm = 2 * (b + h)
    print('area =', ar, 'perimeter =', pm)
else:
    print('Please try again and select from 1 and 2')
