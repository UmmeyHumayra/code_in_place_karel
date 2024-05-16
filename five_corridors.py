"""
Karel will begin in the bottom left corner of a world with 5 "corridors", some of which have beepers at the end of them and some of which are empty, like so:

Get Karel to traverse each corridor (essentially, each row, until a wall blocks her path). At the end of each corridor (they may be different lengths!), if a beeper isn't already there, put a beeper down. Karel should end up at the beginning of the topmost corridor (highest row number), and each corridor should have a beeper at the end of it, like so:
"""

from karel.stanfordkarel import *

def main():
    """
    Traverses 5 variable length corridors and place beepers at the ends of 
    them if there aren't already beepers there.
    """
    for i in range (5):
        traverse_a_row()

def traverse_a_row():
    """
    karel traverses a row and puts beeper on the right most cell of the 
    corridor if one doesn't exist already and comes back to the starting of the corridor
    pre: karel is at the start of the corridor
    post: karel is back at the starting cell of the corridor facing north
    """
    if not_facing_east():
        turn_left()
    move_to_wall()
    beeper_in_last_cell()
    reset_post()
    if right_is_clear():
        turn_right()

def beeper_in_last_cell():
    """
    this function allows karel to check whether there's any beeper
    in the last cell of the row. if not, it puts a beeper
    pre: karel is at the last cell facing wall
    post: karel is sitting on a beeper
    """
    if no_beepers_present(): 
        put_beeper()

def reset_post():
    """
    This function will make karel to get back to the left of each row
    pre: karel is at the right side of row facing wall
    post: karel is back at the left of the row and moves one step forward facing north
    """
    turn_around()
    move_to_wall()
    turn_right()
    if front_is_clear():
        move()


def move_to_wall(): 
    """
    Karel moves forward until it hits the wall
    pre: karel is facing east and front is clear
    post: karel is facing east and front is blocked
    """
    while front_is_clear():
        move()

def turn_around():
    for i in range (2):
        turn_left()

def turn_right():
    for i in range (3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
