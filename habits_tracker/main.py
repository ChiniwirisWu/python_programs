from display import Display
from habit import Habit
from collectDataFromUser import *
from logs import Logs

def app():
    display = Display()
    habit = Habit()
    logs = Logs()
    logs.setLogs()
    while True:
        display.showTitle('Habit tracker')
        display.showlist(elements=['check today performance','Remove check','Show performance', 'Add habit', 'Remove Habit', 'Quit'])
        option = getInt('\noption: ')

        if(option == 1):
            logs.markLog()

        if(option == 3):
            logs.showLogs()
        
        if(option == 4):
            habit.addHabit()

        if(option == 5):
            habit.removeHabit()

        if(option == 6):
            break

app()
