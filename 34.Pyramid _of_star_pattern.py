rows = int(input("Enter Numbers of rows you want : "))
for i in range(1,rows+1):
    for j in range(0,rows-i):
        print(" ",end="")
    print("*"*(2*i-1))