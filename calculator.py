print("Welcome to Vivek's Calculator\n")

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

def square(a):
      
      sq=a*a
      print("Square of ",a,"is",sq)
      
      

print("press 1 : For integer datatype\n press 2 : For float datatype")
ch=int(input("Enter your choice"))





if (ch==1):
      
     
      print("1) Addition \n 2) Subtraction \n 3) Multiplication \n 4)Division\n 5) Modulus \n6)Square")
      choice=int(input("Enter your choice"))
      
      a=input("Enter 1st number")
      b=input("Enter 2nd number")
      a = int(a)
      b = int(b)



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

      elif choice==6:
            square(a)
             
           
      else:
             print("Invalid choice")
             
   

       

        
elif ch==2:
      a1=float(a)
      b1=float(b)
      print("1) Addition \n 2) Subtraction \n 3) Multiplication \n 4)Division\n 5) Modulus")
      choice1=int(input("Enter your choice"))


      if choice1==1:
            add(a1,b1)
            
       
                
      elif choice1==2:
            sub(a1,b1)
            
             

      elif choice1==3:
            mul(a1,b1)
             

      elif choice1==4:
            div(a1,b1)
              

      elif choice1==5:
            mod(a1,b1)

      elif choice1==6:
            square(a1)
             
           
      else:
            print("Invalid choice")
             

else:
      print("Invalid choice for datatype")
      
      




    



















