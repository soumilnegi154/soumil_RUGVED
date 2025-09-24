"""Define a function named “triple_and” that takes three parameters and returns True
only if they are all True and False otherwise"""



def triple_and(x,y,z):                                  #defining function triple_and
    if (x==True and y==True and z==True):               #checking if all parameters are true
        return True                         
    else:
        return False

print(triple_and(bool(input("Enter value: ")),          #here taking parameters as input
                 bool(input("Enter value: ")),          #it will be true if theres any input
                 bool(input("Enter value: "))))         #false if no input