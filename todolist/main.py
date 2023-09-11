import pandas as pd
import os
import csv
from datetime import date

def app():
    genHabits()
    while True:
        showTitle('To-Do-App')
        showMenu()
        option = getInt()
        if(option == 1):
            checkTodaysTask()
            
        if(option == 2):
            addTask()

        if(option == 3):
            break

def getInt():
    return int(input('\n> '))

def getHabits():
    df = pd.read_csv('./habits.csv')
    return df


def setTodayDate():
    df = pd.read_csv('./today_yesterday.csv')
    df['yesterday'].iloc[0,0] = df['today'].iloc[0,0] 
    df['today'].iloc[0,0] = date.today()

def genHabits():
    habits = getHabits()
    data = []
    for el in habits:
        habit = {} 
        habit['name'] = el
        habit['done'] = 0
        habit['date'] = date.today()
        data.append(habit)
    with open('./todos.csv', mode='a') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writerows(data)

def getStr():
    return str(input('\n> '))

def showTitle(title):
    os.system('cls||clear')
    print('# --------- # {} # --------- #'.format(title))
    print('\n')

def click():
    input('\nClick here to continue')

def checkTodaysTask():
    df = pd.read_csv('./todos.csv')
    if(df.shape[0] == 0):
        print("You completed all your tasks")
        click()
        return
    df = df[df['date'] == str(date.today())]
    habits = getHabits()
    df.append(habits)
    print(df)
    n = getInt() 
    if(n >= 0 and n <= df.shape[0]):
        df = df.drop(labels=[n], axis=0)
        with open('./todos.csv', mode='w') as f:
            df = df.set_index('name')
            data = df.to_csv()
            f.write(data)

def showList(options:list):
    for i in range(len(options)):
        print('{}  {}'.format(i + 1, options[i]))

def showMenu():
    showList(['check to-do', 'Add ToDo', 'Quit'])

def addTask():
    showTitle('name ("" to cancel)')
    name = getStr()
    if(name == ''):
        return
    data = {'name': name, 'done': 0, 'date':date.today()}
    with open('./todos.csv', mode='a') as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        writer.writerows([data])

app()
