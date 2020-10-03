#Simple interest formula is given by:
#Simple Interest = (P x T x R)/100
#Where,
#P is the principle amount
#T is the time and
#R is the rate

def simple_interest(p,t,r):
    print('The principal is', p) 
    print('The time period is', t) 
    print('The rate of interest is',r)
    
    SI = (p * t * r)/100
    print('The Simple Interest is', SI) 
    print('Your total amount recieved is:', SI+p)
    return SI

simple_interest(8000, 2, 6)
