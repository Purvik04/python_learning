# loops in python

count = 1

while count <= 10:
    print(count)
    count+=1


nums = [10,20,30,40,50]

for el in nums:
    print(el)
else:
    print("loop ends") #work when loop ends (if break from anywhere then it will not work)


# range (start? , stop, step?) default 0 start and 1 step , not included end
for el in range(5):
    print(el)

for el in range(1,5):
    print(el)

for el in range(1,50,2): #printing odd numbers
    print(el)

for el in range(2,50,2): #printing even numbers
    print(el)

for el in range(100,0, -1):
    print(el)

# pass in python

for el in range(5):
    pass
   
# pass indicates null stmt , it represents that in future some code will be placed here
# pass is generally used in try catch blocks

