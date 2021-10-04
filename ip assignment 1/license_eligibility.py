# Dl banwado mera

while True:
    try:
        age = float(input('What is your age? '))
        break
    except ValueError:
        print('Please enter numbers only')
        continue

if age <= 0:
    print("That can't be your age!")
elif 16 <= age < 18:
    print('You are eligible to drive gearless 2-wheeler vehicles (eg. Scooty) after obtaining a DL')
elif age >= 18:
    print('You are eligible to drive any vehicle(s) after obtaining a DL')
elif 1<= age < 16:
    print('You are currently not eligible to apply for a DL')
else:
    print('Error')
