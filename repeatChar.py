# Create a Python function that accepts a string. 
# The function should return a string,
#  with each character in the original string doubled. If you send the function "now" as a parameter,
#  it should return "nnooww," and if you send "123a!", it should return "112233aa!!".

# display subfunction
def play(ins):
    
    print(''.join(ins))

# this function doubles each item in the string
def doubler(ins):
    
    # create holder for the new srtring 
    temp =[]
    # iterate throug the string 
    for x in ins:
        
        # save each item twice
        temp.append(x)
        temp.append(x)

    # display final result 
    play(temp)
    

# drvier 
if __name__=="__main__":
    
    # prompt user for inout
    user_in = input("Enter String")

    # call subroutine 
    doubler(user_in)




    