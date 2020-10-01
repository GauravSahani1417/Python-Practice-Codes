#Python program to print odd numbers in a List

#Input: list1 = [2, 7, 5, 64, 14]
#Output: [7, 5]

list1 = [1, 5, 8, 46, 91, 11, 3, 12]

# iterating each number in list 
for num in list1: 
    if num % 2 != 0: 
       print(num, end = " ") 
       