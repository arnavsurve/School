#===============================================================
# Your Name & Lab Section: Arnav Surve, Thursday 9:30am
# Your Purdue Email: asurve@purdue.edu
# Program Description:
# This program takes a user input and runs a function on the input as specified.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#=================================================================


def main():
    option = 0
    # run program loop while user's selected option is 5
    # exit program when user inputs 5
    while option != 5:
        # display program header with options
        print("\n####################################################################")
        print("                          For Loops Lab")
        print("####################################################################")
        print("1. Print all natural numbers between 1 and N")
        print("2. Display and add all natural numbers from N to 1")
        print("3. Display and add all inverse numbers from 1/1 to 1/N")
        print("4. Display the triangle of stars")
        print("5. Exit")
        print("####################################################################")

        # prompt user for option
        option = int(input("\nChoose one of the following options to perform: "))

        if option == 1:
            N = int(input("Enter a natural number for N: "))
            print("Displaying natural numbers from 1 to {N}".format(N = N))
            # iterate 1 through N and display numbers
            for i in range(1, N+1):
                print(i)

        elif option == 2:
            N = int(input("Enter a natural number for N: "))
            print("Displaying natural numbers from {N} to 1".format(N = N))
            # iterate 1 through N, display numbers, and print sum of numbers
            total = 0
            for i in range(N, 0, -1):
                print(i)
                total += i
            print("\nThe sum of numbers from {N} to 1: {total}".format(N = N, total = total))

        elif option == 3:
            N = int(input("Enter a natural number for N: "))
            print("Printing all inverse numbers from 1/1 to 1/{N}".format(N = N))
            sum = 0
            # iterate 1 through N and display inverse numbers
            for i in range(1, N+1):
                # add the inverse (1/i) to sum
                print("1/{i}".format(i = i))
                sum += 1 / i
            print("\nThe sum of all inverse numbers from 1/1 to 1/{N}: {sum:.2f}".format(N = N, sum = sum))

        elif option == 4:
            N = int(input("Enter number of rows to print *s: "))
            # print star triangle according to N
            for i in range(N+1):
                for j in range(i):
                    print("*", end="")
                print("")

        # print goodbye and exit program loop
        elif option == 5:
            print("Goodbye!")

        # notify user in case of invalid input (option not 1 - 5)
        else:
            print("Invalid input!\nEnter a number between 1 and 5.")
    print("End of program.")

main()
