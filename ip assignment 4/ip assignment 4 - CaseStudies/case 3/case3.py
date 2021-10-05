# Write a Python program to:
# Create an admin ID to add, modify or delete data in the list of heritage sites.
# Display the list of world heritage sites in India.
# Search and display information of a world heritage site entered by the user.
# Display the name(s) of world heritage site(s) based on the state input by the user.
import pandas as pd

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
pwd = 'abc@1234'

d_ini = pd.read_csv('case3.csv').to_dict()
d_ct = {}
for k in list(d_ini.keys()):
    d_ct[k] = []
    for v in list(d_ini[k].values()):
        d_ct[k].append(v)

d_rk = {}
for elem in d_ct:
    d_rk[elem] = []
    for elem2 in d_ct[elem]:
        d_rk[elem].append(elem2)


def ini():
    print('\n\nWelcome to heritage sites directory.')
    menu()


def menu():
    print('\nApplication Menu:\n')

    print('Enter 1 for Opening search')
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
    print('\nEnter 1 for search by name')
    print('Enter 2 for search by state')
    print('Enter 3 for exit')
    action = input('Your input? ').lower()

    if action == '1':

        s = input('\nSearch by name (min. 1 character): ').lower()
        if len(s) == 0:
            print('\nPlease try again! (min. 1 character)')
            search()

        flg = []

        for i in d_rk['Site']:
            if s in i.lower():
                flg.append(i)
                occr = len([char for index, char in enumerate(flg) if char == i])

                st = d_rk['State'][[index for index, element in enumerate(d_rk['Site']) if element == i][occr - 1]]

                inf = d_rk['Info'][[index for index, element in enumerate(d_rk['Site']) if element == i][occr - 1]]

                print('\nSite: {}\nState: {}\nInformation:\n{}'.format(i, st, inf))

        if not flg:
            print('\nNot found!')

    elif action == '2':

        s = input('\nSearch by state (min. 1 character): ').lower()
        if len(s) == 0:
            print('\nPlease try again! (min. 1 character)')
            search()

        flg = []

        for i in d_rk['State']:
            if s in i.lower():
                flg.append(i)

                occr = len([char for index, char in enumerate(flg) if char == i])

                sit = d_rk['Site'][[index for index, element in enumerate(d_rk['State']) if element == i][occr - 1]]

                inf = d_rk['Info'][[index for index, element in enumerate(d_rk['State']) if element == i][occr - 1]]

                print('\nSite: {}\nState: {}\nInformation:\n{}'.format(i, sit, inf))

        if not flg:
            print('\nNot found!')

    elif action == '3':
        menu()

    else:
        print('\nPlease chose from 1/2/3')
        search()

    searchagain = input('\nSearch again? (y/n): ').lower()

    if searchagain == 'y':
        search()
    else:
        menu()


def change():
    print('\nChange a record information:')
    print('To go back to menu, press <enter>')
    admin = input('Please enter the password: ')
    if admin == '':
        menu()
    elif admin == pwd:
        print('\nWelcome Admin!')

        print('\nSelect the site you want to edit:')
        print('(Please enter the number 1/2/3/4...)')

        count = 1

        for i in d_rk['Site']:
            print('{} - {}'.format(count, i))
            count += 1
        count -= 1

        inp = input('\nYour input? ')

        for i in inp:
            if i not in digits or inp == '':
                print('Please enter positive integral values only!')
                change()

        action = int(inp)

        if action == 0 or action > count:
            print('Out of range! Please try again\n')
            change()

        print('Current info is:\n{}'.format(d_rk['Info'][action - 1]))

        new_inf = input('\nNew info: ')
        if new_inf == '' or len(new_inf) == 0:
            print('Please try again! Minimum 1 character is required!')
            change()
        else:
            d_rk['Info'][action - 1] = new_inf

        site = d_rk['Site'][action - 1]
        state = d_rk['State'][action - 1]
        new_inf = d_rk['Info'][action - 1]

        print('\nSite: {}\nState: {}\nInformation: {}'.format(site, state, new_inf))

        change_more = input('\nChange something else? (y/n)').lower()
        if change_more == 'y':
            change()
        else:
            menu()
    else:
        print('\nWrong password! Please try again')
        change()


def delete():

    print('\nDelete a record:')
    print('To go back to menu, press <enter>')
    admin = input('Please enter the password: ')
    if admin == '':
        menu()
    elif admin == pwd:
        print('\nWelcome Admin!')

        print('\nSelect the record you want to delete:')
        print('(Please enter the number 1/2/3/4...)')

        count = 1

        for i in d_rk['Site']:
            print('{} - {}'.format(count, i))
            count += 1
        count -= 1

        inp = input('\nYour input? ')

        for i in inp:
            if i not in digits or inp == '':
                print('Please enter positive integral values only!')
                delete()

        action = int(inp)-1

        sure = input('Are you sure you want to delete data for {}? (y/n): '.format(d_rk['Site'][action])).lower()

        if sure == 'y':
            del d_rk['Site'][action]
            del d_rk['State'][action]
            del d_rk['Info'][action]
            print('\nDeleted!')

        if action == 0 or action > count:
            print('Out of range! Please try again\n')
            delete()

        delete_more = input('\nDelete something else? (y/n)').lower()
        if delete_more == 'y':
            delete()
        else:
            menu()
    else:
        print('\nWrong password! Please try again')
        delete()


def add_elem():

    print('\nAdd a record:')
    print('To go back to menu, press <enter>')
    admin = input('Please enter the password: ')
    if admin == '':
        menu()
    elif admin == pwd:
        print('\nWelcome Admin!')

        print('\nPlease enter the record details here, or press <enter> to bo back:')

        add_site = input('Name of the Heritage Site: ')
        for i in d_rk['Site']:
            if add_site.lower() == i.lower():
                print('Site name already present!')
                print('Please try again')
                add_elem()

        if add_site == '':
            print('Redirecting to menu.')
            menu()
        else:
            d_rk['Site'].append(add_site)

        add_state = input('State where {} is found: '.format(add_site))
        if add_state == '':
            print('Redirecting to menu.')
            menu()
        else:
            d_rk['State'].append(add_state)

        add_info = input('Information about {}: '.format(add_site))
        if add_info == '':
            print('Redirecting to menu.')
            menu()
        else:
            d_rk['Info'].append(add_info)

        add_more = input('\nAdd something else? (y/n): ').lower()
        if add_more == 'y':
            add_elem()
        else:
            menu()


def reset():
    global d_rk

    d_rk.clear()
    d_rk = {}
    for i in d_ct:
        d_rk[i] = []
        for j in d_ct[i]:
            d_rk[i].append(j)

    print('\nSuccessfully reset the data!')
    menu()


def disp():
    print('\nHeritage Sites Data:')
    print("{:<20}  {:<20}  {}\n".format('Site', 'State', 'Information'))

    x = 0
    while x < len(d_rk['Site']):
        site = d_rk['Site'][x]
        state = d_rk['State'][x]
        info = d_rk['Info'][x]

        print("{:<20}  {:<20}  {}".format(site, state, info))
        x += 1

    menu()


ini()
