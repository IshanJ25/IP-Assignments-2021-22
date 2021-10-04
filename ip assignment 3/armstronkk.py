# Python program to check if the number is an Armstrong number or not
num = input("Enter a number: ")

lst = list(num)
lstlen = len(lst)
count = 0
amst = 0
while count < lstlen:
    amst += int(lst[count]) ** lstlen
    count += 1

if amst == num:
    print('yay! armstronkk!')
else:
    print('no armstronkk')
