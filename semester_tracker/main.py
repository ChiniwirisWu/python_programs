from secundary_functions import *
from semester import Semester
from display import Display

def app():
    if(Semester.exists()):
        appOpen = True
        while appOpen:
            Display.showTitle('Semester tracker')
            Display.showElementsAsOrderedList(['Show grades', 'Add grades', 'Remove grades', 'Quit'])
            option = getInt()
            if(option == 1):
                Semester.showGrades()
                click()
            if(option == 2):
                Semester.addGrade()
            if(option == 3):
                pass
            if(option == 4):
                appOpen = False
    else:
        Semester.setUpNewSemester() # Works
        app()

app()
