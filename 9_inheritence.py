class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCar(Car):

    def __init__(self,brand):
        self.brand = brand

class Fotuner(ToyotaCar):

    def __init__(self,type):
        super().__init__("toyota")
        self.type = type

c1 = Fotuner("diesel")
c2 = Fotuner("petrol")

print(c1.type)
print(c1.brand)

c2.start()


# classmethod decorator
class Student:
    name = "anonymous"

    # it's not changing class attr but creating new instance attr
    # def changeName(self, name):
    #     self.name = name

    # to do this there are many ways
    # def changeName(self, name):
    #     # Student.name = name 
    #     self.__class__.name = name

    # class method has class as first implicit argument
    @classmethod
    def changeName(cls, name):
        cls.name = name

s1 = Student()
s1.changeName("Rahul kumar")
print(s1.name)
print(Student.name) 