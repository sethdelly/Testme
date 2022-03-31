# Python program to print the numbers from a given number n till 0 using recursion

count = 1
num = int(input("Enter number: "))
while num >= 0:
    print(f"{count},  {num}")
    count += 1
    num -= 1



