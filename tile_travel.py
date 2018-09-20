'''
Algorithmi fyrir 3x3 grid leik
Búa til lúppu og harðkóða núverandi staðsettningu og möguleika í hverju skrefi.
Prufa ef input matchar við möguleika og breyta núverandi staðsettningu miðað við það.
'''


current_tile = 1
game_over = False
not_valid = 'Not a valid direction!'

directions = ['(N)orth', '(E)ast', '(S)outh' , '(W)est']

you_can = 'You can travel: '

while game_over == False:
    counter = 0
    while current_tile == 1:
        if counter == 0:
            print(you_can + directions[0] + '.')
        ask_user = input('Direction: ')
        if ask_user.lower() == 'n':
            current_tile = 2
            break
        else:
            print(not_valid)
        counter += 1
    counter = 0
    while current_tile == 2:
        if counter == 0:
            print(you_can + directions[0] + ' or ' + directions[1] + ' or ' + directions[2] + '.')
        ask_user = input('Direction: ')
        if ask_user.lower() == 'n':
            current_tile = 3
            break
        elif ask_user.lower() == 's':
            current_tile = 1
            break
        elif ask_user.lower() == 'e':
            current_tile = 5
            break
        else:
            print(not_valid)
        counter += 1
    counter = 0
    while current_tile == 3:
        if counter == 0:
            print(you_can + directions[1] + ' or ' + directions[2] + '.')
        ask_user = input('Direction: ')
        if ask_user.lower() == 's':
            current_tile = 2
            break
        elif ask_user.lower() == 'e':
            current_tile = 6
            break
        else:
            print(not_valid)
        counter += 1
    counter = 0
    while current_tile == 4:
        if counter == 0:
            print(you_can + directions[0] + '.')
        ask_user = input('Direction: ')
        if ask_user.lower() == 'n':
            current_tile = 5
            break
        else:
            print(not_valid)
        counter += 1
    counter = 0
    while current_tile == 5:
        if counter == 0:
            print(you_can + directions[2] + ' or ' + directions[3] + '.')
        ask_user = input('Direction: ')
        if ask_user.lower() == 's':
            current_tile = 4
            break
        elif ask_user.lower() == 'w':
            current_tile = 2
            break
        else:
            print(not_valid)
        counter += 1
    counter = 0
    while current_tile == 6:
        if counter == 0:
            print(you_can + directions[1] + ' or ' + directions[3] + '.')
        ask_user = input('Direction: ')
        if ask_user.lower() == 'e':
            current_tile = 9
            break
        elif ask_user.lower() == 'w':
            current_tile = 3
            break
        else:
            print(not_valid)
        counter += 1
    counter = 0
    while current_tile == 8:
        if counter == 0:
            print(you_can + directions[0] + ' or ' + directions[2] + '.')
        ask_user = input('Direction: ')
        if ask_user.lower() == 's':
            current_tile = 7
            break
        elif ask_user.lower() == 'n':
            current_tile = 9
            break
        else:
            print(not_valid)
        counter += 1
    counter = 0
    while current_tile == 9:
        if counter == 0:
            print(you_can + directions[2] + ' or ' + directions[3] + '.')
        ask_user = input('Direction: ')
        if ask_user.lower() == 's':
            current_tile = 8
            break
        elif ask_user.lower() == 'w':
            current_tile = 6
            break
        else:
            print(not_valid)
        counter += 1
    counter = 0
    if current_tile == 7:
        print('Victory!')
        break