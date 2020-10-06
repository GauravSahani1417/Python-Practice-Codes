#Remove i’th character from string in Python

# Python code to demonstrate 
# method to remove i'th character 
# using replace() 
  
# Initializing String  
test_str = "GeeksForGeeks"

# Printing original string  
print ("The original string is : " + test_str) 

# Removing char at pos 3 
# using replace 
new_str = test_str.replace('e', '') 

# Printing string after removal   
# removes all occurrences of 'e' 
print ("The string after removal of i'th character( doesn't work) : " + new_str)

# Now, Removing 1st occurrence of e, i.e 2nd pos. 
# if we wish to remove it. 
new_str = test_str.replace('e', '', 1) 

# Printing string after removal   
# removes first occurrences of e 
print ("The string after removal of i'th character of first occurance(works) : " + new_str) 

# Now, Removing 3rd occurrence of e, i.e 2nd,3rd and 10th position.
# if we wish to remove it. 
new_str = test_str.replace('e', '', 3) 

# Printing string after removal   
# removes third occurrences of e
print ("The string after removal of i'th character of 3rd occurance(works) : " + new_str) 