

# function with all parameters
# very important to understand


# "PADK"
 # P==> PARAMETER
 # A==> * ARGS
 # D==> DEFAULT PARAMETERS
 # K==> ""KWARGS





# DEFAULT PARAMETERS


def func(name = 'unknown' , age = 24):
    print(name)
    print(age)


func()


func('vivek')




# using all parameters

def func1(name,*args,last_name = 'unknown' , **kwargs):
    print(name)
    print(*args)
    print(last_name)
    print(kwargs)



func1('vanshika',1,2,3,4,a = 12,b = 13)





# using only "parameter and default parametes both"

# " we need to maintain the order of parameter " #
