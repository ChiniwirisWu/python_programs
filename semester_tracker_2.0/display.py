import os

class Display(object):

    def __init__(self, title):
        self.title = title

    def showTitle(self):
        print('')
        os.system('cls||clear')
        print('# ---------- # {} # ---------- #\n'.format(self.title))

    def listAndShowElements(self, fields:list):
        for i in range(len(fields)):
            print('{}  {}'.format(i + 1, fields[i]))
    
    def showMenu(self):
        self.showTitle()
        self.listAndShowElements(['See grades', 'Add grade', 'Remove grade' ,'Quit'])



