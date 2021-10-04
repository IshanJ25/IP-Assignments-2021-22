# kya aap vote kar sakte hai?

while True:
    try:
        age = float(input('What is your age? '))
        break
    except ValueError:
        print('Please enter numbers only')
        continue

if age <= 0:
    print("That can't be your age!")
elif age >= 18:
    print('You are eligible to vote in India.')
elif 1 <= age < 18:
    print('You are currently not eligible to vote in India.')
else:
    print('Error')
