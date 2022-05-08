# Create a Program to find the factorial of a user defined integer.
print("Create a Program to find the factorial of a user defined integer.")

num=int(input("Enter a number "))
f=1

for i in range(1,num+1):
    f=i*f
    if i==num:
        print("Factorial of ",num,"is",f)




'''
n=int(input())

def fact(i):

    f=i*f
    return f

for i in range(1,n+1):
    if i<=n+1:
        fact(i)
    



'''
