import symmetric

array_num = symmetric('i', [1,2,3,5,3,7,9,3])
print("Original array: "+str(array_num))

print("Number of occurances of the number 3 in the said array: "+str(array_num.count(3)))

symmetric.reverse()
print("reverse the order of the items: ")
print(str(array_num))
