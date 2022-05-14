


# make flexible Function (to use no. of argument without any limit)

# * operator
# * args



# normal Function

def total(a,b):
    return a+b


print(total(3,4))   # this working well , if give only two arguments ,

#print(total(3,4,1))   # and if we give more than two argument , it will give error  {TypeError: total() takes 2 positional arguments but 3 were given}



# SOLUTION for this problem  is "* ARGS"


# * args function

def add(*args):
    #print(args)
    total =0
    for num in args:
        total += num
    return total

        
        
        
    
    #print(type(args))

result = add(1,2,3,4,5)
print(result)
