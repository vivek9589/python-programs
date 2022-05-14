'''

def decorator_function(any_function):
    def inner_function():
        print("this is awesome function")
        any_function()
    return inner_function



@decorator_function
def func(a):
    print("this is a function with argument",a)

func(7)


'''



##########  Above code give error --> because  we are  passing the argument ###########




#### solution ####


def decorator_function(any_fun):
    def inner_function(*args,**kwargs):
        print("solution of argument problem")
        return any_fun(*args, **kwargs)
        
    return inner_function


@decorator_function
def func(a):
    print("this is a function with arguments",a)


#func(6)


@decorator_function
def add(a,b):
    return a+b

print(add(3,5))

