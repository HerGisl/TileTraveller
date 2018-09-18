'''
Algorithmi fyrir 3x3 grid leik
Búa til lúppu og harðkóða núverandi staðsettningu og möguleika í hverju skrefi.
Prufa ef input matchar við möguleika og breyta núverandi staðsettningu miðað við það.
'''
# argargarg

current_tile = 1
game_over = False
not_valid = 'Not a valid direction!'

directions = ['(N)orth', '(E)ast', '(S)outh' , '(W)est']



you_can = 'You can travel: '

while game_over == False:
    while current_tile == 1:

        ask_user = input(you_can + directions[0] + '.')
        if ask_user.lower() == 'n':
            print('Direction: ' + ask_user)
            current_tile = 2
        else:
            print(not_valid)
    while current_tile == 2:

        ask_user = input(you_can + directions[0] + ' or ' + directions[1] + ' or ' + directions[2] + '.')
        if ask_user.lower() == 'n':
            print('Direction: ' + ask_user)
            current_tile = 3
        elif ask_user.lower() == 's':
            print('Direction: ' + ask_user)
            current_tile = 1
        elif ask_user.lower() == 'e':
            print('Direction: ' + ask_user)
            current_tile = 5
        else:
            print(not_valid)
    while current_tile == 3:

        ask_user = input(you_can + directions[1] + ' or ' + directions[2] + '.')
        if ask_user.lower() == 's':
            print('Direction: ' + ask_user)
            current_tile = 2
        elif ask_user.lower() == 'e':
            print('Direction: ' + ask_user)
            current_tile = 6
        else:
            print(not_valid)
    while current_tile == 4:

        ask_user = input(you_can + directions[0] + '.')
        if ask_user.lower() == 'n':
            print('Direction: ' + ask_user)
            current_tile = 5
        else:
            print(not_valid)
    while current_tile == 5:

        ask_user = input(you_can + directions[2] + ' or ' + directions[3] + '.')
        if ask_user.lower() == 's':
            print('Direction: ' + ask_user)
            current_tile = 4
        elif ask_user.lower() == 'w':
            print('Direction: ' + ask_user)
            current_tile = 2
        else:
            print(not_valid)
    while current_tile == 6:

        ask_user = input(you_can + directions[1] + ' or ' + directions[3] + '.')
        if ask_user.lower() == 'e':
            print('Direction: ' + ask_user)
            current_tile = 9
        elif ask_user.lower() == 'w':
            print('Direction: ' + ask_user)
            current_tile = 3
        else:
            print(not_valid)
    while current_tile == 8:
        print('location ' + str(current_tile))
        ask_user = input(you_can + directions[0] + ' or ' + directions[2] + '.')
        if ask_user.lower() == 's':
            print('Direction: ' + ask_user)
            current_tile = 7
        elif ask_user.lower() == 'n':
            print('Direction: ' + ask_user)
            current_tile = 9
        else:
            print(not_valid)
    while current_tile == 9:
        ask_user = input(you_can + directions[2] + ' or ' + directions[3] + '.')
        if ask_user.lower() == 's':
            print('Direction: ' + ask_user)
            current_tile = 8
        elif ask_user.lower() == 'w':
            print('Direction: ' + ask_user)
            current_tile = 6
        else:
            print(not_valid)
    if current_tile == 7:
        print('Victory!')
        break