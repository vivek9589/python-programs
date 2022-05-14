

















# WITH NORMAL LIST


def to_power(p,*args):
    power_list = []

    if args == ():
        print("Hey you didn't pass args")

    else:
        for i in args:
            #print(args)
            power_list.append(i**p)
        print(" with normal list")
        print(power_list)




Nums = [1,2,3]

to_power(3,*Nums)



#  WITH LIST COMPREHENSION
def to_power_comp(p,*args):
    return [print("Hey you didn't pass args")  if args == () else i**p for i in args]


Nums_c = [1,2,3]
print("with list comprehension")
print(to_power_comp(3,*Nums_c))






# HARSHIT SOLUTION     ======>>>>>

# CHECK LIST IS EMPTY OR  NOT

# first method
l  = []

if l:
    print("not empty")
else:
    print("empty")



# second method

l1 = [1,2,3]

if len(l1)>0:
    print("not empty")
else:
    print("empty")




# harshit solution

def  to_power_h(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return "you didn't pass any args"


nums  = [1,2,3]
print("harshit solution")
print(to_power_h(3,*nums))
