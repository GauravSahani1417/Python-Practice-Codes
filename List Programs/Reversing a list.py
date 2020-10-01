#Reversing a list
#Input : list = [10, 11, 12, 13, 14, 15]
#Output : [15, 14, 13, 12, 11, 10]

#Using in-built reverse function
def Reverse(lst): 
    lst.reverse() 
    return lst 
      
lst = [10, 11, 12, 13, 14, 15] 
print("List before reversing :", lst)
print("Reversed list is : ", Reverse(lst)) 
