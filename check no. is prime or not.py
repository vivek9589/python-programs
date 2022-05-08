
num = int(input("enter a number"))

for i in range(2,num-1):
    if num%i==0:
        print(num,"not a prime number")
        break
else:
    print(num,"is a prime number")
