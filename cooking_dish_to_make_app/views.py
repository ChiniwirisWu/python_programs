import os
import numpy as np
from data import ingredients, recipies

def clear():
    print('')
    os.system('cls||clear')

getInt = lambda: int(input('\n> ')) 

def showDishes():
    avaliable:list = []
    for key, value in recipies.items():
        collection:list = []
        for name, ing in ingredients.items():
            if(name in value):
                collection.append(name) 
        if(len(collection) == len(value)):
            avaliable.append(key)
    print(ingredients)
    print(avaliable)
    input()
            



def addRecipie():
    clear()
    print('# ---- # Add recipie # ---- #')
    counter = 1
    name = str(input('Name: '))
    ingredients:list = []
    while True:
        print('Insert "" to end list')
        ingredient = str(input('ingredient #{}: '.format(counter)))
        if(ingredient == ""):
            break
        ingredients.append(ingredient)
        counter += 1
    recipies[name] = ingredients
    print('{} added successfully'.format(name))
    input('\nClick to continue')


def showIngredients():
    clear()
    counter = 1
    print('# ---- # Ingredients # ---- #')
    for key, value in ingredients.items():
        print('({}) {} = {}'.format(counter, key, value))
        counter += 1
    input('\nclick to continue')
        

def addIngredient():
    print('(1) Add to an existing ingredient\n(2) Add new ingredient')
    n = getInt() or 2
    if(n == 1):
        while True:
            counter = 1
            clear()
            print('# ---- # Ingredients # ---- #')
            print('Insert to 0 to quit\n')
            for key, value in ingredients.items():
                print('({}) {} = {}'.format(counter, key, value))
                counter += 1
            print('Select a ingredient')
            n = getInt()
            if(n == 0): break
            print('Select how many to be added to {}'.format(tuple(ingredients.items())[n - 1][0]))
            a = getInt()
            ingredients[tuple(ingredients.items())[n - 1][0]] += a
            input('\n Click to continue')
    else:
        print('Insert new Ingredient: ')
        name = str(input('Name: ')) 
        amount = int(input('Amount: ')) 
        ingredients[name] = amount
        input('\n Click to continue')

def removeIngredients():
    print('# ---- # Ingredients # ---- #')
    counter = 1
    for key, value in ingredients.items():
        print('({}) {} = {}'.format(counter, key, value))
        counter += 1
    print('Select a ingredient')
    n = getInt()
    print('Select amount')
    a = getInt()
    print(tuple(ingredients.items()))
    ingredients[tuple(ingredients.items())[n - 1][0]] -= a
    if(ingredients[tuple(ingredients.items())[n - 1][0]] <= 0):
        ingredients.pop(tuple(ingredients.items())[n - 1][0])
    input('\n Click to continue')

def showRecipies():
    clear()
    print('# ----- # Recipies # ---- #')
    counter = 1
    for key, value in recipies.items():
        print('({}) {}, ingredients: {}'.format(counter, key, value))
        counter += 1
    input('\nClick to continue')

def removeRecipie():
    clear()
    print('# ----- # Recipies # ---- #')
    showRecipies()
    print('Select recipie')
    n = getInt()
    name = tuple(recipies.items())[n - 1][0]
    recipies.pop(name)
    print('{} removed successfully'.format(name))
    input('\nClick to continue')

def menu():
   while True:
        clear()
        print('# ----- # Dish recomendator # ---- #')
        print('(1) Show avaliable dishes\n(2) Add ingredients\n(3) Remove ingredients\n(4) Show recipies\n(5) Show ingredients\n(6) Add recipie\n(7) Remove recipie\n(8) Quit application')
        option = getInt()
        if option == 1:
            showDishes()
        elif option == 2:
            addIngredient()
        elif option == 3:
            removeIngredients()
        elif option == 4:
            showRecipies()
        elif option == 5:
            showIngredients()
        elif option == 6:
            addRecipie()
        elif option == 7:
            removeRecipie()
        elif option == 8:
            print('App close')
            break
