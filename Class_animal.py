from abc import ABC, abstractmethod

class ANIMAl(ABC):

    def move(self):
        pass


class Human(ANIMAl):

    def move(self):
        print("I can walk and run.")


class snake(ANIMAl):
    def move(self):
        
        print("I can crawl.")

class dog(ANIMAl):
    def move(self):
        print("I can bark.")

class Lion(ANIMAl):
    def move(self):
        print("I can roar.")

R = Human()
R.move()

K = snake()
K.move()

R = dog()
R.move()

K = Lion()
K.move()