from abc import ABC, abstractmethod

class ABCclass:

    def print(ABC, x):
        print("Passed value ", x)

    
    @abstractmethod
    def task(self):
        print("We are inside the ABSclass task.")
class test_class(ABCclass):
    def task(self):
        print("We are inside the test class task.")

    

test_obj = test_class()
test_obj.task()
test_obj.print(100)


