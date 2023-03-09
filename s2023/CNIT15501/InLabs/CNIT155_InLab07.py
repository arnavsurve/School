#===============================================================
# Your Name & Lab Section: Arnav Surve, Thursday 9:30am
# Your Purdue Email: asurve@purdue.edu
# Program Description:
# This program validates whether three user provided side lengths form a valid triangle. If they do, the program then calculates the perimeter.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#=================================================================
import math


def displayMyInfo(): # Print programmer information in box of stars
    print("          *******************************")
    print("          *         Arnav Surve         *")
    print("          *      asurve@purdue.edu      *")
    print("          *        CNIT155 InLab07      *")
    print("          *******************************")

def Validate(a, b, c): # function to validate whether 3 sides form a triangle
    if a >= b and a >= c: # if a is the longest side
        if b + c > a: # verify sides b & c sum to greater than a
            return True
        else:
            return False
    elif b >= a and b >= c: # if b is the longest side
        if a + c > b: # verify sides a & c sum to greater than b
            return True
        else:
            return False
    else: # if c is the longest side 
        if a + b > c: # verify sides a & b sum to greater than c
            return True
        else:
            return False

def computePerimeter(a, b, c):
    return (a + b + c) # calculate perimeter of 3 sides using Heron's formula 

def main():
    displayMyInfo() # call display info at start of program
    option = True
    # run program loop while option is True
    # exit program when option changed to False
    while option == True:
        # prompt user for options
        a = float(input("Enter side length 'a' of triangle: "))
        b = float(input("Enter side length 'b' of triangle: "))
        c = float(input("Enter side length 'c' of triangle: "))

        print("\nValidating triangle...\n")

        # if valid triangle, print perimeter
        if Validate(a, b, c):
            print("This is a valid triangle")
            print("The perimeter of the triangle is {per:.2f}\n".format(per = computePerimeter(a, b, c)))

            # ask user if they want to compute again, if Y then return to loop start & 
            # prompt for new side lengths. If N then exit program
            option2 = True
            while option2 == True:
                proceed = input("Do you want to compute again? (Y/N): ").lower()
                if proceed == "y":
                    option2 = False
                elif proceed == "n":
                    option = False
                    option2 = False
                else:
                    print("Invalid input")
                    print("Enter Y or N, case insensitive")
                    continue
                continue
        else: # prompt again if user provides invalid input
            print("Inputs do not form a triangle. Please enter different values\n")
            continue
            
    print("End of program")


main()
