from assignment import Assignment
from display import Display
import csv
from collectDataFromUser import *
import pandas as pd

class Semester(Assignment):

    def __init__(self):
        self.name = self.getSessionName()

    def sessionExists(self):
        path = './semesters_content/actual_session.csv'
        df = pd.read_csv(path)
        return df.shape[0] >= 1

    def getSessionName(self):
        path = './semesters_content/actual_session.csv'
        df = pd.read_csv(path)
        if(df.shape[0] == 1):
            return df.iloc[0, 0]
        return False
    
    def createSession(self):
        data = collectDataFromUser(['name'], 'create session')
        self.insertSessionInDB(data['name'])
        self.setUpAssignments()

    def setUpAssignments(self):
        assignments = self.collectAssignments()
        for el in assignments:
            assignment = Assignment(el)
            assignment.createAssignment()

    def showGrades(self):
        assignments = self.getAssignments()
        display = Display('Grades')
        display.showTitle()
        for el in assignments:
            assignment = Assignment(el)
            grades = assignment.getGrades().sort_values(by='cut', ascending=True)
            print(el)
            print(grades)
            print('\n')

    def addGrades(self):
        display = Display('Add grades')
        assignments = self.getAssignments()
        while True:
            display.showTitle()
            display.listAndShowElements(assignments)
            option = getInt('option (0 to quit)')
            if(option == 0):
                break
            if(option > 0 and option <= len(assignments)):
                name = assignments[option - 1]
                assignment = Assignment(name)
                assignment.addGrade()
        
    def removeGrades(self):
        display = Display('Remove grades')
        assignments = self.getAssignments()
        while True:
            display.showTitle()
            display.listAndShowElements(assignments)
            option = getInt('option (0 to quit)')
            if(option == 0):
                break
            if(option > 0 and option <= len(assignments)):
                name = assignments[option - 1]
                assignment = Assignment(name)
                grades = assignment.getGrades()
                display.showTitle()
                print(grades)
                n = getInt('Pick grade')
                if(n >= 0 and n <= grades.shape[0]):
                    assignment.removeGrade(n)


    #helper
    def collectAssignments(self):
        assignments:list = []
        counter = 1
        while True:
            name = getStr('Assigment #{} (insert "" when done): '.format(counter))
            if(name == ''): 
                break
            assignments.append(name)
            counter += 1
        return assignments
    
    #helper
    def insertSessionInDB(self, name):
        with open('./semesters_content/actual_session.csv', mode='w') as f:
            writer = csv.writer(f)
            writer.writerows([['name'], [name]])
        




    


