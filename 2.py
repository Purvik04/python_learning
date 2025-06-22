#in python we can access char by index but can't manipulate

#slicing

#str[start:end] end is not included

str = "apnacollege"

print(str[1:4])

print(str [:4] ) # is equal to print(str[0:4])

print(str[5:]) # is equal to print(str[5:len(str)])

# negative slicing
# indexing -1 from last char
str2 = "apple"

print(str2[-3:-1]) #last index not count

# string fucntions
str3 = "I am an engineer."

print(str3.endswith("er."))
print(str3.capitalize)
print(str3.replace("e","o"))
print(str3.find("am")) #return first index of word
print(str3.count("am"))

age = 20

if(age>18):
    print("can apply for license")
elif(age==18):
    print("can not")
else:
    print("pagal abhi to bachha hain")