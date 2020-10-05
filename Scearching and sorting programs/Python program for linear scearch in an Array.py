#Python Program for Linear Search

#Input : arr[] = {10, 20, 80, 30, 60, 50, 
#                     110, 100, 130, 170}
#          x = 110;
#Output : 6
#Element x is present at index 6!!!

# Searching an element in a list/array in python 
# can be simply done using \'in\' operator 
# Example: 
# if x in arr: 
#   print arr.index(x) 
  
# If you want to implement Linear Search in python 
  
# Linearly search x in arr[] 
# If x is present then return its location 
# else return -1 

def search(arr, x): 
    
    for i in range(len(arr)):
        
        if arr[i] == x: 
            return i 
        
    return "No element found!"

arr = (1, 2, 3, 4, 10, 15)
find = 2

print("The element",find,"exist in an array at index:" ,search(arr, find))
