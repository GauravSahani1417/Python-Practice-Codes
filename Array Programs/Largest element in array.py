def largest(arr,n):
    max = arr[0]
    # Traverse array elements from second 
    # and compare every element with  
    # current max
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [14, 4, 27, 3, 1998]
n = len(arr)

Ans = largest(arr,n)

print ("Largest in given array is",Ans)