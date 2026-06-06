# Question 1
num = int(input("Enter a number: "))
odd_numbers = [i for i in range(1, num) if i % 2 != 0]
print("Odd numbers:", odd_numbers)

# Question 2
fruits = ["apple", "banana", "mango", "orange", "grapes"]
updated_fruits = [fruit.capitalize() for fruit in fruits]

print("Original List:", fruits)
print("Updated List:", updated_fruits)