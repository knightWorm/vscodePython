# Create a function in Python that accepts two parameters. 
# The first should be the full price of an item as an integer. 
# The second should be the discount percentage as an integer.

# The function should return the price of the item after the discount has been applied. 
# For example, if the price is 100 and the discount is 20, the function should return 80.


def display(ins):
    print(ins)

def calculate(x, y):
    
    temp  = x - (x * (y/100))

    # display result
    display(temp)

if __name__ =="__main__":
    
    # get user input 
    temp = input("Enter Price and percentage: ")
    temp = temp.split(" ")

    # price 
    x = int(temp[0])
    
    # percentage 
    y = int(temp[1])

    # call subrutine 
    calculate(x,y)

    
    