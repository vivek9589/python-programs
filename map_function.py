# map function

numbers = [1,2,3,4]

#normal method using "map function "

'''


def square(a):
    return a**2

sq=list(map(square,numbers))
print(sq)
'''
# by using "lambda function"

sq1 = list(map(lambda a : a**2,numbers))
print(sq1)



# by list comprehension

sq_new = [i**2 for i in numbers]
print(sq_new)sDF
