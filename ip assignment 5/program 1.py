# Print unique words in lower case

txt = input('Text here: ').lower() \
    .replace('.', '').replace(',', '')
words = txt.split()
d = {}

for i in words:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

keys = d.keys()
for i in keys:
    print(i, end=', ')
