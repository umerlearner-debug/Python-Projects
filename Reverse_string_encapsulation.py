class StringReverse:
    def __init__(self, text):
        self.text = text

    def reverse_string(self):
        return self.text[::-1]

text = input("Enter a string: ")

obj = StringReverse(text)

print(obj.reverse_string())