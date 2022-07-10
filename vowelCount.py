# Create a function in Python that accepts a single word 
# and returns the number of vowels in that word. 
# In this function, only a, e, i, o, and u will be counted as vowels — not y.


# contains my dictionary list and return the count
import re


def dic_vowels(com):

    vowels_dic = ['a','A', 'e','E','i','I','o','O','u','U']
    
    # maintain count 
    count  = 0
    
    # iterator 
    for i in range(len(com)):
        count  += vowels_dic.count(com[i])

    return count

if __name__ == "__main__":
    
    # get user input 
    user_in = input("Enter String: ")

    temp  = user_in.split(' ')
    if len(temp) > 1: 
        print("invalid input! Single words only, Run program again")
    else:
    # call subroutine 
        print("'"+user_in +"' Contains "+ str(dic_vowels(user_in)) + " Vowel(s)")
    
    