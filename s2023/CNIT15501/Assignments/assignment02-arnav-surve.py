#=================================================================
# Arnav Surve, Thursday 9:30am
# asurve@purdue.edu
# Program Description: 
# This is a conversion calculator that converts pounds - kilograms, celsius - fahrenheit, miles - kilometers, and feet - inches. It takes user input and outputs the according conversions.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified. 
# I have not given other fellow student(s) access to my program. 
#=================================================================

def main():
    print("           **************************************")
    print("           *        CNIT155 Assignment 02       *")
    print("           *                                    *")
    print("           *        Conversion Calculator       *")
    print("           **************************************\n")

    # prompting user for full name
    fullname = input("Enter your full name: ")
    print("Your name is", fullname)

    print("\n** 1st. Pounds to Kilograms conversion **")
    # asking user to input pounds
    pounds = float(input("Enter weight in Pounds to convert to Kilograms: "))
    # converting to kilograms
    kilograms = pounds/2.2046
    # display pounds and kilograms
    print("The weight entered is {pounds:.2f} lb and {kilograms:.2f} kg".format(pounds = pounds, kilograms = kilograms))

    print("\n** 2nd. Celsius to Fahrenheit conversion **")
    # prompts user for today's temperature in fahrenheit    
    celsius = float(input("Enter the temperature in Celsius to convert to Fahrenheit: "))
    # convert fahrenheit input to celsius
    fahrenheit = (celsius * 9/5) + 32
    # print temperature in celsius and data type of variable
    print("The entered temperature in Celsius is {c:.2f} C and {f:.2f} F".format(c=celsius, f=fahrenheit))

    print("\n** 3rd. Miles to Kilometers conversion **")
    # ask user for miles input
    miles = float(input("Enter Miles to convert to Kilometers: "))
    # convert miles to kilometers
    kilometers = miles * 1.609344
    # display miles and kilometers
    print("The distance entered in Miles is {m:.2f} mi and {k:.2f} km".format(m = miles, k=kilometers))


    print("\n** 4th. Feet and Inches to Centimeters **")
    # prompt user for feet and inches and store in variables
    print("Enter your height in feet and inches: ")
    feet = int(input("Feet: "))
    inches = int(input("Inches: "))
    # convert to only inches, then convert to centimeters
    total_inches = (feet * 12) + inches
    cm = total_inches * 2.54
    # display entered height and equivalent centimeters
    print("The height entered is", feet, "feet", inches, "inches and", cm, "cm")

main()
