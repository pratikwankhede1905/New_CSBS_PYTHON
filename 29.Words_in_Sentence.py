sen = input("Enter Any sentence : ")
length = len(sen)
spaces = 0
for i in range (0, length):
    if (sen[i]==' '):
        spaces +=1
print(f"{sen} has total of {spaces+1} words")