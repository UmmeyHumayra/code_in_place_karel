"""
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
"""

from graphics import Canvas
import random
import time

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14      # The number of bricks in the base
COLORS = ["red", "orange", "yellow", "green", "blue", "violet", ]

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_base_brick_row (canvas, BRICKS_IN_BASE)
    # for next row, the number of bricks will be BRICKS_IN_BASE - 1
    #Count variable keeps track of the number of bricks that needs to be decreased while going up the rows in pyramid
    count = 1
    for bricks in range (BRICKS_IN_BASE-1):
        bricks_in_row = BRICKS_IN_BASE - count
        draw_next_brick_row (canvas, bricks_in_row, count)
        count +=1 


def draw_base_brick_row(canvas, BRICKS_IN_BASE):
    for i in range (BRICKS_IN_BASE): 
        start_x = CANVAS_WIDTH/2 - (BRICKS_IN_BASE/2)*BRICK_WIDTH + i*BRICK_WIDTH
        start_y = CANVAS_HEIGHT - BRICK_HEIGHT
        end_x = start_x + BRICK_WIDTH
        end_y = start_y + BRICK_HEIGHT
        color = random.choice(COLORS)

        canvas.create_rectangle(start_x, start_y, end_x, end_y, color, 'black')
        #canvas.wait_for_click()
        #time.sleep(0.02)
        

def draw_next_brick_row(canvas, bricks_in_row, count):
    for i in range (bricks_in_row): 
        start_x = CANVAS_WIDTH/2 - (bricks_in_row/2)*BRICK_WIDTH + i*BRICK_WIDTH
        start_y = CANVAS_HEIGHT - (count+1)*BRICK_HEIGHT
        end_x = start_x + BRICK_WIDTH
        end_y = start_y + BRICK_HEIGHT
        color = random.choice(COLORS)

        canvas.create_rectangle(start_x, start_y, end_x, end_y, color, 'black')
        #canvas.wait_for_click()
        #time.sleep(0.02)
  

if __name__ == '__main__':
    main()
