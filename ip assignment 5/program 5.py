print('Please enter names and marks of 10 students')
print('Names should be unique and marks in integral value\n')

d = {}
d2 = {}
txt = ''
mrk = 0
i = 1

while i <= 10:
    txt = input('Name {}: '.format(i))
    mrk = int(input('Marks: '))
    print()

    if txt not in d:
        d[txt] = mrk
        i += 1
    else:
        print('Record for name {} already exists! '
              'Please use different name.\n'.format(i))

e = {i: [] for i in list(d.values())}

for key, val in d.items():
    e[val].append(key)

for i in range(0, 5):
    d2[sorted(e.keys(), reverse=True)[i]] = e[sorted(e.keys(), reverse=True)[i]]

print(e)
print(d2)

for i in d2.keys():
    for j in d2[i]:
        print('{} marks received by {}'.format(i, j))
