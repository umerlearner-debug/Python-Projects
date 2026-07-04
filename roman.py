class Roman:

    def convert(self, num):

        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        roman = ""

        i = 0

        while num > 0:

            if num >= value[i]:
                roman = roman + symbol[i]
                num = num - value[i]
            else:
                i = i + 1

        return roman


number = int(input("Enter an integer: "))

obj = Roman()

answer = obj.convert(number)

print("Roman Numeral =", answer)