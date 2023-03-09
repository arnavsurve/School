#===============================================================
# Your Name & Lab Section: Arnav Surve, Thursday 9:30am
# Your Purdue Email: asurve@purdue.edu
# Program Description: 
# This program takes user input for the number of students in CNIT155, the price of the textbook, and today's temperature in fahrenheit. It returns a few lines of data after each user input based on the input given.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#=================================================================

def main():
    # prompts user for number of students, prints that number and the data type
    print("This is InLab02 for CNIT155 by Arnav Surve")
    students = int(input("\nEnter the number of students in CNIT 155: "))
    print("The number of students in CNIT 155 is", students)
    print("The data type of the number of students is", type(students))

    # prompts user for price of textbook, prints that number and the data type
    textbookprice = float(input("\nEnter the price of the textbook: "))
    print("The price of the textbook is ${:0.2f}".format(textbookprice))
    print("The data type of the price is", type(textbookprice))

    # prompts user for today's temperature in fahrenheit    
    fahrenheit = float(input("\nEnter today's temperature in Fahrenheit (ºF): "))
    # convert fahrenheit input to celsius
    celsius = (fahrenheit -32) * 5 / 9
    # print temperature in celsius and data type of variable
    print("Today's temperature in Celsius is", str(round(celsius, 2)), "ºC")
    print("The data type of the temperature is", type(celsius))

main()
