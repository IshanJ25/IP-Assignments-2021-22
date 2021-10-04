def func():
    age = 0
    while True:
        try:
            age = int(input('What is your age? '))
            break
        except:
            print('Please enter integral value for age!\n')
            continue

    if age <= 0 or age > 120:
        print("That can't be your age! Please try again\n")
        func()
    elif 16 <= age < 18:
        print('You are eligible to drive gearless 2-wheelers after obtaining a DL')
    elif 18 <= age <= 100:
        print('You are eligible to drive any vehicle after obtaining a DL')
    elif 1 <= age < 16:
        print('You are currently not eligible to apply for a DL')
    else:
        print('Error')
        func()


func()
