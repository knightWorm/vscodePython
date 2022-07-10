#  Create a Python function that accepts a string.
#  This function should count the number of Xs and the number of Os in the string. 
#  It should then return a boolean value of either True or False.

# If the count of Xs and Os are equal, then the function should return True. 
# If the count isn't the same, it should return False. 
# If there are no Xs or Os in the string,
# it should also return True because 0 equals 0. The string can contain any type and number of characters.

from dataclasses import asdict


def counter(strs):
    
    # O and X container
    oContainer  = 0
    xContainer = 0

    for x in range(len(strs)):
        if strs[x] == 'x' or strs[x] == 'X':
            xContainer +=1
        elif strs[x] == 'o' or strs[x] == "O":
            oContainer +=1
    
    return oContainer == xContainer

# driver 
if __name__=="__main__":
    
    # get user input (String)
    user_in = input("Enter String: ")
    
    # pass onto subroutine and print 
    print(counter(user_in))
    
    