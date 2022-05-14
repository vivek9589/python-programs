# * args as a arguments




def multiply_nums(*args):
    multiply = 1
    print(args)
    for i in args:
        multiply *= i
    return multiply




num = [2,3,4] 

print(multiply_nums(*num))






# 1)  when we pass argument of "list/tuple" it considered as a single element
# 2) solution   ===> pass arguments of "list/tuple" with  [ "* operator"]
