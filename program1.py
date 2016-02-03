
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
RANDOMIZE = "r"
QUIT_PROGRAM = "q"


# The operation functions
def Addition():
    """
    adds two random integers and checks if the inputted answer is correct  and if not asks again for the answer 3 times before giving the answer. It will also ask 4 random addition questions from being called till it returns to the main function
	parameters:
	none
	Variables 
	first - a random integer from the random library 
	second - a random integer from the random library
	add - adds the first and second random integers together
	input_answer - the users answer
    """

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

    """
    subtracts two random integers and checks if the inputted answer is correct  and if not asks again for the answer 3 times before giving the answer. It will also ask 4 random subtraction questions from being called till it returns to the main function.
	parameters:
	none
	Variables 
	first - a random integer from the random library 
	second - a random integer from the random library
	sub - subtracts the second random integer from the first
	input_answer - the users answer
    """
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

    """
    multiplies two random integers and checks if the inputted answer is correct  and if not asks again for the answer 3 times before giving the answer. It will also ask 4 random multiplication questions from being called till it returns to the main function.
	Parameters:
	none
	Variables 
	first - a random integer from the random library 
	second - a random integer from the random library
	multiply - the first random integer times the second
	input_answer - the users answer
    """

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
    """
    divides two random integers and checks if the inputted answer is correct  and if not asks again for the answer 3 times before giving the answer. It will also ask 4 random multiplication questions from being called till it returns to the main function. There is also a while loop that makes sure that the function will not randomly select problems with answers that are not integers.
	Parameters:
	none
	Variables 
	first - a random integer from the random library 
	second - a random integer from the random library
	divide - the first random integer divided by the second
	input_answer - the users answer
    """

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
    """
    Uses one random integer and raises it to the power of another random integer  and checks if the inputted answer is correct  and if not asks again for the answer 3 times before giving the answer. It will also ask 4 random multiplication questions from being called till it returns to the main function. there is a while loop that makes sure that the answer does not exceed 2500 to make the questions easier.
	Parameters:
	none
	Variables 
	first - a random integer from the random library 
	second - a random integer from the random library
	power - the first random integer to the power of  the second
	input_answer - the users answer
    """

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

            
            if input_answer != power:
                print("\tSorry, you missed this one. The correct answer is", power , ".\n ")
            else:
                print("\tCorrect!\n")
                

        input("Please press enter for another question \n")
    print("You have completed all 4 practice problems for this section. Redirecting you back to the main menu.\n")
    input("Please press enter to select another operation\n")
    return(Main_Body_Function())

def Randomize():
    """
    Randomly selects an operation from the main menu so that the user can do a random problem.
    Parameters
	None
	Variables
	None
    """
    print("\nYou have selected randomize \n")

    #choices = [, SUBTRACTION, MULTIPLICATION, DIVISION, EXPONENTIATION, QUIT_PROGRAM]
    #random.shuffle(choices)

    random_choice = random.sample(["a","s","m","d","e"], 1)
    
    if random_choice == ["a"]:
            Addition()
            return(None)
            
    elif random_choice == ["s"]:
            Subtraction()
            return(None)
        
    elif random_choice == ["m"]:
            Multiplication()
            return(None)
        
    elif random_choice == ["d"]:
            Division()
            return(None)
        
    elif random_choice == ["e"]:
            Exponentiation()
            return(None)
    
    


# The menue       
def display_menu():

    """ Displays the main mein whenever called.
	Parameters
	None
	Variables
	None
    """

    print("Type any of the following single letter operations to start the designated math problems.\
{a, s, m, d, e, q}\n")
    
    print("\ta  for addition")
    print("\ts  for subtraction")
    print("\tm  for mulitplication")
    print("\td  for division")
    print("\te  for exponentiation")
    print("\tr  for random")
    print("\tq  to quit the program\n")
    


#The Welcome
def Welcome():
    """
    Prints a welcome statement that explains what the function is.
    """

    print("Welcome to the CISC 106 Basic Math Instructor. \
        This program allows you to practice your math skills in addition, \
        subtraction, multiplication, division and exponentiation.\n")


#return and main body function
def Main_Body_Function():

    """ This is what would normally be written into the ‘main’ function of the program but is displayed as a separate function so as to be called by other functions.
	Parameters
	None
	Variables 
	None
    """

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

        elif operation == RANDOMIZE:
            Randomize()
            return(None)
        
        else:
            print("Error: You have selected an invalid option.")
            operation = input("Please try again: \n")
            
    else:
        print("Thank you for using the CISC 106 Basic Math Instructor. Please Come again.")
    





# The body of the program
def main():
    """ where the program starts executing and where all the functions are called from.
	Parameters
	None
	Variables
	None
    """

    #Say welcome
    Welcome()

    #Calling the Main Body Function
    Main_Body_Function()
    
main()
