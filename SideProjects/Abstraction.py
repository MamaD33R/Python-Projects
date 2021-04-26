# Your class should contain at least one abstract method and one regular method.
# Create a child class that defines the implementation of its parents abstract method.
# Create an object that utilizes both the parent and child methods.


from abc import ABC, abstractmethod

class NewStudent(ABC):
    def StuID(self, ID):
        print("Your ID is: ", ID)
    @abstractmethod
    def NewID(self, ID):
        pass

class ChangeID(NewStudent):
    def NewID(self, ID):
        print('Your new changed ID is {}.'.format(ID))

obj = ChangeID()
obj.StuID('5548')
obj.NewID('1045')
