def getInt(msg:str=''):
    return int(input(msg if msg != '' else '> '))

def getStr(msg:str=''):
    return str(input(msg if msg != '' else '> '))

def click():
    input('click to continue')
    return True

def formatNumberToTwoDigits(n):
    """
    This function is created just to fil numbers with two digits
    Args:
        n(int) : 2
    Return:
        n(str) : 02
    """
    return '0' + str(n) if len(str(n)) == 1 else n
