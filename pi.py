# Write a function in Python that accepts one numeric parameter. 
# This parameter will be the measure of an angle in radians. 
# The function should convert the radians into degrees and then return that value.

import math

def converter(ins):
    print(str(int(ins))+ " Rad = " + str(ins*180/math.pi) + " Degrees")

if __name__ == "__main__":
    print("Radians to Degrees converter.")

    user_in = float(input("Enter Radians: "))
     
    #  send to converter
    converter(user_in)
    