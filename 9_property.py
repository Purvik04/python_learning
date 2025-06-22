class Student:

    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        # self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"

    # def calcPercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"

    # method is converted into property of object
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths)/3) + "%"

s1 = Student(98,86,87)

print(s1.percentage)
s1.phy = 86
# s1.calcPercentage()
print(s1.percentage)
