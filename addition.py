
# Stephen Buchanan, Benjamin Mazur, Section 20L, 10/12/13
# Program 1

# Program 6-13

#imporing libraries
from cisc106_32 import*
import random


# seting a globle variable for Random Number
RANDOM_NUMBER1 = random.randint(1, 100)
RANDOM_NUMBER2 = random.randint(1, 100)

# Choices for the Menu 
ADDITION = "a"
SUBTRACTION = "s"
MULTIPLICATION = "m"
DIVISION = "d"
EXPONENTIATION = "e"
QUIT_PROGRAM = "q"
# The operation functions

def Addition():

    print("\nYou have selected addition \n")

    for number_of_problems in range(0,5,1):

        first = random.randint(1, 100)
        second = random.randint(1, 100)
        
        add = first + second
        
        print("How much is", first," plus ", second, "?")
        input_answer = int(input())
                
        while (input_answer != add) and number_of_answers => 3 :                
    
            print("Incorrect, please try again: \n")

            print("How much is", first," plus ", second, "?")
            input_answer = int(input())

             
        if input_answer != add:
                print("\tSorry, you missed this one. The correct answer is",add, ".\n ")
        else:
                print("\tCorrect!\n")
                

        input("Please press enter for another question \n")
        
    print("You have completed all 4 practice problems for this section. Redirecting you back to the main menu.\n")
    input("Please press enter to select another operation\n")
    #return(Main_Body_Function())

Addition()
