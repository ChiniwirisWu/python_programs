import os
import csv
import datetime 
import numpy as np
import pandas as pd
from default_data import *


def createFile(data):
    path = data['path']
    content = ''
    #1 get the contetn
    while True:
        showTitle(data['title'])
        print('All the content will be added, any text is erased.')
        content += getStr() + '\n'
        yesNo = getStr('The file is ready to be save? y/n')
        if(yesNo == 'y'):
            break
    #creates the file if it doesn't exists
    if(os.path.exists(path)):
        with open(path, mode="x") as f:
            pass
    #writes on the file the content
    with open(path, mode='w') as f:
        f.write(content)

def createRowInPageTracker(data:dict):
    with open('./page_tracker.csv', mode='a') as f:
        csv.register_dialect('mydialect', delimiter=',', skipinitialspace=True, quoting=csv.QUOTE_NONE)
        writer = csv.DictWriter(f, fieldnames=['title', 'type', 'category', 'path', 'date'], dialect='mydialect')
        writer.writerow(data)


def pickPage(mode):
    #mode can be all, category, type
    df = getDataFrame(mode)
    readingPages =  True
    while readingPages:
        readingPage = True
        showPages(df)
        n = getInt('page (0 to exit)') 
        if(n == 0):
            readingPages = False
            continue
        row = df.iloc[n - 1, :]
        path = row['path']
        title = row['title']
        if(n > 0 and n <= df.shape[0]):
            while readingPage:
                with open(path, mode='r') as f:
                    showTitle(title)
                    print(f.read())
                    quitInput = getStr('Click e to Exit')
                    if(quitInput == 'e'):
                        f.close()
                        readingPage = False
                        break
    return 


def createNewPageMetadata():
    #this function creates a dictionary with the information to create a csv to track the pages in the /pages directory
    data = {
            'date' : '',
            'title':'',
            'type':'',
            'category':'',
            'path': ''
            }
    for el in data:
        showTitle(el)
        if(el == 'category' or el == 'type'):
            #fill category and type
            data[el] = selectOrCreateNewField(el)

        elif(el == 'date'):
            #fill date
            data[el] = datetime.date.today()

        elif(el == 'title'):
            #fill title
            data[el] = '{} {}'.format(getStr('title'), data['date'])
        elif(el == 'path'):
            data[el] = './pages/{}.txt'.format(data['title'])
    return data











def getAllPages():
    df = pd.read_csv('./page_tracker.csv')    
    return df


def showPages(df):
    showTitle('Pick a page')
    for key, el in df.iterrows():
        print(key + 1, el.title)


def showTitle(title):
    """
    This function cleans the console and also shows the title of the page
    Args:
        title:str
    Return:
        print(title)
    """
    print('')
    os.system('cls||clear')
    print('# -------- # {} # -------- #'.format(title))


def getDataFrame(mode):
    df = getAllPages()
    if(mode == 'category' or mode == 'type'):
        #show fields avaliable
        showTitle(mode)
        values = getFieldValues(mode) 
        showFieldOptions(values, mode)
        print('\n select a {}'.format(mode))
        field = getInt()
        field = values[field - 1]
        return df[df[mode] == field]



    return df


def selectOrCreateNewField(field):
    values = getFieldValues(field)
    showFieldOptions(values, field)
    while True:
        print('\ninsert "-1" to create a new {}'.format(field))
        option = getInt()
        if(option == -1):
            return createNewField(field)
        elif (option > 0 and option <= len(values)):
            return values[option - 1]


def createNewField(field:str):
    name = getStr(field)
    return name


def showMenu():
    print('(1) Add new page\n(2) Show all pages\n(3) Show pages by category\n(4) Show pages by type\n(5) Quit app')


def getFieldValues(field:str):
    #returns all the elements for categories and type and also it adds some default options
    df = pd.read_csv('./page_tracker.csv')
    values = df[field].unique()
    if(field == 'category'):
        values = np.unique(np.concatenate((values, default_categories), axis=0)) 

    elif(field == 'type'):
        values = np.unique(np.concatenate((values, default_types), axis=0))
    return values

def showFieldOptions(values:list, field:str):
    print('{}: \n'.format(field))
    counter = 1
    for el in values:
        print('{}  {}'.format(counter, el))
        counter += 1

getInt = lambda msg='' : int(input('\n\n> ' if msg=='' else '{}: '.format(msg)))
getStr = lambda msg='' : str(input('\n\n> ' if msg=='' else '{}: '.format(msg)))
click = lambda : input('\nClick to continue.')
