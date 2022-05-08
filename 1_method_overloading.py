

#  function / method overloading #

# write a python script to find area of circle ,and area of rectangle with the help of method overloading #





class calculation():


    def area(self,para1=None,para2=None):
        if (para1!=None and para2!=None):
            x =  para1 *para2
            return x

        elif(para1!=None and para2==None):
            x = 3.14 * para1 * para1
            return x

        else :
            x = "no parameter passed"
            return x

y = calculation()
rectangle =  y.area(12,3)
circle  = y.area(12)

print("area of rectangle :" , rectangle)
print("area of circle   : ",circle)
            
