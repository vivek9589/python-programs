# program for leap year #


#if a year divided by 4 and not divided by 100 then it is a leap year,
#if a year divided by 400 then it is also a leap year
#if a year divided by 100 then it is not a leap year



year=int(input("enter a year"))

if year%4==0 and year%100!=0:
    print(year,"is a leap year")
elif year%400==0:
    print(year,"is a leap year")
elif year%100==0:
    print(year,"is not a leap year")

else:
    print(year,"not a leap year")
