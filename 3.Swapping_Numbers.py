# Method 1: Using third variable
# Defining 2 variable for Numbers.
a = 3
b = 2
Temp = a # defining value of temp is a .
a = b # Updating value of "a" to "b" means changing value "3" to "2". 
b = Temp # Updating Value of "b" to "Temp" means "2" to "Temp = a = 3"
print("a :",a)
print("b :",b)

# Method 2 : Without using third variable :
c = 4 # Defining a variable in which we stored it's value '4'.
d = 5 # Defining a variable in which we stored it's value '5'.
c = c + d # Updating value of c = c+d means now c = 9
d = c - d # Updating value of d = c-d means now it will use c = 9 means d = 9-5 = 4
c = c - d # Updating value of c = c-d means now it will use d = 4 means c = 9-4 = 5
print("c :",c) # printing updated value of c.
print("d :",d) # Printing updated value of d.
