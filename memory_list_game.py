'''
Instructions
Write a program that has a user play a memory game using lists. 
This Python programming assignment will guide you through the exciting process of creating your own memory game, a classic and engaging exercise that tests your ability to remember and match pairs of items. In this game the cards will be represented as numbers in a list and their location will be indices of the list. By completing this project, you will practice critical list concepts. Not only will this enhance your problem-solving skills, but you will also have a lot of fun as you watch the game come to life and challenge yourself or your friends to find all the pairs.

Milestone #1: Create the truth list.
Use a for loop to create a list that has the values  0  through  N_PAIRS - 1  twice. So for example if  NUM_PAIRS = 3 as in the example, your list should have this value:
[0, 0, 1, 1, 2, 2]

Milestone #2: Shuffle the list. 
The python random library has a special function called shuffle which will randomly order the values in a list. Call that function on your list and then print out the result. Print out the list to make sure it looks shuffled! Assuming that your list from the previous milestone was named truth
random.shuffle(truth)
print(truth)

Milestone #3: Create a displayed list
In this program you will need to keep track of a separate list, which is the one to display to the user. We use the '*' symbol to denote that a value is hidden to the user (otherwise we display the value). Initially displayed should be a list of '*' values which is the same length as truth. If  NUM_PAIRS = 3:
['*', '*', '*', '*', '*', '*']

Milestone #4: Get a valid index from the user
Write logic to get a valid index from the user. A valid index must be greater than or equal to 0, it must be less than or equal to the index of the last element in the list. It also must be one where the value of the displayed list at that index must be '*' (otherwise it is an index which has already been guessed). If the user does not enter a valid index, ask them to give you a new index. We recommend that you define a new function get_valid_index which takes in the displayed list and returns the valid index the user entered.

Here are specific strings we are expecting for you to print out when the user doesn't enter a valid index:
Entering the same index twice
"You entered the same index twice. Try again."

Number is out-of-bounds
"Invalid index. Try again."

Non-number.
"Not a number. Try again."

Inputting an index that has already been revealed
"This number has already been matched. Try again."

Milestone #5: Check correct.
Get two valid inputs from the user and check if there is a match. If there is a match, you should reveal those values in the displayed list. Otherwise, if the values don't match, you should tell the user the values, but do not update the displayed list. Of course, you should first make sure the user didn't enter the same index twice. Here are a few examples. Imagine the current value of displayed and truth lists are as follows:
[2, 1, 1, 2, 0, 0] # truth_list
['*', '*', '*', '*', 0, 0] # displayed_list
Here is an example turn where the user does not get a match (user input is in blue):
['*', '*', '*', '*', 0, 0]
Enter an index: 0
Enter an index: 1
Value at index 0 is 2
Value at index 1 is 1
No match. Try again. 
Press Enter to continue... 

Here is an example turn where the user does get a match (user input is in blue):
['*', '*', '*', '*', 0, 0]
Enter an index: 0
Enter an index: 3
Match!

Since the user got a match the display list will be updated to [2, '*', '*', 2, 0, 0]

Milestone #6: Play multiple turns.
The user should play until all the pairs have been correctly located. Between turns make sure to call clear_terminal. At the end of the game, tell the user that they have won by printing something like 'Congratulations! You won!'
'''
'''
steps:
1. Create the truth_list using for loop and NUM_PAIRS as the range
2. Call the random shuffle function on the truth_list
3. Create a displayed_list by displaying '*' for each item in truth_list
4. helper function to get one valid index. order of conditions to check: 
    # non-number
    # Number is out-of-bounds
    # Inputting an index that has already been revealed
5. helper function to get 2 indices, and make sure that the user didn't enter the same index twice
6. check if the numbers at user_input indices matches or not. Print message accordingly and update & return displayed_list.
7. in the main function loop the get indices function and check match function until there's no "*" left
8. insert clear terminal function  
'''

import random

NUM_PAIRS = 5

def main():
    truth_list = create_truth_list()
    random.shuffle(truth_list)
    displayed_list = create_displayed_list(truth_list)
    
    while '*' in displayed_list:
        print (displayed_list)
        first_index, second_index = get_two_valid_indices(displayed_list) 
        check_if_numbers_match(first_index, second_index, truth_list, displayed_list)

    print("Congratulations! You won!")

def check_if_numbers_match(first_index, second_index, truth_list, displayed_list):
    if truth_list[first_index] == truth_list [second_index]:
        displayed_list [first_index] = truth_list [first_index]
        displayed_list [second_index] = truth_list [second_index]
        print ("Match!")
        
    elif truth_list[first_index] != truth_list [second_index]:
        print("Value at index " + str(first_index)+ " is " + str(truth_list[first_index]))
        print("Value at index " + str(second_index)+ " is " + str(truth_list[second_index]))
        print("No match. Try again.")
        input("Press Enter to continue...")

    clear_terminal()
    return (displayed_list)

def get_two_valid_indices(displayed_list):
    index1 = get_a_valid_index(displayed_list)
    index2 = get_a_valid_index(displayed_list)
    while index2 == index1:
        print("You entered the same index twice. Try again.")
        index2 = get_a_valid_index(displayed_list)   
    return (index1, index2)

def get_a_valid_index(displayed_list):
    while True:
        user_input =input("Enter an index: ")
        if not user_input.isdigit():
            print("Not a number. Try again.")
            continue
        
        if int(user_input) > len(displayed_list):
            print ("Invalid index. Try again.")
            continue 

        if not displayed_list[int(user_input)] == "*": 
            print ("This number has already been matched. Try again.")
            continue
        break

    return (int(user_input))


def create_displayed_list(truth_list):
    displayed_list = []
    for i in range (len(truth_list)):
        displayed_list.append("*")
    return displayed_list


def create_truth_list():
    truth_list = []
    for i in range (NUM_PAIRS):
        truth_list.append(i)
    return (2*truth_list)


def clear_terminal():
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()
