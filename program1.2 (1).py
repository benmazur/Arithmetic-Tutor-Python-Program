
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

    for number_of_problems in range(0,4,1):

        first = random.randint(1, 100)
        second = random.randint(1, 100)
        
        add = first + second
        
        print("How much is", first," plus ", second, "?")
        input_answer = int(input())
                                     
        if (input_answer == add):
            print("\tCorrect!")
            
        if ( input_answer != add):
        
            for number_of_answer in range(1,3,1):                
  
                if ( input_answer != add):
                    print("Incorrect, please try again: \n")
                    print("How much is", first," plus ", second, "?")
                    input_answer = int(input())

                elif (input_answer == add):
                    print("\tCorrect!\n")

            if input_answer != add:
                print("\tSorry, you missed this one. The correct answer is",add, ".\n ")
            else:
                print("\tCorrect!\n")
                

        input("Please press enter for another question \n")
        
    print("You have completed all 4 practice problems for this section. Redirecting you back to the main menu.\n")
    input("Please press enter to select another operation\n")
    return(Main_Body_Function())



# The Function for subtraction    
def Subtraction():

    print("\nYou have selected subtraction \n")
    
    for number_of_problems in range(0,4,1):

        first = random.randint(1, 100)
        second = random.randint(1, 100)

       
        subtract = first - second
        
        print("How much is", first," minus ", second, "?")
        input_answer = int(input())
                                     
        if (input_answer == subtract):
            print("\tCorrect!")
            
        if ( input_answer != subtract):
        
            for number_of_answer in range(1,3,1):                
  
                if ( input_answer != subtract):
                    print("Incorrect, please try again: \n")
                    print("How much is", first," minus ", second, "?")
                    input_answer = int(input())

                elif (input_answer == subtract):
                    print("\tCorrect!\n")

            if input_answer != subtract:
                print("\tSorry, you missed this one. The correct answer is", subtract, ".\n ")
            else:
                print("\tCorrect!\n")
                

        input("Please press enter for another question \n")
        
    print("You have completed all 4 practice problems for this section. Redirecting you back to the main menu.\n")
    input("Please press enter to select another operation\n")
    return(Main_Body_Function())


#The Function for Multiplication
def Multiplication():

    print("\nYou have selected multiplication \n")

    for number_of_problems in range(0,4,1):

        first = random.randint(1, 100)
        second = random.randint(1, 100)
        
        multiply = first * second
        
        print("How much is", first," times ", second, "?")
        input_answer = int(input())
                                     
        if (input_answer == multiply):
            print("\tCorrect!")
            
        if ( input_answer != multiply):
        
            for number_of_answer in range(1,3,1):                
  
                if ( input_answer != multiply):
                    print("Incorrect, please try again: \n")
                    print("How much is", first," times ", second, "?")
                    input_answer = int(input())

                elif (input_answer == multiply):
                    print("\tCorrect!\n")

            if input_answer != multiply:
                print("\tSorry, you missed this one. The correct answer is", multiply , ".\n ")
            else:
                print("\tCorrect!\n")
                

        input("Please press enter for another question \n")
        
    print("You have completed all 4 practice problems for this section. Redirecting you back to the main menu.\n")
    input("Please press enter to select another operation\n")
    return(Main_Body_Function())

    
#The Function for division
def Division():

    print("\nYou have selected division \n")
    
    for number_of_problems in range(0,4,1):

        first = random.randint(1, 100)
        second = random.randint(1, 100)
        
        divide = first / second
        int_dividing = int(divide)

        while divide != int_dividing:
            first = random.randint(1, 100)
            second = random.randint(1, 100)

            divide = first / second
            int_dividing = int(divide)

        
        print("How much is", first," divided by ", second, "?")
        input_answer = int(input())
                                     
        if (input_answer == divide):
            print("\tCorrect!")
            
        if ( input_answer != divide):
        
            for number_of_answer in range(1,3,1):                
  
                if ( input_answer != divide):
                    print("Incorrect, please try again: \n")
                    print("How much is", first," divided by ", second, "?")
                    input_answer = int(input())

                elif (input_answer == divide):
                    print("\tCorrect!\n")

            if input_answer != divide:
                print("\tSorry, you missed this one. The correct answer is", int(divide) , ".\n ")
            else:
                print("\tCorrect!\n")
                

        input("Please press enter for another question \n")
    print("You have completed all 4 practice problems for this section. Redirecting you back to the main menu.\n")
    input("Please press enter to select another operation\n")
    return(Main_Body_Function())
          
        
# The Function for Exponetiation
def Exponentiation():

    print("\nYou have selected exponentiation \n")

    for number_of_problems in range(0,4,1):

        first = random.randint(1, 100)
        second = random.randint(1, 100)
        
        power = first ** second

        while (power > 2500):
            first = random.randint(1, 100)
            second = random.randint(1, 100)
            power = first ** second
        
        print("How much is", first," to the power of ", second, "?")
        input_answer = int(input())

        
        
        if (input_answer == power):
            print("\tCorrect!")
            
        if ( input_answer != power):
        
            for number_of_answer in range(1,3,1):                
  
                if ( input_answer != power):
                    print("Incorrect, please try again: \n")
                    print("How much is", first," to the power of ", second, "?")
                    input_answer = int(input())

                elif (input_answer == power):
                    print("\tCorrect!\n")

            if input_answer != power:
                print("\tSorry, you missed this one. The correct answer is", power , ".\n ")
            else:
                print("\tCorrect!\n")
                

        input("Please press enter for another question \n")
    print("You have completed all 4 practice problems for this section. Redirecting you back to the main menu.\n")
    input("Please press enter to select another operation\n")
    return(Main_Body_Function())



# The menue       
def display_menu():
    print("Type any of the following single letter operations to start the designated math problems.\
{a, s, m, d, e, q}\n")
    
    print("\ta  for addition")
    print("\ts  for subtraction")
    print("\tm  for mulitplication")
    print("\td  for division")
    print("\te  for exponentiation")
    print("\tq  to quit the program\n")


#The Welcome
def Welcome():
        print("Welcome to the CISC 106 Basic Math Instructor. \
This program allows you to practice your math skills in addition, \
subtraction, multiplication, division and exponentiation.\n")


#return and main body function
def Main_Body_Function():

    #display menu
    display_menu()

    # Get users choice
    operation = input("Type in operation now: \n")
        
    while operation != QUIT_PROGRAM:
        

        # Finding and Running the operation of choice
        if operation == ADDITION:
            Addition()
            return(None)
            
        elif operation == SUBTRACTION:
            Subtraction()
            return(None)
        
        elif operation == MULTIPLICATION:
            Multiplication()
            return(None)
        
        elif operation == DIVISION:
            Division()
            return(None)
        
        elif operation == EXPONENTIATION:
            Exponentiation()
            return(None)
        
        else:
            print("Error: You have selected an invalid option.")
            operation = input("Please try again: \n")
            
    else:
        print("Thank you for using the CISC 106 Basic Math Instructor. Please Come again.")
    





# The body of the program
def main():

    #Say welcome
    Welcome()

    #Calling the Main Body Function
    Main_Body_Function()
    
main()
