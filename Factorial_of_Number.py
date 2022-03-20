# Python program to find the factorial of a number using recursion

import math


def factorial():

    while True:

        try:
            fact = 1
            numbers = int(input("Enter number to find the factorial: "))
            if numbers < 0:
                print("Factorial cannot be negative !! ")
            elif numbers < 2:
                print("{}! = {}".format(numbers, fact))
            else:
                for i in range(numbers, 1, -1):
                    # print(i)
                    fact = fact * int(i)
                print("{}! = {}".format(numbers, fact))

        except Exception:
            print("##### Only numbers are allowed !!!")


factorial()