#Swap commas and dots in a String
#Input : 14, 625, 498.002
#Output : 14.625.498, 002

# Python code to replace "," with "." and vice-versa 
def Replace(str1): 
    maketrans = str1.maketrans 
    final = str1.translate(maketrans(', .', '., ')) 
    return final 

# Driving Code 
string = "14, 625, 498.002"
print(Replace(string))

def Replace(str1): 
    str1 = str1.replace(', ', 'third') 
    str1 = str1.replace('.', ', ') 
    str1 = str1.replace('third', '.') 
    return str1 

string = "14, 625, 498.002"
print(Replace(string))