


# define a function that take list of string

#  return  list containing reverse of every string

# example
# l  = l = ['abc','tuv','xyz']
# output --->  ['cba', 'vut', 'zyx']







def  reverse_string(l):
    return [name[::-1] for name in l]


#l = ['abc','tuv','xyz']
print(reverse_string(['abc','tuv','xyz']))






# with normal list



def  reverse_list(l):
    new_list = []
    for i in l:
        new_list.append(i[::-1])
    return new_list

list_1 = ['abc','tuv','xyz']
print(reverse_list(list_1))







    
