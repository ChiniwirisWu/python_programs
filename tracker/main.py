import os 
import csv
import numpy as np
import pandas as pd
import datetime
from matplotlib import pyplot as plt

getInt = lambda : int(input('\n> '))
getString = lambda : str(input('\n> '))

def showHeader(title):
    print('')
    os.system('cls||clear')
    print('# ------ # {} # ------ #\n'.format(title))

def getActualTrackerUrl():
    with open('./tracker_name.csv', mode='r') as f:
        df = pd.read_csv('./tracker_name.csv') 
        name = df.iloc[0,0]
        path = './{}.csv'.format(name)
        return path

def getActualTrackerName():
    df = pd.read_csv('./tracker_name.csv')
    name = df.iloc[0, 0]
    return name
        

def removeTracker():
    showHeader('Remove tracker')
    if(os.path.exists('./tracker_name.csv')):
        old_tracker_path = getActualTrackerUrl()
        os.remove(old_tracker_path)
        os.remove('./tracker_name.csv')
    else:
        print('First you have to create a tracker on menu > option 3')
        input('\nClick to continue.')

def showMenu():
    showHeader('Tracker')
    print('(1) Add activity\n(2) See graph\n(3) Set tracker\n(4) Remove tracker\n(5) Quit app')

def setTracker():
    """
    This function creates to files:
    (1) ./tracker_name : there's going to be the name of the tracker 
    (2) ./{name}.csv   : there's going to be the data that will be used to create a graph (in this function, just creates the header)
    """
    #get data
    showHeader('Set tracker')
    print('Please, fill the fields.\n')
    showHeader('Name')
    name = getString()
    showHeader('Parameter')
    parameter = getString()

    #create csv with only a name
    path = './tracker_name.csv'
    #creating the file
    if(os.path.exists(path) == False):
        with open(path, mode='x') as f:
            pass
    #writing the name
    with open(path, mode='w') as f:
        writer = csv.writer(f)
        writer.writerow(['name'])
        writer.writerow([name])
    
    #create csv with the values to track
    path = './{}.csv'.format(name)
    if(os.path.exists(path) == False):
        #creating the file
        with open(path, mode='x') as f:
            pass
        #adding the header
        with open(path, mode='w') as f:
            writer = csv.writer(f)
            writer.writerow([parameter, 'date'])
        
def showGraph():
    showHeader('Graph')
    if(os.path.exists('./tracker_name.csv')):
        path = getActualTrackerUrl()
        df = pd.read_csv(path)
        y = df.iloc[:, 0]
        x = df.iloc[:, 1]
        headers = df.columns
        parameter = headers[0]
        title = getActualTrackerName()

        plt.title = title
        plt.ylabel = parameter
        plt.xlabel = 'date'
        plt.plot(x, y)
        plt.show()
    else:
        print('First you have to create a tracker on menu > option 3')
        input('\nClick to continue.')

def addActivity():
    showHeader('Add activity')
    if(os.path.exists('./tracker_name.csv')):
        #get the tacker csv
        path = getActualTrackerUrl()
        df = pd.read_csv(path)

        #set up the new data and create it
        parameter = df.columns[0]
        date = datetime.date.today()
        print('Set "{}" value for today ({}):'.format(parameter, date))
        val = getInt()
        data = {parameter: val, 'date': date}
        new_row = pd.DataFrame(data=data, index=[df.shape[0]])
        df = pd.concat([df] + [new_row], ignore_index=True) 
        # updated_data = [df.to_dict()] 
        # print(updated_data)
        updated_data = {
            parameter: list(df.iloc[:, 0]),
            'date': list(df.iloc[:, 1]),
        }
        print(updated_data)
    

        #update the tracker csv
        headers = list(updated_data.keys())
        print(headers)
        with open(path, mode='w') as f:
            writer = csv.writer(f)

            writer.writerow([parameter, 'date'])
            for i in range(len(updated_data[parameter])):
                writer.writerow([updated_data[parameter][i], updated_data['date'][i]])

        input('click to continue')
        
    else:
        print('First you have to create a tracker on menu > option 3')
        input('\nClick to continue.')


def app():
    appOpen = True
    while appOpen:
        showMenu()
        n = getInt()
        if(n == 1):
            addActivity()
        elif(n == 2):
            showGraph()
        elif(n == 3):
            setTracker()
        elif(n == 4):
            removeTracker()
        elif(n == 5):
            appOpen = False
        
app()

