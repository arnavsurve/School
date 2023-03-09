#=================================================================
# Arnav Surve, Thursday 9:30am
# asurve@purdue.edu
# Program Description: 
# This is a program to find the roots of a quadratic equation.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified. 
# I have not given other fellow student(s) access to my program. 
#=================================================================

"""
TODO
- 7 inline comments
"""

import math

def main():
    # prompt user for three coefficients
    a = float(input("Enter the coefficient a: ")) 
    b = float(input("Enter the coefficient b: ")) 
    c = float(input("Enter the coefficient c: ")) 

    # print quadratic equation with coefficients plugged in
    print("\nQuadratic equation is: {a:.1f}x^2 + {b:.1f}x + {c:.1f} = 0".format(a = a, b = b, c = c))

    # calculate and print discriminant
    discriminant = (b * b) - (4 * a * c)
    print("\nDiscriminant: {disc:.3f}\n".format(disc = discriminant))

    if discriminant > 0:
        # calculate 2 roots if discriminant positive
        root1 = ((-1 * b) + math.sqrt(discriminant)) / (2 * a)
        root2 = ((-1 * b) - math.sqrt(discriminant)) / (2 * a)
        print("The equation has two real roots: {root1:.3f} and {root2:.3f}".format(root1 = root1, root2 = root2))

        # calculate 1 root if discriminant is zero
    elif discriminant == 0:
        root = (-1 * b) / (2 * a)
        print("The equation has one real root: {root:.3f}".format(root = root))

    else:
        # if discriminant is negative, return no real roots
        print("The equation has no real roots.")

    # return minimum of three entered coefficients
    print("\nThe smallest coefficient is: {coeff:.2f}".format(coeff = min(a, b, c)))

main()
