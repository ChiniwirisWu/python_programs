import random
from helpers import clear, intInput

def menu():
    clear()
    print('#----------# Password generator #----------#')
    print('\n(1) Generate new password\n(2) Quit')
    n = intInput() 
    return n

def generatePassword():
    clear()
    print('#----------# Password generator #----------#')
    print('Insert the length of the new password:')
    n = intInput()
    print('Insert how many passwords to be generated:')
    m = intInput()
    passwords:list = []

    for j in range(m):
        password:str = '' 
        for i in range(n):
            password += chr(random.randint(33, 126))
        passwords.append(password)
    
    return passwords