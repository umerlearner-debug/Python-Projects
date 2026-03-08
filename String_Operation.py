# Input a word.
text = str(input("Enter a string: "))

# Reverse string
# Using step value as 1 iterate in reverse
revtext = text[::-1]
text = revtext

print("Reverse of given string is: ")
print(text)