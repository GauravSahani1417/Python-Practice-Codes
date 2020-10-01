# Python program to copy or clone a list 
# Using the Slice Operator

def Cloning(list1): 
    li_copy = list1[:] 
    return li_copy 

list1 = [4, 8, 2, 10, 15, 18] 
li2 = Cloning(list1) 
print("Original List:", list1) 
print("After Cloning:", li2) 