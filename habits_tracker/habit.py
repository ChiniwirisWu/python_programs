from collectDataFromUser import *
import os
import pandas as pd
import csv
from display import Display

class Habit(Display):

    def __init__(self):
        self.habits_path = './habits.csv'

    def addHabit(self):
        self.showTitle('Creating habit')
        name = getStr('Name ("" to cancel): ')
        if(name == ""):
            return

        #adding a new row in habits.csv
        with open(self.habits_path, mode='a') as f:
            writer = csv.writer(f)
            writer.writerow([name])


    def removeHabit(self):
        self.showTitle('Removing habit')
        #getitng the habits
        habits = pd.read_csv(self.habits_path)
        elements = list(habits['name'])

        #showing the habits and selecting one
        self.showlist(elements)
        option = getInt('\noption (0 to cancel): ')

        if(option == 0):
            return

        #removing habit from csv
        habits = habits.drop(labels=[option - 1], axis=0) # drop method, returns the dataframe without a row or column
        habits = habits.set_index('name')
        data = habits.to_csv()

        #updating data in habits.csv
        with open(self.habits_path, mode='w') as f:
            f.write(data)

        
    #helper
    def getHabitsList(self):
        return list(pd.read_csv(self.habits_path)['name']) 






