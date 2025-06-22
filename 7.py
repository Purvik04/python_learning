# file i/o in python
import os

# two types of files
# 1> text files:- .txt, .docx etc
# 2> binary files:- .mp4, .mov, .png, .jpeg etc

# open and close files 
#  f = open("file_name", "mode") mode can be r: reading, w: writing

f = open("demo.txt" , "r")
data = f.read()
# data = f.read(10) read only 10 chars from start
print(data)
f.close()

# if file not exist for w and a mode , python will create it
f = open("demo.txt" , "w")
f.write("hello all, overwrited all data")
f.close()

f = open("demo.txt" , "a")
f.write("\nappended data")
f.close()

f = open("demo.txt" , "r")
data = f.read()
# data = f.read(10) read only 10 chars from start
print(data)
f.close()

print("--------------------------")
# with syntax
with open("demo.txt", "r") as f:
    print(f.read())


f = open("sample.txt", "w")
f.close()

os.remove("sample.txt")
