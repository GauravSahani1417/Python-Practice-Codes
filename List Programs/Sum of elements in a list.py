#Python program to find sum of elements in list
#Input: [12, 15, 3, 10]
#Output: 40

# Python program to find sum of elements in list 
x = 0
  
# creating a list 
list1 = [11, 5, 17, 18, 23]  

# Iterate each element in list 
# and add them in variale total 
for y in range(0, len(list1)): 
    x = x + list1[y] 
    
# printing total value 
print("Sum of all elements in given list: ", x) 
  