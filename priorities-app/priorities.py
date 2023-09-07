import pandas as pd
import random
import numpy as np

def showPriorities():
    df = pd.read_csv('./priorities.csv')
    if(df.shape[0] == 0):
        print("There's no priorities")
        input()
        return

    df = df.nlargest(100, 'importance').reset_index(drop=True)
    print(df)
    input('\n')

def removePriority():
    df = pd.read_csv('./priorities.csv')
    if(df.shape[0] == 0):
        print("There's no priorities")
        input()
        return

    df = df.nlargest(100, 'importance').reset_index(drop=True)
    print(df)
    n = int(input('Insert priority index (-1 to cancel): '))
    if(n == -1):
        return

    if(n >= 0 and n <= df.shape[0]):
        main_df = pd.read_csv('./priorities.csv')
        new_id = df.iloc[n]['id']

        index = main_df[main_df['id'] == new_id].index
        main_df = main_df.drop(labels=index, axis=0)
        main_df = main_df.set_index('name')
        data = main_df.to_csv()

        with open('./priorities.csv', mode='w') as f:
            f.write(data)

def addPriority():
    name = str(input('Title ("" to cancel): '))
    if(name == ""):
        return
    importance = float(input('Importance (1 - 10) (0 to cancel): '))
    if(importance == 0):
        return


    #getting the index of the new row
    priorities = pd.read_csv('./priorities.csv')
    importances = np.array(list(priorities['importance']), dtype='f') 
    importances = np.sort(importances)
    # new_index = np.searchsorted(importances, importance, side='right')

    #adding new row to dataframe
    new_row = pd.DataFrame(data={'name': name, 'importance':importance, 'id':random.randint(1000, 1000000)}, index=[0])
    priorities = priorities.append(new_row, ignore_index=True)
    priorities = priorities.set_index('name')

    #adding new dataframe into csv
    new_data = priorities.to_csv()
    with open('./priorities.csv', mode='w') as f:
        f.write(new_data)



