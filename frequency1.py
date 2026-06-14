# Test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print dictionary
print("Test Dictionary:", test_dict)

# Take input from user
value = int(input("Enter the value to check frequency: "))

# Count frequency
frequency = list(test_dict.values()).count(value)

# Print frequency
print("Frequency of", value, "is:", frequency)