# permutation by import method (use )


'''

#import factorial_by_RECURSSION as fact
from factorial_by_RECURSSION import *

x = 5
y = 2

val_x = fact(x)
val_y = fact(x-y)

z = val_x/val_y

print("Peremuation of {} over {} is {}".format(x,y,z))





import factorial_by_RECURSSION as fact_1

x = 5
y = 2

val_x = fact_1.fact(x)
val_y = fact_1.fact(x-y)

z = val_x/val_y

print("Peremuation of {} over {} is {}".format(x,y,z))


'''


# combination #

import factorial_by_RECURSSION as fact_1

x = 5
y = 2

val_x = fact_1.fact(x)
val_r= fact_1.fact(y)
val_y = fact_1.fact(x-y)*val_r

z = val_x/val_y

print("Peremuation of {} over {} is {}".format(x,y,z))
