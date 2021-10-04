p = float(input('Principle in ₹: '))
r = float(input('Interest rate per month in %: '))
t = float(input('Time in months: '))

ci = (p * ((1 + (r / 100)) ** t)) - p
amt = ci + p

print('Compound interest will be ₹', ci, ' and amount will be ₹', amt)
