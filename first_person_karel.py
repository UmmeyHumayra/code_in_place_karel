"""
Write a program that lets you play Karel in a rectangular world (moving and turning left and not walking off of the world, all that good stuff)!
Have you ever wanted to be Karel, wandering about a nice rectangular world, not a worry in the world, just moving and turning left whenever you'd like? You can emulate this feeling by writing a console-based first person Karel program! For simplicity, assume that beepers and painting are out of the question, and the world has no walls. All you should implement is moving and turning left. Store the number of columns and rows in your "world" as constants, and assume you start in row 1 column 1 facing East. Prompt the user for an action ("move" or "turn left" until they press enter without typing anything, in which case the result of input() will be an empty string, and you can stop looping).
Recall that you can only move if you're not about to move off of the world! This means you can only move in the following cases:
  facing East and current column is less than the number of columns (move right)
  facing West and current column is greater than 1 (move left)
  facing North and current row is less than the number of rows (move up)
  facing South and current row is greater than 1 (move down)
Here's what turning left does to the direction you (Karel) are facing:
  if you're facing East, turning left will make you face North
  if you're facing North, turning left will make you face West
  if you're facing West, turning left will make you face South
  if you're facing South, turning left will make you face East

Here's a sample run of the program (user input is in blue):
Welcome to first person Karel. You're at row 1, column 1, facing East (facing column 3) 
What would you like to do? You can move and turn left. Press enter to finish. move 
You moved one step forward and now you're at row 1 column 2 
What would you like to do? You can move and turn left. Press enter to finish. turn left 
You turned left and are now facing North. 
What would you like to do? You can move and turn left. Press enter to finish. turn left 
You turned left and are now facing West. 
What would you like to do? You can move and turn left. Press enter to finish. move 
You moved one step forward and now you're at row 1 column 1. 
What would you like to do? You can move and turn left. Press enter to finish. move 
You can't move forward! 
What would you like to do? You can move and turn left. Press enter to finish. 
You've ended up at row 1 and column 1 facing West.

This may be a confusing problem (it's certainly a pretty big problem)! If you'd like a hint about how to get started, scroll down and keep reading (though we recommend you give it your best shot first!). If you're feeling good, stop reading right here and go right ahead!

As a hint, this is what the beginning of our solution code looks like:

N_COLS = 3 # Notice these constants! 
N_ROWS = 3 
def main(): 
    print("Welcome to first person Karel! You're at row 1, column 1, facing East (facing column " + str(N_COLS) + ")")
    facing_direction = 'East'  # This variable will keep track of the way Karel is facing -- it changes if the user says to "turn left"!
    curr_col = 1  # This variable ...
    curr_row = 1  # ... and this one keep track of Karel's position in the world! They may change if the user says to "move"
    action = input("What would you like to do? You can move and turn left. Press enter to finish. ")
    # ... more code! There's a while loop that starts on this line, but our hint ends here :^)
"""

"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""
WORLD_ROW_NUM = 3
WORLD_COL_NUM = 3

def main():
    user_row = 1
    user_column = 1
    direction = "East"
    print ("Welcome to first person Karel! You're at row 1, column 1, facing East (facing column 3)")
    user_action = input("What would you like to do? You can move and turn left. Press enter to finish. ")
    while (user_action !=""):
      # I could reorganize / pretty_print the code by splitting the if condition
        if (user_action=="move") and (direction=="East" and user_column<WORLD_COL_NUM): 
            #move right
            user_column = user_column +1
            print("You moved one step forward and now you're at row", user_row, "column", user_column, ".") 
            user_action = input("What would you like to do? You can move and turn left. Press enter to finish. ")

        elif (user_action=="move") and (direction=="West" and user_column>1):
            #move left
            user_column = user_column - 1
            print("You moved one step forward and now you're at row", user_row, "column", user_column, ".")
            user_action = input("What would you like to do? You can move and turn left. Press enter to finish. ")
            
        elif (user_action=="move") and (direction=="North" and user_row<WORLD_ROW_NUM): 
            #move up
            user_row = user_row + 1
            print("You moved one step forward and now you're at row", user_row, "column", user_column, ".") 
            user_action = input("What would you like to do? You can move and turn left. Press enter to finish. ")
            
        elif (user_action=="move") and (direction=="South" and user_row>1):
            #move down
            user_row = user_row - 1
            print("You moved one step forward and now you're at row", user_row, "column", user_column, ".")
            user_action = input("What would you like to do? You can move and turn left. Press enter to finish. ")

        elif (user_action=="turn left") and (direction=="East"):
            direction = "North"
            print ("You turned left and are now facing", direction, ".")
            user_action = input("What would you like to do? You can move and turn left. Press enter to finish. ")
        
        elif (user_action=="turn left") and (direction=="North"):
            direction = "West"
            print ("You turned left and are now facing", direction, ".")
            user_action = input("What would you like to do? You can move and turn left. Press enter to finish. ")
        
        elif (user_action=="turn left") and (direction=="West"):
            direction = "South"
            print ("You turned left and are now facing", direction, ".")
            user_action = input("What would you like to do? You can move and turn left. Press enter to finish. ")
        
        elif (user_action=="turn left") and (direction=="South"):
            direction = "East"
            print ("You turned left and are now facing", direction, ".")
            user_action = input("What would you like to do? You can move and turn left. Press enter to finish. ")
        
        else: 
            print ("You can't move forward!")
            user_action = input("What would you like to do? You can move and turn left. Press enter to finish. ")   
  
    print("You've ended up at row", user_row, "and column", user_column, "facing", direction, ".")

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
