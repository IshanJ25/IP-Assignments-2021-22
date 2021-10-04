x = input("Check for palindromeness: ")

# y = reversed(x)
# 'hello' ==> 'olleh'
# '1234321' ==> 1234321'

xlist = [i for i in x]
a = len(xlist)-1
y = ""
while a >= 0:
    y += xlist[a]
    a -= 1

if x == y:
    print("Palindrome")
else:
    print("Not palindrome")
