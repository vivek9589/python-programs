# Factorial program  through function #
def fact(x):
    y=1
    if x==1 or x==0:
        return y
    else:
        y=x*fact(x-1)
        return y
#val = int(input("Enter a value"))
#funct_val = fact(val)
#print("Factorial of {} is {} ".format(val,funct_val))
    



#  RecursionError: maximum recursion depth exceeded in comparison

# RECURSSION ERROR -: arise due to which system acheive its maximum depth.
                        
