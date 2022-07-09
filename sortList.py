# Create a function in Python that accepts two parameters. The first will be a list of numbers. 
# The second parameter will be a string that can be one of the following values: asc, desc, and none.

# If the second parameter is "asc," then the function should return a list with the numbers in ascending order. 
# If it's "desc," then the list should be in descending order, and 
# if it's "none," it should return the original list unaltered.

from lib2to3.pgen2 import driver
import numbers
from typing import OrderedDict


def ascending(ins):
    print("Ascending Order")
    # sort list: sort() default is ascending 
    ins.sort()
    print(str(ins))


def descending(ins):
    
    print("descending Order")

    # sort(), needs setting set to reverse 
    ins.sort(reverse= True)
    print(str(ins))


# secondary driver
def controller(lis, com):
    if com == "desc":
        descending(lis)
    elif com == "asc":
        ascending(lis)
    elif com == "none":
        print("Original list:")
        print(str(lis))

        

# Main driver
if __name__ == "__main__":
    
    # list of numbers
    lis = [1,100,1000,200,500,300,400]
    # print empty line for easthetics 
    print("\n")
    # test1 Original
    controller(lis, "none")

    # test2 ascending Order 
    controller(lis, "asc")

    # test 3 descending order
    controller(lis, "desc")

