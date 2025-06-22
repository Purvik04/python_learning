# oops part2

# del keyword
class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks


# s1 = Student("karan", 98)
# print(s1.name)
# del s1.name
# del s1
# print(s1.name)

# public and private attr
class Account:

    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #private attr, by giving __ ahead of attr name

    # private method
    def __hello(self):
        print("Hello account holder")

a1 = Account(12345, "abcde")
# print(a1.__acc_pass) gives error
        
        