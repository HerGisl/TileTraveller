current_tile = 1
game_over = False
not_valid = 'Not a valid direction!'

directions = ['(N)orth', '(S)outh', '(E)ast', '(W)est']



you_can = 'You can travel: '

while game_over == False:
    while current_tile == 1:
        ask_user = input(you_can + directions[0] + '.')
        if ask_user.lower() == 'n':
            current_tile = 2
        else:
            print(not_valid)
    while current_tile == 2:
        ask_user = input(you_can + directions[0] + ' or ' + directions[2] + ' or ' + directions[1] + '.')
        if ask_user.lower() == 'n':
            current_tile = 3
        elif ask_user.lower() == 's':
            current_tile = 1
        elif ask_user.lower() == 'e':
            current_tile = 5
        else:
            print(not_valid)
