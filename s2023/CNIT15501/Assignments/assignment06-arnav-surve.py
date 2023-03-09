#=================================================================
# Arnav Surve, Thursday 9:30am
# asurve@purdue.edu
# Program Description:
# This program performs various computations depending on the user's choice.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

import math # import math library for factorial function

def main():
    option = 0
    # run program loop while user's selected option is 5
    # exit program when user inputs 5
    while option != 5:
        # display program header with options
        print("+ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ")
        print("                          Fun For Loops")
        print("+ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + \n")
        print("1. Display natural numbers from N2 to N1, given N1 < N2")
        print("2. Display the squared of natural numbers from N1 to N2, given N1 < N2")
        print("3. Compute the factorial of N")
        print("4. Display the inverted trangle of stars")
        print("5. Exit")
        print("\n+ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ")

        # prompt user for choice of option
        option = int(input("\nChoose one of the following options to perform: "))

        if option == 1:
            # display natural numbers from N2 to N1, given N1 < N2
            N2 = int(input("Enter a natural number for N2: "))
            N1 = int(input("Enter a natural number for N1: "))
            print("Displaying natural numbers from {N2} to {N1}".format(N2 = N2, N1 = N1))
            # iterate down from N2 to N1 and print
            for i in range(N2, N1 - 1, -1):
                print(i)

        elif option == 2:
            # display the squared of natural numbers from N1 to N2, given N1 < N2
            N1 = int(input("Enter a natural number for N1: "))
            N2 = int(input("Enter a natural number for N2: "))
            print("Displaying the squares of natural numbers from {N1} to {N2}".format(N2 = N2, N1 = N1))
            # iterate from N1 to N2 and print square of that number
            for i in range(N1, N2 + 1):
                print(i ** 2)

        elif option == 3:
            # compute the factorial of N
            N = int(input("Enter natural number for N: "))
            print("Factorial of {N}: {f}".format(N = N, f = math.factorial(N)))

        elif option == 4:
            # display an inverted triangle of stars
            N = int(input("Enter number of rows to print inverted triangle of *s: "))
            # iterate down starting from N
            for i in range(N, 0, -1):
                # print appropriate amount of starting whitespace
                print(" " * (N - i), end="")
                # print appropriate number of stars
                for j in range(i):
                    print("*", end="")
                print("")

        # print goodbye and exit program loop
        elif option == 5:
            print("Goodbye!")

        # notify user in case of invalid input (option not 1 - 5)
        else:
            print("Invalid input!\nEnter a number between 1 and 5.\n")


main()
