# Write a function in Python that accepts a list of any length that contains a mix of 
# non-negative integers and strings. The function should return a list with only 
# the integers in the original list in the same order.

# Display funtcion 
from curses.ascii import isdigit
from hashlib import algorithms_guaranteed
from sunau import Au_read


def display(ins):

    print("The String has these INTS in it: "+ str(ins))

# gets the number of ints in a given string
def intCounter(ins):
    
    # holder for ints
    nums =  []
    
    # iterator
    for x in ins:
    # if int instance is int add number hold 
        if isdigit(x):
            nums.append(x)
    
    # send to display
    display(nums)
    
    

# drvier
if __name__ == "__main__":
    
    user_in =  input ("Enter string: ")
    
    intCounter(user_in)
    