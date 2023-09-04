from secundary_functions import *
import pandas as pd
import os
import csv
from display import Display
from datetime import date

class Semester:

    #this properties I get them from ./semesters_log/semesters_log.csv
    def __init__(self):
        #with a property I get all the info instead of asking for it. It's clever if it works
        #Seems like, properties are away from other scripts and that properties are private.
        data = self.getActualSemester
        self.name = data['name']
        self.path = data['path']
        self.number = data['number']
        self.date = data['date']

    @property
    def getActualSemester(self):
        """
        This method returns semesters name, which is the same as one on semesters_log
        Return 
            dict = {name, path, number, date}
        """
        
        name:str = ''
        fields:dict = {}
        
        df = pd.read_csv('./semesters_log/actual_semester.csv')
        if(df.shape[0] == 1):
            #getting the name of the file
            name = df.iloc[0,0]

        #getting the row from semesters_log
        df = pd.read_csv('./semesters_log/semesters_log.csv')
        df = df[df['name'] == name] 
        df = df.iloc[0, :]
        #parece que el objeto series si tiene clave-valor
        return dict(df)

    @property
    def exists(self):
        """
        This method returns if there are semesters logs registered
        """
        df = pd.read_csv('./semesters_log/actual_semester.csv')
        return df.shape[0] > 0
        

    @classmethod
    def setUpNewSemester(cls):
        #variable declarations
        number:int = 0
        assignments:list = []
        counter = 1
        today = date.today()

        #method behaiviour
        Display.showTitle('Setting up new semester')
        number = getInt('number: ')
        name = 'Semester_{}_{}'.format(formatNumberToTwoDigits(number), today) #Semester_03_2023/09/11
        path = name + '.csv'
        #adding the assignments
        while True:
            Display.showTitle('Setting up new semester')
            assignment = getStr('assignment #{} (insert "" to end): '.format(counter))
            if(assignment == ''):
                break
            assignments.append(assignment)
            counter += 1

        #check if the data is valid to perform the app correctly
        if(number <= 0 or len(assignments) < 1):
            print('Invalid information passed')
            click()
            cls.setUpNewSemester() 
        else:
            #add file to semesters_log/semesters_log.csv
            with open('./semesters_log/semesters_log.csv', mode='w') as f:
                writer = csv.writer(f)
                writer.writerows([['number', 'name' ,'path', 'date'], [number, name, path, today]])
            #logging semester
            with open('./semesters_log/actual_semester.csv', mode='w') as f:
                writer = csv.writer(f)
                writer.writerows([['name'], [name]])
                

            #creating assignments csv
            for el in assignments:
                path = './assignments_grades/{}.csv'.format(el)
                Assignment.createAssignment(path, el)


    @classmethod
    def createAssignment(cls, path, name):
        """
        This method creates a csv file
        Args:
            path(str) : name.csv
            name(str) : example 
        Return
            new file : ./assignments_grades/example.csv
        """
        #create file
        with open(path, mode='x') as f:
            pass
    
        #write headers
        with open(path, mode='w') as f:
            writer = csv.writer(f)
            writer.writerow(['grade', 'date', 'cut'])



        
