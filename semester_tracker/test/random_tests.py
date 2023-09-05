#this does not work
# phrase = 'hola'.append(' hello')
# print(phrase)

# import os
#  os.remove('./hi.txt')

# with open('./hi.txt', mode='x') as f:
    # f.write('hi')
#looks like, open mode w creates a buffer, but it doesn't creates a file

import pandas as pd

df = pd.read_csv('./data.csv')

print(dict(df))

# names = df['name']
# print(type(names))
#series seems similar to arrays
# print(df)
# print(df['name'])
# print(names['name'])

df = df[df['name'] == 'gilberto']
print(type(df))

actual_semester_df = pd.read_csv('../semesters_log/actual_semester.csv')
semester_name = actual_semester_df.iloc[0,0]

semesters_df = pd.read_csv('../semesters_log/semesters_log.csv')
#dataframe object

semester_info:dict = {}
actual_semester_info = semesters_df[semesters_df['name'] == semester_name]
for el in actual_semester_info.columns:
    semester_info[el] = actual_semester_info[el]
print(semester_info)

