# Take marks as input from user.
print("Enter marks obtained in 4 subjects: ")
math = int(input("Maths: "))
english = int(input("English: "))
science = int(input("Science: "))
Urdu = int(input("Urdu: "))

sum = math+english+science+Urdu
print("Sum of math english science urdu = ", sum)

perc = (sum/400)*100
print(end = "Percentage mark = ")
print(perc)
