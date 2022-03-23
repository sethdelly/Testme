# Python program to insert a number to any position in a list

from array import *

while True:
    try:
        special_num = int(input("Enter the special number to be inserted in the array: "))
        position = int(input("Enter position in array: "))
        numbers = array("i", [4, 23, 45, 14, 81, 29, 40, 56, 78, 67, 65])
        print(numbers)
        numbers.insert(position, special_num)
        print(" ")
        print(numbers)
    except ValueError:
        print(" ")
        print(" Hey, only DIGITs are allowed !! ")