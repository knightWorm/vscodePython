# Write a Python function that accepts three parameters. 
# The first parameter is an integer. The second is one of the 
# following mathematical operators: +, -, /, or *. The third parameter will also be an integer.

# The function should perform a calculation and return the results. 
# For example, if the function is passed 6 and 4, it should return 24.

# Display all calculation  for all functions
from tkinter import Y


def display(ins):
    print(ins)

# Adds x and Y
def calAdd(x,y):
    display(x+y)

def calSub(x,y):
    display(x-y)

def calDiv(x,y):
    display(x//y)

def calMul(x,y):
    display(x*y)

# second driver 
def subCal(x, com, y):
    
    # logic 
    if com == "+":
        calAdd(x,y)
    elif com == "-":
        calSub(x,y)
    elif com == "/":
        calDiv(x,y)
    elif com == "*":
        calMul(x,y)
    else: 
        print("Function not supported.")
    
# driver 
if __name__ == "__main__":
    
    # get user input 
    user_in = input("Enter Command: ")

    # divide user_in into components for arithmetic
    x = int(user_in[0])
    y = int(user_in[2])
    com = user_in[1]

    # call subroutine 
    subCal(x, com, y)

