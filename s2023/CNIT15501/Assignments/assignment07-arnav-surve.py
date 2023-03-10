#=================================================================
# Arnav Surve, Thursday 9:30am
# asurve@purdue.edu
# Program Description:
#
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

"""
TODO
program desc
15 inline comments
"""

def displayMyInfo(): # Print programmer information in box of stars
    print("          -------------------------------")
    print("          |         Arnav Surve         |")
    print("          |      asurve@purdue.edu      |")
    print("          |        CNIT155 InLab07      |")
    print("          -------------------------------")

def factorial(n):
    sum = 1
    for i in range(1, n):
        sum += sum * i
    return sum

def maximumNo(x, y, z):
    return max(x, y, z)

def digits(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count


def main():
    displayMyInfo() # call display info at start of program
    option = 0
    # run program loop while option is True
    # exit program when option changed to False
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
            num = int(input("Enter a natural number for N: "))
            print("{num}! = {ans}".format(num = num, ans = factorial(num)))

        elif option == 2:
            print("2. Find the maximum")
            first = int(input("Please enter the 1st number: "))
            second = int(input("Please enter the 2nd number: "))
            third = int(input("Please enter the 3rd number: "))
            print("The greatest number among the three numbers: {ans}".format(ans = maximumNo(first, second, third)))

        elif option == 3:
            print("3. Find the number of digits")
            num = int(input("Enter a natural number for N: "))
            print("The number of digits in {num} is {ans}".format(num = num, ans = digits(num)))

        elif option == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid option! Enter a number between 1 and 5.")
            continue

main()
