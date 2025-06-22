# list in python
# lists are mutable
list1 = ["karan", 98, True, 45.234]
# slicing of list is same as string

# list functions
list = [2,1,3,4]

list.append(0)
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

list.insert(1, 0)
print(list)

list.remove(0) #remove first occurence of given element
print(list)

list.pop(0) #remove element from given index
print(list)



# tuple is same as list bt it is immutable
tuple = (67,87, 35, 67)

tup1 = () #empty
tup2 = (1,) #single valued , why comma bcz python allows to normally write value in () 
# if not comma it will understand it as normal int

