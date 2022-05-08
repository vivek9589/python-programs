
#Create a program to print the fibonacci series#


n=int(input("Enter a number"))
a=0
b=1
c=0

#print(a," ",b)


for i in range(2,n+1):
    a=b
    b=c
    c=a+b
    print(c,end=" ")
