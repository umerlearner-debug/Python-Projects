import random
import string

# Ask user for password length
length = int(input("Enter password length: "))

# Characters to use
characters = string.ascii_letters + string.digits

# Generate password
password_list = []

for i in range(length):
    password_list.append(random.choice(characters))

# Shuffle the password
random.shuffle(password_list)

# Convert list to string
password = "".join(password_list)

print("Generated Password:", password)