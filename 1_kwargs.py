


#Kwargs (keyword arguments)
# ** kwargs (double star operator)


'''
kwargs store as a  "dictionay" and we can store no. of element





'''



def func(name,**kwargs):
    #print(kwargs) # print dictionary
    #print(type(kwargs)) # type ---> dict and [ * args type  is "tuple"]
    for k , v in kwargs.items():
        print(f"{k}: {v}")



#func('vaibhav',first_name = 'vivek' , last_name = 'rathore')


# dictionary unpacking
d = {'name':'harshit','age':24}
func(**d)

