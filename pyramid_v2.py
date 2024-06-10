'''
Instructions
Write a program that draws a pyramid consisting of bricks arranged in horizontal rows, so that the number of bricks in each row decreases by one as you move up the pyramid. A sample run is shown below.
The pyramid should be centered at the bottom of the drawing canvas and should use constants for the following values:
BRICK_WIDTH The width of each brick (30 pixels) 
BRICK_HEIGHT The height of each brick (12 pixels) 
BRICKS_IN_BASE The number of bricks in the base (14)
Note: If you're using a screen reader, you may want to start with a smaller pyramid (smaller BRICKS_IN_BASE) for easier debugging.
You should write your program so that, if the constant values were different, the pyramid drawn would reflect the values in those constants (i.e., brick sizes or the number of bricks in the base could be different).
The bricks can be any color you like. Here is an example of drawing a single yellow brick in the top left corner of the canvas:
canvas.create_rectangle(
    0, 0, 
    BRICK_WIDTH, BRICK_HEIGHT, 
    "yellow", "black"
)
'''
from graphics import Canvas
import random
import time

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 12      # The number of bricks in the base
canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
COLORS = ["red", "orange", "yellow", "green", "blue", "violet", ]

def main(): 
    y_space = CANVAS_HEIGHT - BRICK_HEIGHT * BRICKS_IN_BASE
    for i in range (BRICKS_IN_BASE):
        for j in range (i+1):
            x_space = (CANVAS_WIDTH - (BRICK_WIDTH * (i+1)))/2
            start_x = x_space + j*BRICK_WIDTH
            start_y = y_space + i*BRICK_HEIGHT
            draw_brick(start_x, start_y)
            #print (i, j, start_x)

def draw_brick(x, y):
    canvas.create_rectangle (
        x, y, 
        x+BRICK_WIDTH, y+BRICK_HEIGHT,
        random.choice(COLORS),
        'black'
    )

if __name__ == '__main__':
    main()
