import pandas as pd

n = int(input("Number of Students: "))

if n >= 1:
    df = {'RollNo': [], 'Name': [], 'Marks': []}
    for i in range(n):
        r = int(input('Roll Number: '))
        j = str(input('Name: '))
        m = float(input('Marks %: '))
        df['RollNo'].append(r)
        df['Name'].append(j)
        df['Marks'].append(m)
    print(df)
    df = pd.DataFrame(df)
else:
    print('Zero Students, Everyone has passed to class 12')

print()
print()
print()
print(df)
