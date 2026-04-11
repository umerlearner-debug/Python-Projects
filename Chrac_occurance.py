string = input("Please enter your own word: ")

chrac = input("Please enter your own chracter: ")

i = 0
count = 0

while(i < len(string)):
    if (string[i] == chrac):
        count = count + 1
        
    i = i + 1

print("The total number of time", chrac ,"has occured = ", count)