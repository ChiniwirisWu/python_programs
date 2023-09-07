import os

def showTitile(title):
    os.system('cls||clear')
    print('# ---------- # {} # ---------- #\n'.format(title))

def showList(options:list):
    for i in range(len(options)):
        print('{}   {}'.format(i + 1, options[i]))
