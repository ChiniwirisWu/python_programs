from display import Display
import random
from collectDataFromUser import *
from matplotlib import pyplot as plt
import csv
import pandas as pd
from datetime import date
from habit import Habit

class Logs(Habit, Display):

    def __init__(self):
        super().__init__()
        self.logs_path = './logs.csv'

    @property
    def today(self):
        df = pd.read_csv('./today.csv')
        #in case there's no date, set today
        if(df.shape[0] == 0):
            with open('./today.csv', mode='a') as f:
                writer = csv.writer(f)
                writer.writerow([str(date.today())])

        return  df['date'][0]

    def createLinearImages(self,elements:list):
        arr = []
        counter = 0 
        for i in range(len(elements)):
            if(i == 0):
                arr.append(elements[i])
            else:
                counter = arr[i - 1] + elements[i]
                arr.append(counter)
        return arr

    def showLogs(self):
        habits = self.getHabitsList()
        print(habits)
        #data = {habit:{done:[], date:[]}, habit:{done:[], date:[]}}
        #data = [[[],[]], [[],[]], [[],[]]]
        data = []
        for i in range(len(habits)):
            df = pd.read_csv(self.logs_path)
            df = df[df['name'] == habits[i]]
            done = list(df['done']) 
            date = list(df['date'])
            element = []
            element.append(habits[i])
            element.append(self.createLinearImages(done)) 
            element.append(date)
            data.append(element)

        #show in a matplot
        for el in data:
            plt.title(el[0])
            plt.ylabel('done')
            plt.xlabel('date')
            plt.plot(el[2], el[1], c='red')
            plt.show()



    def setLogs(self):
        if(self.today != str(date.today())):
            habits = self.getHabitsList()
            today_logs = []
            #if there's no habits, there's no reason to excecute this method
            if(len(habits) > 0):
                for el in habits:
                    log = {}
                    log['name'] = el
                    log['done'] = 0
                    log['date'] = date.today()
                    log['id'] = random.randint(1,100000)
                    today_logs.append(log)
            #[{},{},{}] : I created this data structure
            with open(self.logs_path, mode='a') as f:
                writer = csv.DictWriter(f, fieldnames=['name','done','date','id'])
                writer.writerows(today_logs)
                self.updateDate()

    def updateDate(self):
        with open('./today.csv', mode='w') as f:
            writer = csv.writer(f)
            writer.writerows([['date'],[str(date.today())]])


    def markLog(self):
        while True:
            df = pd.read_csv(self.logs_path)
            df_undone = df[df['done'] == 0]
            if(df_undone.shape[0] == 0):
                print('You completed all your tasks for today. Congrats!')
                input()
                return
            self.showTitle('Mark completed habits')
            n = getInt('\nPick task (insert -1 to quit): ')
            if(n == -1):
                break
            if(n >= 0 and n < df_undone.shape[0]):
                row = df_undone.iloc[n, :]
                task_id = row['id']
                index = df[df['id'] == task_id].index
                df.loc[index, ['done']] = 1
                df = df.set_index('name')
                data = df.to_csv()
                with open(self.logs_path, mode='w') as f:
                    f.write(data)




