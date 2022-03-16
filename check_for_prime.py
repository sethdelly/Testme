# Python program to check whether the given integer is a prime number or not


while True:
    num = int(input("Enter a number to check if its prime or not: "))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, " is not a Prime Number")
                break
        else:
            print(num, " is a Prime Number ")
    else:
        print(num, " is not a Prime Number")