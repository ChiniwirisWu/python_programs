import os

players_list:list = list()


cleanTerminal = lambda : os.system('cls||clear')
insertInt = lambda : int(input('> '))
insertStr = lambda : str(input('> '))



class Player(object):
    def __init__(self, name):
        self.life = 10
        self.name = name
    
    def __str__(self):
        return 'Player: {}\nLife: {}'.format(self.name, self.life)
    
    def substract_life(self, n):
        self.life -= n

def createPlayers():
    """
    This function creates (n) players and adds then to "players list".
    """
    cleanTerminal()
    print('Insert number of players: ')
    n = insertInt() 
    for i in range(n):
        cleanTerminal()
        print('Insert player {} name: \n'.format(i + 1))
        name = insertStr()
        new_player = Player(name=name)
        players_list.append(new_player)
        print('{} added successfully!'.format(name))
        input()

def showPlayers():
    """
    This function shows the players listed.
    """
    cleanTerminal() 
    for i in range(len(players_list)):
        print('({}) {}'.format(i + 1, players_list[i].name))

def removePlayer():
    cleanTerminal()
    showPlayers()
    print('Choose a player: ({}-{})\n'.format(1, len(players_list)))
    x = insertInt()
    x -= 1
    if(players_list[x] in players_list):
        players_list.pop(x)
    else:
        print('The player chosen doesn\'t exist.')

def removeAllPlayers():
    players_list.clear()
    print('All players have been erased.')
    input()

    
def menu():
   menu_state:bool = True
   while menu_state:
        cleanTerminal()
        print('Guessing word game!\n\n')
        print('(1) Play\n(2) Create Players\n(3) Delete Player\n(4) Delete all players\n(5) Quit')  
        x = insertInt()

        if (x == 1):
            return True
        elif (x == 2):
            createPlayers()
        elif (x == 3):
            removePlayer()
        elif (x == 4):
            removeAllPlayers()
        elif (x == 5):
            return False


