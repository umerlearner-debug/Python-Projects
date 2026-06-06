# Taking input for two sets

set1 = set(map(int, input("Enter elements of Set 1 separated by spaces: ").split()))
set2 = set(map(int, input("Enter elements of Set 2 separated by spaces: ").split()))

# Finding symmetric difference
result = set1.symmetric_difference(set2)

print("Symmetric Difference:", result)