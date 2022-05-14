


# Decorators   ----> enhance the functionality of other functions

'''


def decorator_function(any_function):
    def wrapper_function():
        print("this is awesome function")
        any_function()
    return wrapper_function


#this is awesome function
def func1():
    print("this is function1 ")

#this is awesome function
def func2():
    print("this is function2 ")

#var = decorator_function(func2)
#var()


# no need to take new variable,
func1 = decorator_function(func1)
func1()




'''
# @ use for decorators 

def decorator_function(any_function):
    def wrapper_function():
        print("this is awesome function")
        any_function()
    return wrapper_function



@ decorator_function       # shortcut
def func1():
    print("this is function1 ")
func1()
