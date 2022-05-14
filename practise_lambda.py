
'''

# lambda expression  practise


#normal function


def is_even(a):
    return a%2==0

print(is_even(3))



# by using lambda

is_even_ = lambda a : a%2==0

print(is_even_(4))

'''


# using lambda with "if else"

# write a python script that return true if the length of string is greater than 5
#otherwise return false



def func(s):
    if len(s)>=5:
        return True
    else:
        return False

string = 'vivek'
print(func(string))

#using lambda function
print("using lambda function")

a = lambda s : True if len(s) > 5 else False
print(a(string))
