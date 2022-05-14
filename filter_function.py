

# filter function

def is_even(a):
    return a%2==0

numbers = [3,4,2,1,5,6,9,8,10]
#print(filter(lambda a : a%2==0,numbers))   #----> it print the object

evens = list(filter(lambda a : a%2==0,numbers))
print(evens)    # it filtered even no. from the list




for i in evens:    # filter object is "iterate only single time ",if split into tuple and list then it iterate no. of times
    print(i)

for i in evens:
       print(i)
