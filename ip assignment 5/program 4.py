# to reads 2 strings & print the common words

t1 = input('Text 1: ').lower()\
    .replace('.', '').replace(',', '')
t2 = input('text 2: ').lower()\
    .replace('.', '').replace(',', '')

l1 = t1.split()
l2 = t2.split()
d = {}

for i in l1:
    if i in l2:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

j = [i for i in d.keys()]
print('Common words:')
for i in j:
    print(i, end=', ')
