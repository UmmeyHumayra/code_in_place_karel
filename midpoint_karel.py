"""
As an exercise in solving algorithmic problems, you will program to find the midpoint of 1st Street. Say Karel starts in the 5x5 world. Karel should end in the center of 1st row.
Note that the final configuration of the world should have only a single beeper at the midpoint of the 1st row. Along the way, Karel is allowed to place additional beepers wherever it wants to, but must pick them all up again before it finishes. Similarly, if Karel paints/colors any of the corners in the world, they must all be uncolored before Karel finishes.

In solving this problem, you may count on the following facts about the world:
Karel starts at bottom left corner of the world, facing east.
The initial state of the world includes no interior walls or beepers.
The world need not be square, but you may assume that it is at least as tall as it is wide.
If the width of the world is odd, Karel must put the beeper in the center square. If the width is even, Karel must drop a beeper on the left most of the two squares.
There are many different algorithms you can use to solve this problem so feel free to be creative!
You should design your program to run successfully in all possible worlds.
"""

from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""

def main():
    turn_left() # karel faces north/up
    two_step_up()
    climb_down()
    plant_beeper()

def two_step_up():
    """
    this function will help karel to find the midpoint 
    by going two step up and one step to the right
    pre: karel is facing north
    post: karel is at top row facing north
    """
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            turn_right()
            move()
            turn_left()

def climb_down():
    """
    karel will climb down from the midpoint on top row to
    the midpoint on bottom row
    pre: karel is at top row facing north
    post: karel is at bottom row facing south
    """
    turn_around()
    move_to_wall()

def plant_beeper():
    """
    karel puts the beeper and set to end position
    pre: karel at bottom row faces south
    post: karel sits on a beeper and faces east
    """
    put_beeper()
    turn_left()

def move_to_wall():
    """
    pre: karel will move forward until blocked by wall
    post: karel is facing wall 
    """
    while front_is_clear():
            move()

def turn_right():
    for i in range (3):
        turn_left()

def turn_around():
    for i in range (2):
        turn_left()

if __name__ == '__main__':
    main()
