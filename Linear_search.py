# Python program to implement linear search
from array import *


def linear_search():

    while True:
        try:
            data = int(input("Enter data to be found: "))
            values = array("i", [15, 5, 20, 35, 2, 42, 67, 17])
            for i in range(0, len(values)):
                if data == values[i]:
                    print(data, "found at index:", i )
                    break
            else:
                print(f"{data}, not found !!")
        except ValueError:
            print("Sorry, only Numbers are allowed !! ")


linear_search()