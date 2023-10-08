from collectDataFromUser import *
import pandas as pd
import csv

class Assignment(object):
    
    def __init__(self, name):
        self.name = name
        self.path = './semesters_content/grades/{}.csv'.format(self.name)

    def createAssignment(self): 
        #1. Register in ./semester_content/actual_assignments.csv
        #2. Create a file in ./semester_content/grades 
        self.logAssignment()
        self.createGradesLogs()

    def addGrade(self):
        #data is a dictionary
        data = collectDataFromUser(['grade','cut','percentage'], 'Add Note')
        self.insertGradeInDB(data)

    def getGrades(self):
        df = pd.read_csv(self.path)
        return df

    def removeGrade(self, ind):
        df = pd.read_csv(self.path) 
        df = df.drop(labels=ind, axis=0).set_index('grade')
        data = df.to_csv()
        self.updateGrades(data)

    @classmethod
    def getAssignments(cls):
        assignments = pd.read_csv('./semesters_content/actual_assignments.csv')
        return list(assignments['name'])

    #helper
    def updateGrades(self, grades:str):
        with open(self.path, mode='w') as f:
            f.write(grades)

    #helper
    def insertGradeInDB(self, data):
        max_points = (data['percentage'] * 20) / 100
        points = (data['grade'] * max_points) / 20
        data['points'] = points
        with open(self.path, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=data.keys())
            writer.writerow(data)


    #helper
    def logAssignment(self):
        with open('./semesters_content/actual_assignments.csv', mode='a') as f:
            writer = csv.writer(f)
            writer.writerow([self.name])
        

    #helper
    def createGradesLogs(self):
        with open(self.path, mode='x') as f:
            with open(self.path, mode='w') as f:
                writer = csv.writer(f)
                header = ['grade', 'cut', 'percentage','points']
                writer.writerow(header)




