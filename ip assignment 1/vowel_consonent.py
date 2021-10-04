var = input("Please Enter Any Character: ")
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']
vow = ['a', 'e', 'i', 'o', 'u']


if len(var) == 1:
    varl = var.lower()
    if varl in alph:
        if varl in vow:
            vartype = "vowel"
        else:
            vartype = "consonant"
        print(var, 'is an alphabet -', vartype)
    elif '0' <= var <= '9':
        print(var, "is a number")
    else:
        print(var, "is a special character")
else:
    print("Single character only!")
