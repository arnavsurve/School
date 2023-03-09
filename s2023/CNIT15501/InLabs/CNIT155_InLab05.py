#===============================================================
# Your Name & Lab Section: Arnav Surve, Thursday 9:30am
# Your Purdue Email: asurve@purdue.edu
# Program Description: 
# This program takes a user input and runs a calculation on the input as specified.
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
        print("                          While Loops Lab")
        print("####################################################################")
        print("1. Print all natural numbers between 1 and N")
        print("2. Add up all natural numbers between 1 and N")
        print("3. Add up all even natural numbers between 1 and N")
        print("4. Compute the sum and average of the square numbers between 1 and N")
        print("5. Exit")
        print("####################################################################")

        # prompt user for option
        option = int(input("\nChoose one of the following options to perform: "))

        if option == 1:
            N = int(input("Enter a natural number for N: "))
            print("Displaying natural numbers from 1 to {N}".format(N = N))
            # iterate 1 through N and display numbers
            i = 1
            while i <= N:
                print(i)
                i += 1

        elif option == 2:
            N = int(input("Enter a natural number for N: "))
            print("Displaying natural numbers from 1 to {N}".format(N = N))
            # iterate 1 through N, display numbers, and print sum of numbers
            i = 1
            total = 0
            while i <= N:
                print(i)
                total += i
                i += 1
            print("\nThe sum of numbers from 1 to {N} is {total}".format(N = N, total = total))


        elif option == 3:
            N = int(input("Enter a natural number for N: "))
            print("Displaying even natural numbers from 1 to {N}".format(N = N))
            # iterate through even numbers from 1 to N, display numbers, and print sum of numbers
            i = 2
            total = 0
            while i <= N:
                total += i
                print(i)
                i += 2
            print("\nThe sum of even numbers from 1 to {N} is {total}".format(N = N, total = total))

        elif option == 4:
            N = int(input("Enter a natural number for N: "))
            print("Displaying the squares of numbers from 1 to 7")
            # iterate 1 through N, display squares of numbers, and display sum and average of squared numbers
            i = 1
            total = 0
            while i <= N:
                print(i ** 2)
                total += (i ** 2)
                i += 1
            print("The sum of the squares of numbers from 1 to {N} is {sum}".format(N = N, sum = total))
            print("The average of squares of numbers from 1 to {N} is {avg:.2f}".format(N = N, avg = total/N))

        # print goodbye and exit program loop
        elif option == 5:
            print("Goodbye!")

        # notify user in case of invalid input (option not 1 - 5)
        else:
            print("Invalid input!\nEnter a number between 1 and 5.")

    print("End of program.")

main()
