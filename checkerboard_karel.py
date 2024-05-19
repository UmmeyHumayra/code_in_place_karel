"""
Warning: this is really hard to get perfect!
Get Karel to create a checkerboard pattern of beepers inside an empty rectangular world, as illustrated below:
Note: Karel should end up where she starts
As you think about how you will solve the problem, you should make sure that your solution works with checkerboards that are different in size from the standard 6x6 checkerboard shown in the example above. Some examples of such cases are discussed below. Odd-sized checkerboards are tricky, and you should make sure that your program generates the following pattern in a 5x3 world:
This problem is hard: Try simplifying your solution with decomposition. Can you checker a single row/column? Make the row/column work for different widths/heights? Once you've finished a single row/column, can you make Karel fill two? Three? All of them? Incrementally developing your program in stages helps break it down into simpler parts and is a wise strategy for attacking hard programming problems.
world sizes: 6x6 , 3x5, 3x1
"""

from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.

Steps: 
# Karel makes checker pattern from first cell: 
    ## faces up
    ## makes checker pattern in a column while climbing up
    ## climbs down the row
# If front clear karel moves one step forward and up
# Karel repeats making checker pattern from first cell until hits the end of the world
# Karel returns to end position
"""

def main():
    checker_column_from_first_cell()
    while front_is_clear():
        move_one_step_forward_and_up()
        #make karel start creating checker from the second cell of the column
        checker_column_from_first_cell()
        if front_is_clear():
            move()
            # make karel start creating checker from the first cell of the column
            checker_column_from_first_cell()
    return_to_end_position()

def checker_column_from_first_cell():
    """
    Karel will make a checker column
    pre: karel is at the bottom of the column
    post: karel has made checker pattern and climbed down to the bottom of the column facing east
    """
    face_north()
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    turn_around()
    climb_down()

def move_one_step_forward_and_up():
    """
    Karel moves 1 step forward and 1 step up
    pre: karel is facing open direction
    post: karel moved 1 step forward and 1 step up facing north
    """
    move()
    turn_left()
    move()


def climb_down():
    """
    pre: karel is at the top of the column facing south
    post: karel is at the bottom of the column facing east 
    """
    move_to_wall()
    turn_left()

def return_to_end_position():
    """
    karel has completed making a checkerboard
    pre: karel is at the bottom of last column facing east
    post: karel is the bottom of the first column facing east
    """
    turn_around()
    move_to_wall()
    turn_around()

def move_to_wall():
        while front_is_clear():
            move()

def face_north(): 
    while not_facing_north():
        turn_left()

def turn_around():
    for i in range (2):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
