from display import Display

def collectDataFromUser(fields:list, title):
    data:dict = {}
    display = Display(title)
    display.showTitle()
    for el in fields:
        data[el] = getInt(el)
    return data

def getInt(msg:str=''):
    return int(input('\n{}: '.format(msg)))

def getStr(msg:str=''):
    return str(input('\n{}: '.format(msg)))

def click():
    input('\nClick to continue')
