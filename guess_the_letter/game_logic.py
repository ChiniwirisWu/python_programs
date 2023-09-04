import random
import math
from Players import players_list
from Players import cleanTerminal
from constants import words
game_over = True

def selectWord():
    random_num = random.randint(0, len(words) - 1)
    return words[random_num]


def showLife():
    lifes = str()
    for el in players_list:
        lifes += '{} = {} hp.\n'.format(el.name, el.life)
    return lifes


def showWord(word):
    hide_word = str()
    """
    ' _ _ _' :(odd=space),(even=down) 
    """
    for i in range(len(word)):
        hide_word += '_ '
    hide_word = hide_word.strip()
    return hide_word


def fill_words(string, letter, word):
    """
    I need to recreate a string (I can't modify it by mutation)
    """
    hidden_word:str = str()
    for i in range(len(word)):
        if(word[i] in correctWords):
            hidden_word += word[i] + ' '
        else:
            hidden_word += '_ '


    return [hidden_word, word.count(letter)]

    


def gamePlay():
    """
    This function will have:
    1. Turn between players.
    2. Show word on screen. (done)
    3. guess letters.
    4. guess word. 
    5. Substract life from each mistake from the players.
    6. Game over or won message
    """
    global word_spaced 
    global correctWords
    correctWords = []
    word = selectWord()
    word_spaced = showWord(word) 
    points = 0
    counter = 0

    def resetLifes():
        for el in players_list:
            el.life = 10

    cleanTerminal()
    while game_over:
        print(showLife()) 
        print(word_spaced) 
        l = input('{} pick a letter: '.format(players_list[counter].name))

        #here the letter is processed
        if(l in word and l not in correctWords):
            correctWords.append(l)
            data = fill_words(word_spaced, l, word)
            word_spaced = data[0] 
            points += data[1]
        else:
            players_list[counter].substract_life(1)
            if(players_list[counter].life <= 0):
                print('You loose!')
                input()
                resetLifes()
                break

            

        #here the counter grows, so the turns will switch
        if counter == len(players_list) - 1:
            counter = 0
        else:
            counter += 1
        
        if(points == len(word)):
            print('You won!')
            input()
            resetLifes()
            break



    
