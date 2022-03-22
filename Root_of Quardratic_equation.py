# Python program to find the roots of a quadratic equation
# x = (-b ± √ (b² - 4ac) )/2a

import math
while True:
    try:
        a = int(input("Enter root a: "))
        b = int(input("Enter root b: "))
        c = int(input("Enter root c: "))
        if (a and b and c) > 0:
            Discriminant = (math.pow(b, 2) - (4 * a * c))
            D = abs(Discriminant)
            Square_root = math.sqrt(D)
            x1 = round(((-b + Square_root)/(2*a)), 2)
            x2 = round(((-b - Square_root) / (2 * a)), 2)
            print(f"Sum_Of_Root: {x1}")
            print(f"Neg_Of_Root: {x2}")
            print((x1, x2))
        else:
            print("Please Enter Roots greater than zero '0' !!! ")

    except ValueError:
        print("Sorry, only numbers are allowed !!")