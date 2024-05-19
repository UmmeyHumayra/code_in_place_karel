"""
Instructions
In Code in Place we are all about building technology to help folks learn. Now it is your turn. Implement Khansole Academy—a program that helps other people learn addition! Write a program that randomly generates a simple addition problem for the user, reads in the answer from the user, and then checks to see if they got it right or wrong.
More specifically, your program should be able to generate simple addition problems that involve adding two 2-digit integers (i.e., the numbers 10 through 99). The user should be asked for an answer to the generated problem. Your program should determine if the answer was correct or not, and give the user an appropriate message to let them know.

A sample run of the program is shown below (user input is in blue for visual clarity):
Khansole Academy
What is 51 + 79?
Your answer: 120
Incorrect.
The expected answer is 130

Here's another sample run, where the user gets the question correct (user input is in blue):
Khansole Academy
What is 55 + 11?
Your answer: 66
Correct!

When you have decided that your program works as intended, hit Check Correct.

Optional Extension
If you're up for it, we can make Khansole Academy an even better learning tool. Be creative! We recommend you start with the "three in a row" extension first, then come up with your own :-).

Three in a row

In the previous milestone you wrote code to randomly generate one addition problem at a time and tell the user if they got it right or not. In this milestone, you should randomly generate addition problems until the user has gotten 3 problems correct in a row. (Note: the number of problems the user needs to get correctly in a row to complete the program is just one example of a good place to specify a constant in your program).

You should be able to use a lot of your code from the previous milestone to help out here!
A sample run of the program is shown below (user input is in blue).
Khansole Academy
What is 51 + 79? 
Your answer: 120 
Incorrect. 
The expected answer is 130 

What is 33 + 19? 
Your answer: 42 
Incorrect. 
The expected answer is 52 

What is 55 + 11? 
Your answer: 66 
Correct! 
You've gotten 1 correct in a row. 

What is 84 + 25? 
Your answer: 109 
Correct! 
You've gotten 2 correct in a row. 

What is 26 + 58? 
Your answer: 74 
Incorrect. 
The expected answer is 84 

What is 98 + 85? 
Your answer: 183 
Correct! 
You've gotten 1 correct in a row. 

What is 79 + 66? 
Your answer: 145 
Correct! 
You've gotten 2 correct in a row. 

What is 97 + 20? 
Your answer: 117 
Correct! 
You've gotten 3 correct in a row. 

Congratulations! You mastered addition.

As a side note, one of the earliest programs Mehran wrote (with his friend Matthew) when he was first learning how to program was very similar to Khansole Academy. It was called “M&M’s Math Puzzles.” It was written in a language named BASIC on a computer that had 4K of memory (that’s 4 Kilobytes) and used cassette tapes (the same kind used for music in the 1970’s) to store information. Yeah, Mehran is old.

Beyond addition?
There is no limit to how awesome you can make your learning software. Can you get it to teach? Can you get it to offer problems other than addition? Get creative! Have fun!
"""

import random

CORRECT_IN_A_ROW = 3

def main():
    print("Khansole Academy")
    print("Complete learning by getting 3 correct answers in a row.") 
    user_score = 0
    select_operation = 0 # to randomly select which operation to perform i.e. (+, -, *, /)
    while user_score < 3:
        num1 = random.randint(10,99)
        num2 = random.randint(10,99)
        select_operation = random.randint (1,4)

        ### This section selects the operation and takes user input
        if select_operation ==1: # 1 for addition
            result = num1+num2
            print ("what is", num1, "+", num2, "?")
            user_answer = int (input("Your answer: "))
        elif select_operation ==2: # 2 for subtraction
            result = num1-num2
            print ("what is", num1, "-", num2, "?")
            user_answer = int (input("Your answer: "))
        elif select_operation ==3: # 3 for multiplication
            result = num1*num2
            print ("what is", num1, "*", num2, "?")
            user_answer = int (input("Your answer: "))
        elif select_operation ==4:# 4 for division
            result = num1//num2
            print ("what is", num1, "/", num2, " to the whole number?")
            user_answer = int (input("Your answer: "))
        
        # This section checks user result. For 3 consecutive correct answer the program completes execution
        if user_answer == result:
            print ("Correct!")
            user_score += 1
            print ("You've gotten", user_score, "correct in a row.")
            print(' ')
        else: 
            print ("Incorrect.")
            print ("The expected answer is", result)
            user_score = 0
            print(' ')
    print("Congratulations! You mastered addition, subtraction, multiplication and division!")
    
if __name__ == '__main__':
    main()
