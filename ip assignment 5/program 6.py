# Write a program that keeps name and birthday in a dictionary as key-value pairs. The program should display a menu
# that lets the user:
# search, add new, edit, delete, reset & display
# an existing record data.

months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

d_main = {}

n_d = {
    'Ishan J.': '2502',
    'Socrates': '0406',
    'Steve J.': '2402',
    'Henry F.': '3006',
    'Albert E.': '1403',
    'Gill A.': '0103',
    'Ed Roberts': '1309',
    'Mark Z.': '1405',
    'Bill G.': '2810',
    'Alex G.B.': '0303'
}

for keyitem in list(n_d.keys()):
    d_main[keyitem] = n_d[keyitem]


def ini():
    print('\n\nWelcome to birthday directory.')
    print('Here you can access birthdays.')
    menu()


def menu():
    global d_main

    print('\nApplication Menu:\n')

    print()
    print('Enter 1 for Search by name')
    print('Enter 2 for Changing a record')
    print('Enter 3 for Deleting a record')
    print('Enter 4 for Adding a record')
    print('Enter 5 for Reset Data')
    print('Enter 6 for Display Data')
    print('Enter 7 for Exiting')

    inp = input('\nYour input? ')

    for i in inp:
        if i not in digits:
            print('Please enter positive integral values only!')
            menu()

    action = int(inp)

    if action not in [1, 2, 3, 4, 5, 6, 7]:
        print('\nError! Please enter number within the range.')
        menu()
    elif action == 1:
        search()
    elif action == 2:
        change()
    elif action == 3:
        delete()
    elif action == 4:
        add_elem()
    elif action == 5:
        reset()
    elif action == 6:
        disp()
    elif action == 7:
        print('\nHave a nice day!')
        quit()
    else:
        print('\nError! Please enter number within the range.')
        menu()


def search():
    s = input('\nSearch the name here (min. 1 character): ')
    s = s.lower()
    if len(s) == 0:
        print('\nPlease try again! (min. 1 character)')
        search()
    else:
        flg = []
        for j in list(d_main.keys()):
            if s in j.lower():
                date = str(int(d_main[j][:2])) + ' ' + months[int(d_main[j][-2:])]
                print('{} - {}'.format(j, date))
                flg.append(j)

        if not flg:
            print('\nNot found!')

    action = input('\nSearch again? (y/n): ').lower()

    if action == 'y':
        search()
    else:
        menu()


def change():

    print('Change a record:')
    print('Enter 1 to change a date')
    print('Enter 2 to change a name')

    namedate = input('\nYour input? ')
    if namedate not in ['1', '2']:
        print('Please select between 1 and 2!')
        menu()

    action = int(namedate)

    if action == 1:
        changedate()
    elif action == 2:
        changename()
    else:
        menu()


def changedate():
    count = 1
    print('\nSelect the date you want to edit:')
    print('(Please enter the number 1/2/3/4...)\n')
    for i in d_main.keys():
        cdate = str(int(d_main[i][:2])) + ' ' + months[int(d_main[i][-2:])]
        print('{} - {} - {}'.format(count, i, cdate))
        count += 1
    inp = input('\nYour input? ')

    for i in inp:
        if i not in digits:
            print('Please enter positive integral values only!')
            changedate()

    action = int(inp)

    if action > len(list(d_main.keys())) or action == 0:
        print('Out of range! Please try again\n')
        changedate()
    else:
        cd = d_main[list(d_main.keys())[action - 1]]
        dd = str(int(cd[:2])) + ' ' + months[int(cd[-2:])]
        print('\nCurrent date is {}'.format(dd))
        inp = input('Please enter new date in DDMM format: ')

        for i in inp:
            if i not in digits:
                print('Please enter in valid DDMM format')
                changedate()

        ddmm = inp

        if len(ddmm) != 4 or not 1 <= int(ddmm[:2]) <= 31 or not 1 <= int(ddmm[-2:]) <= 12:
            print('Invalid date! please try again.\n')
            changedate()
        else:
            newdate = str(int(ddmm[:2])) + ' ' + months[int(ddmm[-2:])]
            print('\nThe new date is {}'.format(newdate))
            d_main[list(d_main.keys())[action - 1]] = ddmm
            menu()


def changename():
    count = 1
    print('\nSelect the name you want to edit:')
    print('(Please enter the number 1/2/3/4...)\n')
    for i in d_main.keys():
        cdate = str(int(d_main[i][:2])) + ' ' + months[int(d_main[i][-2:])]
        print('{} - {} - {}'.format(count, i, cdate))
        count += 1
    inp = input('\nYour input? ')

    for i in inp:
        if i not in digits:
            print('Please enter positive integral values only!')
            changename()

    action = int(inp)

    if action > len(list(d_main.keys())) or action == 0:
        print('Out of range! Please try again\n')
        changename()
    else:
        cd = list(d_main.keys())[action - 1]
        print('\nCurrent name is {}'.format(cd))
        new_n = input('Please enter new name: ')

        if new_n in ['\n', '', ' ', '.', ',', ':', '?']:
            print('Invalid name! please try again.\n')
            changename()
        else:
            d_main[new_n] = d_main[cd]
            del d_main[cd]
            print('"{}" is replaced by "{}"'.format(cd, new_n))
            menu()


def delete():
    count = 1
    print('\nSelect the data you want to delete:')
    print('(Please enter the number)\n')
    for i in d_main.keys():
        print('{} - {}'.format(count, i))
        count += 1

    inp = input('\nYour input? ')

    for i in inp:
        if i not in digits:
            print('Please enter positive integral values only!')
            menu()

    action = int(inp)

    if action > len(list(d_main.keys())) or action == 0:
        print('Out of range! Please try again\n')
        change()
    else:
        del d_main[(list(d_main.keys())[action - 1])]
        menu()


def add_elem():
    addobj = input('\nName to be added: ')

    if addobj in d_main:
        print('\nAlready in record!')
        action = input('Return to menu? (y/n)\n').lower()
        if action == 'y':
            menu()
        else:
            print('\nPlease try again')
            add_elem()
    else:
        inp = input('\nBirthday in DDMM format: ')

        for i in inp:
            if i not in digits:
                print('Please enter positive integral values only!')
                menu()

        obj_date = inp

        if len(obj_date) != 4 or not 1 <= int(obj_date[:2]) <= 31 or not 1 <= int(obj_date[-2:]) <= 12:
            print('Invalid date! please try again.')
            add_elem()
        else:
            newdate = str(int(obj_date[:2])) + ' ' + months[int(obj_date[-2:])]
            d_main[addobj] = obj_date
            print('Added:\n{} - {}'.format(addobj, newdate))
            action = input('\nAdd another name? (y/n): ').lower()

            if action == 'y':
                add_elem()
            else:
                menu()


def reset():
    d_main.clear()
    for i in list(n_d.keys()):
        d_main[i] = n_d[i]

    print('\nSuccessfully reset the data!')
    menu()


def disp():
    print('\nBirthdays in record:')
    for i in d_main:
        idate = str(int(d_main[i][:2])) + ' ' + months[int(d_main[i][-2:])]
        print('{} - {}'.format(i, idate))
    menu()


ini()
