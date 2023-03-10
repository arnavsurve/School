#=================================================================
# Arnav Surve, Thursday 9:30am
# asurve@purdue.edu
# Program Description:
"""
This Python program performs various computations using user defined functions. It
displays a menu and asks the user to select one of options. The menu will be
displayed at the beginning and then displayed whenever each option is done (except
the Exit option). The program keeps running until the user choose the exit option.
"""
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

def displayMyInfo(): # Print programmer information in box
    print("          -------------------------------")
    print("          |         Arnav Surve         |")
    print("          |      asurve@purdue.edu      |")
    print("          |        CNIT155 InLab07      |")
    print("          -------------------------------")

def factorial(n):
    # iterate through n and add each factorial to the sum
    sum = 1
    for i in range(1, n):
        sum += sum * i
    return sum

def maximumNo(x, y, z):
    # return the maximum number out of three arguments
    return max(x, y, z)

def digits(n):
    # calculate number of digits in a number n
    count = 0
    while n > 0:
        # iterate through each tens place in the number and increment the counter
        count += 1
        n = n // 10
    return count


def main():
    displayMyInfo() # call display info at start of program
    option = 0
    # run program loop while option is not 4
    # exit program when user selects exit option 4
    while option != 4:
        # display user options
        print("\n\n========================== User Defined Functions Menu ==========================")
        print("1. Compute N factorial")
        print("2. Find the maximum")
        print("3. Find the number of digits")
        print("4. Exit")
        print("=================================================================================")

        # prompt user for options
        option = int(input("\nChoose one of the following options to perform: "))

        if option == 1:
            print("1. Compute N factorial")
            # prompt user for a natural number
            num = int(input("Enter a natural number for N: "))
            print("{num}! = {ans}".format(num = num, ans = factorial(num)))

        elif option == 2:
            print("2. Find the maximum")
            # prompt user for 3 numbers to find maximum
            first = int(input("Please enter the 1st number: "))
            second = int(input("Please enter the 2nd number: "))
            third = int(input("Please enter the 3rd number: "))
            print("The greatest number among the three numbers: {ans}".format(ans = maximumNo(first, second, third)))

        elif option == 3:
            # prompt user for a number to calculate amount of digits
            print("3. Find the number of digits")
            num = int(input("Enter a natural number for N: "))
            print("The number of digits in {num} is {ans}".format(num = num, ans = digits(num)))

        elif option == 4:
            # exit program when user selects option 4
            print("Goodbye!")
            break

        else:
            # Raise error when user selects an invalid option
            print("Invalid option! Enter a number between 1 and 5.")
            continue

main()
