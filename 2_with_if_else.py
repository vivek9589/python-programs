

# list  comprehension with  "if statement "




# with normal list
numbers  = list(range(1,11))
nums = []
for i in numbers:
    if i%2 ==0:
        nums.append(i)
print(nums)


# with list comprehension
print("even list of list_comprehension")
even_nums = [i for i in numbers if i%2==0 ]
print(even_nums)
print("odd list of list_comprehension")
odd_nums = [i for i in numbers if i%2!=0 ]
print(odd_nums)
                



