# 2nd way of overriding  #





class student():

    def avg(self, *x):
        average  =  0
        sum  = 0


        if len(x) == 0:
            average = " no values provided "

        else:
            for i in x:
                sum +=i

                average = sum /len(x)

        return average



s1 = student()
avg1 = s1.avg(11,12,13,14,15,16,17,18,19,20)
print(avg1)
