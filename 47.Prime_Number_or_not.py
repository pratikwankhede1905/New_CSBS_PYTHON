num = int(input("Enter any number :"))
def prime_not(num):
    a = True
    if(num == 2):
        return True
    if(num<2):
        return False
    for i in range(2, num):
        if(num%i==0):
            return False
    return(a)
a = prime_not(num)
if(a):
    print("It's a prime num.")
else:
    print("It's not a prime num.")