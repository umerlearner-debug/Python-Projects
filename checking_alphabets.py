# Program to check if a character is an alphabet

char = input("Enter a character: ")

if (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z'):
    print("It is an alphabet.")
else:
    print("It is not an alphabet.")