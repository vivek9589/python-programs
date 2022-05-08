# data structures
# this chapter ---> list
# list --> ordered collection of items

# you can store anything in lists int,float, string
'''

numbers = [1,2,3,4]
print(numbers)



words = ["vivek","rathore","python",'list']
print(words)

# we also use mixed datatype
mixed = [1,2,3,4,"five","six",2.4,None]
print(mixed)


# creating list from the "string"
l = list("This is a list")
print(l)

# creating list from the "Tuple"
tup = ('w','e','r','t','y')
tup1 = list(tup)
print(tup1)


# how to access list element
print("access element,, index of 3 value is ==> ",numbers[2])




# updation in list
numbers[3] = "update at index 3"
print(numbers)

numbers[1:] = 'two'
print(numbers)

numbers[:1] = 'two' 
print(numbers)

numbers[1:1] = 'two'
print(numbers)



numbers[1:] = ["three",33]
print(numbers)
'''




# append in list {append is used for add element in the last of the list}
l = ["apple","mango"]
print(l)
l.append("banana")
print(l)


# some more methods to add data in the list
# insert method
# how to join (concatenate) two list
# extend method
# difference between append and extend method

'''
# insert method
list1 = ["ram","shayam"]
print(list1)
list1.insert(1,"rahul")
print(list1)
 


# how to join (concatenate) two list
l1 = [1,2,3]
l2 = [4,5,6]
#l3 = l1+l2
#print(l3)


# extend method
l1.extend(l2)
print(l1)


# difference between append and extend method
l1.append(l2)
print(l1)

'''

# common methods to delete data from list
# pop method
# del method
# remove method
l1=['orange','apple','pear','banana','kiwi']
print(l1)

# pop method
l1.pop()
print(l1)

l1.pop(1)
print(l1)

#del method

del l1[0]
print(l1)

# remove method
l1.remove('banana')
print(l1)
#l1.remove('kela')
#print(l1)



