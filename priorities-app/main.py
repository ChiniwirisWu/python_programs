from display import *
from priorities import *

def app():
    appOn = True
    while appOn:
        showTitile('Priorities app')
        showList(['Show list', 'Add Priority', 'Remove Priority' ,'Exit app'])
        option = int(input('\n> ')) 

        if(option == 1):
            showTitile('Priorities')
            showPriorities()
        
        elif(option == 2):
            showTitile('Add priority')
            addPriority()

        elif(option == 3):
            showTitile('Remove priority')
            removePriority()

        elif(option == 4):
            appOn = False
            continue
app()

