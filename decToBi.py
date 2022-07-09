# Write a function in Python that accepts a decimal number 
# and returns the equivalent binary number. 

from math import remainder
# from re import A


if __name__ == "__main__":
# Holder for binary conversion 
    remainder = []

# get user input for decimal
    user_input  = int(input("Enter Decimal: "))

    if user_input == 0:
        remainder.append(0)
    else:

    # initially the quotien will be the user input 
        quotien = user_input

    # use while loop to iterate unitl quotient = 0
        while(quotien != 0):
        
        # mod to get the remainder and append to my list.
            rem = quotien%2
            remainder.append(rem)

        # divide original input by 2 to get 
            quotien = quotien//2
        # repeat 

# print remainder in reverse for final binary conversion
    remainder.reverse()

    print(remainder)
        
