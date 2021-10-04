# simple interest = p*r*t/100

p = float(input('Principle in ₹: '))
r = float(input('Interest rate per month in %: '))
t = float(input('Time in months: '))

si = (p*r*t)/100
amt = p+si

print('Simple interest will be ₹',si, ' and amount will be ₹',amt)
