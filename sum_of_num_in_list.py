# Python program to display the sum of n numbers using a list
Total_sum = 0
list_of_num = input("Enter numbers in a list: ")
Final_list = list_of_num.split()
for i in Final_list:
    Total_sum += int(i)
print(Total_sum)