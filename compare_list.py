#compare lists
# == ,is
#is vs equal

fruits1 = ['orange','apple','pear']
fruits2 = ['kiwi','apple','banana']
fruits3 = ['orange','apple','pear']
print(fruits1 == fruits2)  # values are not same result is ==> FALSE
print(fruits1 == fruits3)  # values are same result is ===> TRUE
 
 

print(fruits1 is fruits3)   #  "is " check location of list in memory which is not same everytime that's why result is FALSE

