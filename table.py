#Print the table of user defind number

"""
n=int(input("Enter a number"))
count=1
for var in range(n,n*11,n):
    print(n,"*",count,"=",var)
    count=count+1

    """

# 2nd method of print table (given by sir)

table=int(input("enter a number"))
m=table*10
count=1
for i in range(table,m+1,table):
    print("{}*{}={}".format(table,count,i))
    count=count+1
    
