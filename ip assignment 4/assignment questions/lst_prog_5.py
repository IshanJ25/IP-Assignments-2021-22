a = 'The Republic of India is a country in South Asia. '\
    'It is the largest democracy in the world.'.lower()\
    .replace('.', '').replace(',', '')
b = a.split()
lst = []
for i in b:
    if i not in lst:
        lst.append(i)
print(lst)
