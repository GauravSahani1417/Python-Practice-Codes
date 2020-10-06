#Python program to check if a string is palindrome or not

#Input : malayalam
#Output : Yes

#Input : geeks
#Output : No

def isPalindrome(s):
    return s == s[::-1]

# Driver code
s = "oppo"
ans = isPalindrome(s)

print("Input String is: ", s)
 
if ans==True:
   print("Yes!, The string is palindrome")
else:
   print("No!, The string is not palindrome")
