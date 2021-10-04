# marksheet

print('Please enter marks out of 100:')
e = float(input('English Marks: '))
h = float(input('Hindi   Marks: '))
m = float(input('Maths   Marks: '))
s = float(input('Science Marks: '))
z = float(input('SSc     Marks: '))

avg = (e+h+m+s+z)/5

if avg/100 > 1:
    print('Wrong entry(ies)! Please try again')
else:
    print('You have scored', avg, 'marks out of 100 according to given entries')

