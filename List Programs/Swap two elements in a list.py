#Program to swap two elements in list
#Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
#Output : [19, 65, 23, 90]

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    
    return list

List = [23, 65, 19, 90, 45, 11, 45] 
pos1, pos2  = 1, 4

print(swapPositions(list, pos1-1, pos2-1))