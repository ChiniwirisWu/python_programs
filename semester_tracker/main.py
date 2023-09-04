from semester import Semester
from display import Display

def app():
    if(Semester.exists):
        appOpen = True
        while appOpen:
            Display.showTitle('Semester tracker')
            Display.showElementsAsOrderedList(['Show grades', 'Add grades', 'Remove grades', 'Quit'])
            input()
        print('Looged')
    else:
        Semester.setUpNewSemester() # Works
        app()

app()
