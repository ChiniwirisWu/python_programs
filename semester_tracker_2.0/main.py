from semester import Semester
from assignment import Assignment
from display import Display
from collectDataFromUser import *

def app():
    semester = Semester()
    if(semester.sessionExists()):
        print('Semester exists')

        appOpen = True
        while appOpen:
            display = Display(semester.name)  
            display.showMenu()
            option = getInt('Option')

            if(option == 1):
                semester.showGrades()
                click()

            elif(option == 2):
                semester.addGrades()

            elif(option == 3):
                semester.removeGrades()
                # removeGrade()

            elif(option == 4):
                appOpen = False
                continue
    else:
        semester.createSession()
        app()

app()
