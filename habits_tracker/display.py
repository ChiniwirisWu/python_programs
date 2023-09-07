import os

class Display(object):

    def showTitle(self, title):
        os.system('cls||clear')
        print('# ---------- # {} # ---------- #'.format(title))

    def showlist(self, elements:list):
        for i in range(len(elements)):
            print('{}   {}'.format(i + 1, elements[i]))
