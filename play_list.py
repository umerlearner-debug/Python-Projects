l = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original List:", l)

count = 0
for i in l:
    count += 1
avg = count/len(l)
print("sum = ",count)
print("average = ", avg)

l.sort()

print("Smallest element is: ", l[0])

print("Largest element is: ",l[-1])
