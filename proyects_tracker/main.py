import pandas as pd
import os

class Tracker(object):

    def __init__(self):
        self.PROYECTS_PATH = './proyects.csv'
        self.OPTIONS = ['add day', 'add proyect', 'exit']
        self.OPTIONS_METHODS = [self.addDay, self.addProyect, self.exit]

    def run(self):
        self.proyectsDisplay()
        self.selectOption()

    def proyectsDisplay(self):
        df = pd.read_csv(self.PROYECTS_PATH)
        os.system('clear||cls')

        for key, el in df.iterrows():
            print('{} {}'.format(key + 1, el.title))
            print('Achieved: {} days of {}'.format(el.actual_amount_of_days, el.total_days))
            print('\n')

    def selectOption(self):
        print(self.listInlineFormat(self.OPTIONS))
        option = int(input('\n> '))
        if(option > 0 and option <= len(self.OPTIONS)):
            self.OPTIONS_METHODS[option - 1]()
        else:
            self.proyectsDisplay()
            self.selectOption()

    def exit(self):
        pass

    def addProyect(self):
        adding = True
        while adding:
            os.system('cls||clear')
            name = str(input('name: '))
            days = str(input('days: '))
            print('\nAre you sure to add new proyect?')
            permission = str(input('y/n: '))
            if(permission == 'y'):
                data = {
                    'title': name,
                    'actual_amount_of_days': 0,
                    'total_days': days
                }
                new_row = pd.DataFrame(data, index=[0])
                df = pd.read_csv(self.PROYECTS_PATH)
                df = pd.concat([df, new_row])
                df = df.set_index('title')
                data = df.to_csv()
                with open(self.PROYECTS_PATH, mode='w') as f:
                    f.write(data)
                    adding = False
            else:
                adding = False
        self.run()
            

    def addDay(self):
        adding = True
        while adding:
            self.proyectsDisplay()
            print('Select the proyect: ')
            option = int(input('> '))
            if(option > 0 and option <= len(self.OPTIONS)):
                print('Are you sure to add a day to: {}'.format(self.OPTIONS[option - 1]))
                permission = str(input('y/n: '))
                if(permission == 'y'):
                    df = pd.read_csv(self.PROYECTS_PATH)
                    df.loc[option - 1, 'actual_amount_of_days'] += 1
                    df = df.set_index('title')
                    data = df.to_csv()
                    with open(self.PROYECTS_PATH, mode='w') as f:
                        f.write(data)
                        adding = False
                else:
                    adding = False
            else:
                continue
        self.run()


    def listInlineFormat(self, elements):
        options = str()
        for i in range(len(elements)):
            if(i == len(elements) - 1):
                options += '({}) {}'.format(i + 1, elements[i])
            else:
                options += '({}) {}, '.format(i + 1, elements[i])
        return options


app = Tracker()
app.run()
