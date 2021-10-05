d = {1: 'Abc', 2: 'Def', 3: 'Ghi', 4: 'Jkl'}

a = 1
lst = []
while a <= len(d):
    lst.append(d[a])
    a += 1

print(lst)
