# oops in python

class Student:

    college_name = "ABC College" #class attributes
    name = "anonymous"

    # instance attr >> class attr
    # but we generally don't do this

    # default constructors
    def __init__(self):
        pass

    # parameterized constructors
    def __init__(self, name: str, marks : int):
        if not isinstance(marks,int):
            raise TypeError("Marks must be an integer.")
        print("Hello students")
        self.name = name #instance attribute
        self.marks = marks #instance attribute

    def welcome(self):
        print("hello student,", self.name)

    def get_marks(self):
        return self.marks
    
    # static methods are class level methods and dont need self parameters
    @staticmethod #decorator
    def get_college():
        print(Student.college_name)

    #decorator takes func as input and give func as output with behaviour changed

s1 = Student("Karan", 98)
print(s1.name, s1.marks)
print(s1.get_marks())
s1.welcome()

s1 = Student("arjun", 45)
print(s1.name, s1.marks)

s1.get_college()