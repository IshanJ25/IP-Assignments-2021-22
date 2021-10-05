# online banking program

def deposit():
    print('\nHow much amount would you like to deposit?')
    amt = int(input('  ₹'))
    f = open('case 1.txt', 'r')
    a = int(f.read())

    a = str(a + amt)
    f = open('case 1.txt', 'w')
    f.write(a)
    f = open('case 1.txt', 'r')
    a = f.read()

    print('\nYour current balance is ₹{}'.format(a))
    action = input('Do you want to exit? (y/n)').lower()

    if action == 'y':
        print('\nHave a nice day!')
        quit()
    else:
        accessAcc()


def withdraw():
    print('\nHow much amount would you like to withdraw?')
    amt = int(input('  ₹'))
    f = open('case 1.txt', 'r')
    a = int(f.read())
    if amt > a:
        print("You don't have enuff mony!")
        withdraw()
    else:
        new = str(a-amt)
        f = open('case 1.txt', 'w')
        f.write(new)
        f = open('case 1.txt', 'r')
        a = f.read()

        print('\nYour current balance is ₹{}'.format(a))
        action = input('Do you want to exit? (y/n)').lower()

        if action == 'y':
            print('\nHave a nice day!')
            quit()
        else:
            accessAcc()


def deets():
    print('\nWelcome to details page. Here you will find the details about interest on your money.')
    t = int(input('Tenure of account (in years): '))
    f = open('case 1.txt', 'r')
    a = int(f.read())
    r = 5  # 5% per year

    amt = str(int(a+(a*r*t/100)))

    print('\nOur bank offers interest rate of {}% (simple interest) per year.'.format(r))
    print('In {} years, your money will increase to ₹{}'.format(t, amt))

    action = input('Do you want to exit? (y/n)').lower()

    if action == 'y':
        print('\nHave a nice day!')
        quit()
    else:
        accessAcc()


def createAcc():
    f = open('case 1.txt', 'w')
    f.write('1000')
    f = open('case 1.txt', 'r')
    a = f.read()
    print('\nDone! You now have an account with PyBank,\nAnd we have granted ₹1000 to you as a complementary gift!')
    print('Your current balance is ₹{}'.format(a))
    print('\nWould you like to access your account or exit?')
    print('Enter 1 for Accessing account')
    print('Enter 2 for Exiting')

    action = int(input('Your input? '))
    if action == 1:
        accessAcc()
    elif action == 2:
        print('\nHave a nice day!')
        quit()


def accessAcc():
    f = open('case 1.txt', 'r')
    a = f.read()
    if a == '':
        makeone = input("\nNo account available, would you like to make one? (y/n)").lower()
        if makeone == 'y':
            createAcc()
        elif makeone == 'n':
            print('\nProgram has been restarted')
            ini()
        else:
            print('\nPlease enter a valid answer!')
            accessAcc()
    else:
        print('\nYour current balance is ₹{}'.format(a))
        print('\nDo you want to withdraw, deposit or exit?')
        print('Enter 1 for Withdraw')
        print('Enter 2 for Deposit')
        print('Enter 3 for Account details')
        print('Enter 4 for Exiting')
        print('Enter 5 for Deleting account')
        action = int(input('\nYour input? '))

        if action == 1:
            withdraw()
        elif action == 2:
            deposit()
        elif action == 3:
            deets()
        elif action == 4:
            print('\nHave a nice day!')
            quit()
        elif action == 5:
            print('\nThe account has been deleted and a new account will be made.')
            createAcc()
        else:
            print('\nError! Please try again')
            accessAcc()


def ini():

    f = open('case 1.txt', 'a+')
    f.write('')

    print('\nWelcome to PyBank! Do you want to access your account or make a new account?')
    print('Enter 1 for Accessing account')
    print('Enter 2 for Creating new account')
    print('(CREATING NEW ACCOUNT WILL DELETE PREVIOUS ACCOUNT!!!)')

    initialize = int(input('\nYour input? '))

    if initialize == 1:
        accessAcc()
    elif initialize == 2:
        createAcc()
    else:
        print('Error! Please try again')
        ini()


ini()
