str = input("Enter any single character :")
letters = ["a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def char(char):
    for i in range(0,26):
        if char == letters[i]:
            print("Entered character is verbal.")
char(str)
print("Not any decision means non verbal.")