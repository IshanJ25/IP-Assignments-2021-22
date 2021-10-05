# 'listName:' ['Name', 'DOB', 'Color HEX', 'Weight(kg)', 'Height(m)']
import pandas as pd
d = {
    'abc': ['Abc Def', '03 Aug 2005', '#ffb300', 60, 1.58],
    'ghi': ['Ghi Jkl', '07 Feb 2005', '#ff3300', 61, 1.62],
    'mno': ['Mno Pqr', '23 Apr 2004', '#33ff00', 78, 1.75],
    'stu': ['Stu Vwx', '13 Dec 2006', '#00c8ff', 70, 1.69],
    'jkl': ['Jkl Mno', '18 Jun 2006', '#5000ff', 67, 1.71],
    'yza': ['Yza Cdf', '29 Oct 2005', '#ff0050', 65, 1.68],
}
df = pd.DataFrame.from_dict(d, orient='index')
print(df)
