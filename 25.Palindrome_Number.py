num = input("Enter a number to check if it's a palindrome or not :")
Palindrome = num[::-1]
if(num == Palindrome):
    print("It's a palindrome Number.")
else:
    print("It's not a palindrome Number.")