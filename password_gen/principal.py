from methods import generatePassword, menu
activeApp = True

while activeApp:
    print('')
    option = menu()
    if(option == 1):
        passwords = generatePassword()
        print('Your password{} {}:'.format("'s" if len(passwords) > 1 else '', 'are' if len(passwords) > 1 else 'is'))
        for el in passwords:
            print(el)

        input('\nclick any button to continue')
    elif(option == 2):
        activeApp = False
        continue
    else:
        print('Invalid option')
        input('\nclick any button to continue')


