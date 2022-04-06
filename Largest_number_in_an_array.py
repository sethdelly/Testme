# Python program to find the largest number in a list without using built-in functions

def largest_number():
    while True:
        try:
            num = input(" Enter numbers to populate the array: ")
            lists = num.split(" ")
            lists = [int(x) for x in lists]
            print(lists)
            max_number = lists[0]
            # max_number = 1
            for i in range(len(lists)):
                if max_number < lists[i]:
                    max_number = lists[i]
            print(" ")
            print("The biggest number in the list is: ", max_number)
        except ValueError:
            print(" ")
            print("Sorry, only DIGITS are allowed !! ")


largest_number()