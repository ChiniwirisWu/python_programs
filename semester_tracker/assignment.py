import pandas as pd
import csv

class Assignment(object):
    def __init__(self, name):
        self.name = name
        self.path = './assignments_grades/{}.csv'.format(name)

    def getGrades(self):
        df = pd.read_csv(self.path)
        return df

    def addGrade(self, grade, cut, date, percentage, points):
        with open(self.path, mode='a') as f:
            writer = csv.writer(f)
            writer.writerow([grade, date, cut, percentage, points])


