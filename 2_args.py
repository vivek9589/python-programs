

# * args with normal parameter




#

def multiply_nums(num,*args):
    multiply = 1
    #print(args)
    for i in args:
        multiply *= i
    return multiply


print(multiply_nums(2,4,3))




# CONCLUSION

# 1) when we specify function parameter then  we have necessary to pass the arguments
# 2) if we define function parameter after " * ARGS " , it will give error
# 3) 
