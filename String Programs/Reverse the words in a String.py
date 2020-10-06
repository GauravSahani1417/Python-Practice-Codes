#Reverse words in a given String in Python

#Input : str = "geeks quiz practice code"
#Output : str = "code practice quiz geeks"

def rev_sentence(sentence): 
    # first split the string into words 
    words = sentence.split(' ') 
    # then reverse the split string list and join using space 
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence 

input = 'geeks quiz practice code'
print (rev_sentence(input))