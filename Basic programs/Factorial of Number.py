#Method 1: Recursive
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n-1);

num = 6; 
print("Factorial of",num,"is", factorial(num)) 

#Method 2: Iterative

def factorial(n): 
    if n < 0: 
        return 0
    elif n == 0 or n == 1: 
        return 1
    else: 
        fact = 1
        while(n > 1): 
            fact *= n ### a *= b means a = a * b 
            n -= 1 ### a -= b means a = a - b
        return fact 
    
num = 6; 
print("Factorial of",num,"is", factorial(num)) 