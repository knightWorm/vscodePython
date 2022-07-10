# Write a function in Python that accepts a credit card number.
#  It should return a string where all the characters are hidden 
#  with an asterisk except the last four. For example,
#   if the function gets sent "4444444444444444", 
#   then it should return "************4444".

from distutils.command.sdist import sdist


class _User:
    def __init__(self,ccn):
        self.cn = ccn

    def display(self):
        print("**** **** **** "+str(self.cn[-4:]))

if __name__ == "__main__":
    
    # get user credit card 
    cn = input("Enter Credit Card Number: ")

    if len(cn) > 16:
        print("Invalid Input, Credit card numbers are atleast 16 digits long!")
    else:

    # create class instance 
        p1  = _User(cn)

    # print output 
        p1.display()