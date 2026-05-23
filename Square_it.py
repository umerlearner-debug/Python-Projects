start = input("Enter the starting value: ") 
end = input("Enter the end value: ")
sq= []
even= []
odd=[]
for num in range(start, end+1):
    square = num*num
    sq.append(square)
    if square%2==0:
        square.append
