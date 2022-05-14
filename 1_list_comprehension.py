

# LIST COMPREHENSION

# with the help of " list comprehension" we can create of list in one line



# create a list of sqaures  from 1 to 10




# normal list 
squares  = []
for i in range(1,11):
    squares.append(i**2)
print(squares)




# with LIST COMPREHENSION

squares =  [i**2 for i in range(1,11)]
print(squares)




# another example


# with normal list

negative = []
for i in range(1,11):
    negative.append(-i)

print(negative)




# with list comprehension

negative_1 = [-i for i in range(1,11)]
print(negative_1)



#  third example

# with normal list
names = ['Harshit','Mohit','Rohit']
new_list =[]
for name in names:
    new_list.append(name[0])
print(new_list)




# with list comprehension

list_com = [ name[0] for name in names]
print(list_com)
    





    
