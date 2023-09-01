from secundary_functions import *

def addNewPage():
    data = createNewPageMetadata() 
    createRowInPageTracker(data) #takes a dict and pushes it to the csv
    createFile(data)

def pickPageFromFiles(mode):
    pickPage(mode)
     

def app():
    appContinue = True
    while appContinue:
        showTitle('Page app')
        showMenu()
        option = getInt() 
        if(option == 1):
            addNewPage()
            
        elif(option == 2):
            pickPageFromFiles('all')

        elif(option == 3):
            pickPageFromFiles('category')

        elif(option == 4):
            pickPageFromFiles('type')

        elif(option == 5):
            return False

        else:
            print('unvalid option inserted.')
            click()



