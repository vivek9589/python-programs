



# list comprehension with " if -else"


nums = [1,2,3,4,5,6,7,8,9,10]

#new list = [-1,4,-3,8]

new_List = []

for i in nums:
    if i%2!=0:
        new_List.append(-i)

    else:
        new_List.append(2*i)


print("with normal list")
print(new_List)


# with  list comprehension

new_list2 = [i*2 if (i%2==0) else -i for i in nums]
print("with list comprehension")
print(new_list2)
