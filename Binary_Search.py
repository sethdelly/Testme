# Python program to implement binary search
from array import *


def binary_search():
    while True:
        try:
            key = int(input("Enter KEY number to be searched: "))
            lists = input("Enter numbers to populate the array: ")
            values = lists.split(' ')
            values = [int(i) for i in values]     # List comprehension
            values.sort()
            print(values)
            print(" ")
            # values = array("i", [5, 7, 9, 13, 32, 33, 42, 54, 56, 88])
            # values = array("i", [])
            start = 0
            mid = 0
            end = len(values)-1
            if key not in values:
                print(key, "not found in this array  !! ")
            else:
                for i in range(0, len(values)):
                    if key == values[i]:
                        mid = (start + end)//2
                    elif key > values[mid]:
                        start = mid + 1
                        mid = (start + end)//2
                    elif key < values[mid]:
                        end = mid - 1
                        mid = (start + end)//2
                    elif key == values[mid]:
                        print(key, " is found at index", mid)
                        break
        except ValueError:
            print(" Sorry, only NUMBERS are allowed !! ")


binary_search()




