
directions = ['(N)orth', '(E)ast', '(S)outh' , '(W)est']
directions_short = ['n', 'e', 's' , 'w']

'''
    listum upp 3x3 griddið
    þannig að hver reitur sé listi sem 
    inniheldur tvo lista, einn yfir möguleika
    og anna sem inniheldur næsta reit.
    2   5   8
    1   4   7
    0   3   6
'''

location_list = [
    [
        #Tile 0
        [0], [1]
    ],
    [
        #Tile 1
        [0,1,2], [0, 4, 2]
    ],
    [
        #Tile 2
        [1,2], [5, 1]
    ],
    [
        #Tile 3
        [0], [4]
    ],
    [
        #Tile 4
        [2,3], [3,1]
    ],
    [
        #Tile 5
        [1,3], [8,3]
    ],
    [
        #Tile 6
        [], []
    ],
    [
        #Tile 7
        [0,2], [8, 6]
    ],
    [
        #Tile 8
        [2,3], [7, 5]
    ]
]

def direction_options(options):
    counter = 0
    string_return = ''
    for i in options:
        if counter != 0:
            string_return += ', '
        string_return += directions[i]
        counter += 1
    return string_return
            
def get_user_input(options, location_option):
    run_while = True
    while run_while:
        user_input = input('Direction: ')
        if user_input in directions_short and directions_short.index(user_input) in options:
            print_location_options( )

            run_while = False
        else:
            print('No!')
    


def print_location_options(location_id):
    print('You can travel: ' + direction_options(location_list[location_id][0]) + '.')
    get_user_input(location_list[location_id][0], location_list[location_id][1])

print_location_options(0)