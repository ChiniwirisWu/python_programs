import os

class Display:

    @classmethod
    def showElementsAsOrderedList(cls, elements:list):
        """
        Args:
            elements:list
        Return:
            print(): 
                1. element1
                2. element2
                3. element3
        """
        for i in range(len(elements)):
            print('({}) {}'.format(i + 1, elements[i]))

    @classmethod
    def showTitle(cls, title):
        cls.clearTerminal()
        print('# ---------- # {} # ----------- #'.format(title))
        print('\n')

    @classmethod 
    def clearTerminal(cls):
        print('')
        os.system('cls||clear')
