

# Globala vs local variable
# DATE :- 5/MARCH/2022



# DATE :- 5/MARCH/2022
'''
count=1
def plus():
    count +=1

def minus():
    count -=1

print("count = ",count)
plus()
plus()
minus()
minus()

print("count = ",count)

# UnboundLocalError: local variable 'count' referenced before assignment


'''
# 
count=1
def plus():
    global count
    count +=1

def minus():
    global count
    count -=1

print("count = ",count)
plus()
plus()
minus()
minus()

print("count = ",count)
