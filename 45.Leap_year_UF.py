year = 1986
def leap_year(year):
    a = False
    if(((year%4==0)and(year%100!=0))or (year%400==0)):
       a = True
    
    return(a)
a = leap_year(year)
if(a):
    print("It's a leap Year.")
else:
    print("It's not a leap Year.")