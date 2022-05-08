print("Welcome to Vivek's Calculator\n")
 
a=int(input("Enter  1st number"))
b=int(input("Enter 2nd number"))


print("1) Addition \n 2) Subtraction \n 3) Multiplication \n 4)Division\n 5) Modulus")
choice=int(input("Enter your choice"))


def add(a,b):
      sum=a+b
      print("sum of ",a, "+ ",b,"is =",sum)
      
def sub(a,b):
    diff=a-b
    print("subtraction of ",a, "-",b,"is =",diff)

def mul(a,b):
    pro=a*b
    print("multiply of ",a, "*",b,"is =",pro)

def div(a,b):
    dive=a/b
    print("division of ",a, "/ ",b,"is =",dive)

def mod(a,b):
    modu=a%b
    print("sum of ",a, "% ",b,"is =",modu)


    


if choice==1:
       add(a,b)
            
   
    
elif choice==2:
       sub(a,b)
         
      
      
    
elif choice==3:
       mul(a,b)
               
    
elif choice==4:
        div(a,b)

    
elif choice==5:
       mod(a,b)
       
     

else:
       print("Invalid choice")
        
















