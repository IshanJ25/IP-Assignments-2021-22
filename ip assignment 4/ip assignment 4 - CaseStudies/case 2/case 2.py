import pandas as pd

pswd = '1234'
d = {}
dn = {}


def admin():
    print('\nDo you wish to delete questions or exit?')
    print('\n1 for deleting questions\n2 for exiting')

    action = input('\nYour input? ')

    if action == '1':
        delete()

    elif action == '2':
        menu()

    else:
        print('\nPlease choose between 1 and 2 only!')
        admin()


def delete():
    for j in dn:
        print('{} - {}'.format(j, dn[j][0]))
    print('Please select the question number')
    action = input('Your input? ')

    flg = []
    for j in list(dn.keys()):
        if action == j:
            del dn[j]
            flg.append('found')
            print('Found and deleted')
            print(dn)

    if not flg:
        print('Not found')

    action = input('\nPress <enter> for searching again and q/Q for exit: ')
    if action == '':
        delete()
    else:
        menu()


def menu():
    print('\nInput password to login as Admin\nPress Enter to take the Quiz\nInput q/Q to Exit')
    action = input('\nYour input? ')

    if action == pswd:
        print('\nLogged in as Admin')
        admin()

    elif action.lower() == 'q':
        print('\nHave a nice day!')
        exit()

    else:
        print('Welcome dear guest!')
        take()


def ini():
    global d, dn

    csvpath = 'csv.csv'
    df = pd.read_csv(csvpath)

    d = {
        'Ques': list(df.ques),
        'Ans': list(df.ans),
        'options': {
            'a': list(df.option1),
            'b': list(df.option2),
            'c': list(df.option3),
            'd': list(df.option4),
        },
    }

    dn = {}

    for i in range(1, len(list(df.ques)) + 1):
        dn[str(i)] = [
            d['Ques'][i - 1],
            d['Ans'][i - 1],
            d['options']['a'][i - 1],
            d['options']['b'][i - 1],
            d['options']['c'][i - 1],
            d['options']['d'][i - 1],
        ]

    print('\nWelcome to QUIZZLER!')
    menu()


def take():
    namee = input('Your name: ')
    print('You will be awarded ten (10) points for each correct answer')
    print('You will be awarded zero (0) points for each unattempted answer')
    print('You will lose your streak for each wrong or skipped answer')
    print('You will get bonus for longest streak at the end')
    print('{}, the quiz has started!\n'.format(namee))

    pts = 0
    streak = 0
    ls = 0
    correct = 0
    wrong = 0
    skipped = 0

    for i in dn:
        print(dn[i][0])
        print(dn[i][2])
        print(dn[i][3])
        print(dn[i][4])
        print(dn[i][5])
        inp = input('Your answer? (a/b/c/d) (e for skip): ').lower()
        if inp == dn[i][1]:
            print('Correct answer')
            pts += 10
            streak += 1
            correct += 1
            print('Current streak is {}\n'.format(streak))
            if streak > ls:
                ls = streak
        elif inp == 'e':
            print('Question skipped')
            print('Correct answer was', dn[i][1])
            pts += 0
            streak = 0
            skipped += 1
            print('Current streak is {}\n'.format(streak))
        else:
            print('Wrong answer!')
            print('Correct answer was', dn[i][1])
            pts += 0
            streak = 0
            wrong += 1
            print('Current streak is {}\n'.format(streak))

    bonus = streak*5
    points = pts + bonus
    print('\n{}, you have scored {} points'.format(namee, points))
    print('{} answers were correct'.format(correct))
    print('{} answers were wrong'.format(wrong))
    print('{} questions were skipped'.format(skipped))
    print('Longest streak was {} correct answers\n'.format(ls))

    menu()


ini()
