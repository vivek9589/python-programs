# spilt method
# convert string into list

'''
info = "vivek 20".split()
print(info)

info = "vivek,20,9589462330".split(',')
print(info)

name,age = "vivek 20".split()  # assign value in two different variable
print(name)
print(age)


name,age,city = input("Enter your name and age and city ").split(',')  
print(name)
print(age)
print(city)

'''


#join method
# convert list to string

info = ['vivek','21']
print(' ,'.join(info))



set1 = {'vivek','2','3','4'}
print(set1)
change = list(set1)
print(change)
print(','.join(change))
