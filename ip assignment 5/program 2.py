# to display letters in decreasing order

txt = input('Text here: ').lower()
letrs = list(txt)
d = {}

for i in letrs:
    if 'a' <= i <= 'z':
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

print(d)
e = {i: [] for i in d.values()}

for key, val in d.items():
    e[val].append(key)
print(e)

for i in sorted(e.keys()):
    for j in e[i]:
        print(j, ": ", i, " times", sep="")
