# Power Calculator using loop

base = int(input("Enter the base number: "))
power = int(input("Enter the power: "))

result = 1

for i in range(power):
    result = result * base

print("Result:", result)