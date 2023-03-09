#=================================================================
# Arnav Surve, Thursday 9:30am
# asurve@purdue.edu
# Program Description: 
# This Python program takes the user’s input and calculates the side area, bottom area, and volume of a pool.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified. 
# I have not given other fellow student(s) access to my program. 
#=================================================================

import math

def side_area(d1, d2, l):
    return (d1+d2) * (l/2) # calculate side area given depths and length

def bottom_area(d1, d2, l, w):
    d3 = d2 - d1 # find d3 using d2 and d1
    hypotenuse = math.sqrt(math.pow(d3, 2) + math.pow(l, 2)) # apply hypotenuse formula with d3 and l
    return hypotenuse * w # bottom area is hypotenuse * width

def volume(side, w):
    return side * w

def main():
    d1 = float(input("Enter depth 1 of the pool: "))
    d2 = float(input("Enter depth 2 of the pool: "))

    # only run if d2 greater than d1
    if d2 > d1:
        w = float(input("Enter width of the pool: "))
        l = float(input("Enter length of the pool: "))
        side = side_area(d1, d2, l)
        print("\nCalculating...\n")
        print("The side area of the pool is: {sidearea:.2f} ".format(sidearea = side))
        print("The bottom area of the pool is: {bottom:.2f} ".format(bottom = bottom_area(d1, d2, l, w)))
        print("The volume of the pool is: {vol:.2f} ".format(vol = volume(side, w)))
    else:
        print("Invalid input! D2 must be greater than D1!")

main()
