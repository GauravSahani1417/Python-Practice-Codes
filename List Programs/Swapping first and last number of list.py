#Program to swap first and last number of the list
#Input : [1, 2, 3, 4]
#Output : [4, 2, 3, 1]

# Swap function 
def swapList(newList): 
    size = len(newList)
    
    #Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp 
    
    return newList

newList = [11, 25, 9, 56, 24, 45]

print(swapList(newList))
    
    