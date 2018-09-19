# Lists of direction options
directions = ['(N)orth', '(E)ast', '(S)outh' , '(W)est']
directions_short = ['n', 'e', 's' , 'w']

'''
    Github project location:
    https://github.com/HerGisl/TileTraveller
1. Which implementation was easier and why?
    The implementation with the use of functions. Changing the
    behaviour of the program is way easier, since all the steps in
    the game share the same functionality. 
2. Which implementation is more readable and why?
    Again - the implementaion that uses functions, because 
    each step has a set of options and the the functinality of the 
    program can be traced through the functions.
    I have to admit that the use of nested lists could be
    could be clearer though.
3. Which problems in the first implementations were you able to solve with the latter
implementation?
    In my mind, the separation of the steps/options and functionality was the 
    biggest problem that the later implementation solved with functions.
    ----------
    We list up the 3x3 grid in such way
    that each tile is a list that contains
    two lists:
        a) one that contains direction 
            options in regards to the direction list
        b) one that contains which tile numbers each 
            direction leads to.
    
    The tiles are referenced in order shown below:       
        
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
        [0,1,2], [2, 4, 0]
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
        [1,3], [8,2]
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
'''
    Function that returns direction options, 
    given a parameter that contains indexes
    in regards to the list directions.
'''
def direction_options(options):
    counter = 0
    string_return = ''
    for i in options:
        if counter != 0:
            string_return += ' or '
        string_return += directions[i]
        counter += 1
    return string_return

''' 
    Function that asks user for input, and compares
    given value to the direction list and direction_options 
    list argument.
    If valid user input is given, the index from that value
    in the direction_options list argument is found, and 
    the value from location_options list argument passed
    to the print_location_options function, therby
    changing the current location of the player.
'''
def get_user_input(direction_options, location_options):
    run_while = True
    while run_while:
        user_input = input('Direction: ')
        if user_input.lower() in directions_short and directions_short.index(user_input.lower()) in direction_options:
            print_location_options(location_options[direction_options.index(directions_short.index(user_input.lower()))])
            run_while = False
        else:
            print('Not a valid direction!')

'''
    The main function that prints out a tile direction
    options (calls the direction_option function)
    and asks the user for input (get_user_input) for 
    the given tile number.
    If the tile does not contain any information
    in the location_list, the victory tile has
    been found so the user is notified and
    the program stops executing.
'''
def print_location_options(tile_number):
    if not location_list[tile_number][0]:
        print('Victory!')
    else:
        print('You can travel: ' + direction_options(location_list[tile_number][0]) + '.')
        get_user_input(location_list[tile_number][0], location_list[tile_number][1])

# Starts the game at tile number 0
print_location_options(0)