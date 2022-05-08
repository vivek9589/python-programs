# 1ST method of swapping.
'''

print("This script is intended to swap the value of two variable using a third temporary variable")

a=int(input("enter a 1st number"))
b=int(input("enter a 2nd number"))

print("before swapping of numbers")
print("a=",a,"b=",b)
temp=a
a=b
b=temp

print("After swapping of numbers")
print("a=",a,"b=",b)

'''

#2ND method of swapping
'''

print("Another method of swapping in python ,")
a=int(input("enter a 1st number"))
b=int(input("enter a 2nd number"))

print("before swapping of numbers")
print("a=",a,"b=",b)

a,b=b,a

print("After swapping of numbers")
print("a=",a,"b=",b)


'''


# 3RD method of swapping



print("Another method of swapping in python ,")
a=int(input("enter a 1st number"))
b=int(input("enter a 2nd number"))

print("before swapping of numbers")
print("a=",a,"b=",b)

a=a+b
b=a-b
a=a-b

print("After swapping of numbers")
print("a=",a,"b=",b)
