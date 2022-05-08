#Create a program that asks the user for a number and then prints out a list of all the divisors of that number#


'''
num=int(input())
for i in range(1,num+1):
    if num%i==0:
        print("Divisor of ",num,"is ",i,end="\n")
    else:
        print("not divisor",i)

'''


'''
num=int(input("Enter a number"))
for i in range(1,num+1):
    if num%i==0:
        print(i," ",end="")
'''


# program of lcm with the help of divisor#

def lcm(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i,end=" ")
num=int(input("enter a number"))
lcm(num)
