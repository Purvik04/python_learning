print(1+2)
print("purvik " + "sukhadiya")
print([1,2,3] + [4,5,6])

class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real,"i +", self.img, "j")

    # Dunder functions 
    # operator overloading
    def __add__(self, num2):
        return Complex(self.real+num2.real , self.img+num2.img)
    
    def __sub__(self, num2):
        return Complex(self.real-num2.real , self.img-num2.img)
        
num1 = Complex(1,4)
num1.showNumber()

num2 = Complex(5,4)
num1.showNumber()

# operator overloading
num3 = num1 + num2
num3.showNumber()

num4 = num1 - num2
num4.showNumber()

class Order:

    def __init__(self,item,price):
        self.item = item
        self.price = price

    # dunder function greater than
    def __gt__(self,order2):
        return self.price>order2.price
    
o1 = Order("tea",15)
o2 = Order("cofee",20)
print(o1 > o2)
    
        
