class myClass:

    __privateVar = 27

    def __privmeth(self):
        print("I'm inside the class Myclass.")

    def hello(self):
        print("Private variable value.", myClass.__privateVar)


foo = myClass
foo.hello()
foo.__privmeth
