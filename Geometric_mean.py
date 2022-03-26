# Python program to find the geometric mean  and Arithmetic mean of n numbers

import math

Geometric_mean = 1
Arithmetic_mean = 0

def geometricMeanAndArithmeticMean():
    while True:
        try:
            options = int(input(f""" 
                Please choose one of the options below to complete your calculations:
                                1. GEOMETRIC MEAN
                                2. ARITHMETIC MEAN           
                            """))
            if options == 1:
                print("ENTER TWO EVEN NUMBERS: ")
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                if num1 % 2 != 0 or num2 % 2 != 0:
                    print("Please Enter an EVEN number !!")
                    print("#####################")
                    break
                Geometric_mean = math.sqrt(num1) * math.sqrt(num2)
                round(Geometric_mean,2)
                print(f"The Geometric mean of {num1}, and {num2}, is # {Geometric_mean}, ")

            elif options == 2:
                print("ENTER ANY TWO NUMBERS: ")
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                Arithmetic_mean = (num1 + num2)/2
                round(Arithmetic_mean, 2)
                print(f"The Arithmetric mean of {num1}, and {num2}, is # {Arithmetic_mean},")


        except ValueError:
            print("ONLY NUMBERS ARE ALLOWED !!")
            print("############################")

geometricMeanAndArithmeticMean()


