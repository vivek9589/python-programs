a=int(input("Enter a 1st number"))
b=int(input("Enter a 2nd number"))
c=int(input("Enter a 3rd number"))

if a>b and a>c:
    print(a,"is greater than",b,"and",c)
elif b>a and b>c:
        print(b,"is greater than",a,"and",c)
else:
        print(c,"is greater than",a,"and",b)
