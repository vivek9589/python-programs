# in operator in list

list1 = [1,2,3,4,5,6]

if 8 in list1:
    print("present")

else:
    print("not present")

# some more methods in list
# 1] count
# 2] sort method
# 3] sorted function
# 4] reverse
# 5] clear
# 6] copy

fruits = ['orange','apple','pear','banana','kiwi','apple','banana']

# print(fruits.count('apple'))

#fruits.sort()
#print(fruits)

# sorted function (don't sort the list , but it sort for a one time only)
num = [3,5,1,9,10]
print(sorted(num))   # sorted list
print(num)           # original list

#num.clear()

num_copy = num.copy()
print(num_copy)
