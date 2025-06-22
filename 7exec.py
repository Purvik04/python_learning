# with open("practice.txt" , "a") as f:
#     f.write("Hi everyone\n")
#     f.write("We are learning file I/O\n")
#     f.write("using Java.\n")
#     f.write("I like Programming in Java.")


# with open("practice.txt" , "r") as f:
#     data = f.read()

# new_data = data.replace("Java", "python")

# with open("practice.txt" , "w") as f:
#     data = f.write(new_data)


# with open("practice.txt", "r") as f:
#     data = f.readlines()
#     line_no = 1
#     is_found = False
#     for line in data:
#         index = line.find("learning")
#         if(index != -1):
#             print("Learning is found at line", line_no, "at index",index)
#             is_found = True
#         line_no += 1
#     if(not is_found):
#         print("Word not Found.")

with open("sample2.txt", "r") as f:
    data =f.read()
    print(data)
    list = data.split(",")
    even_count = 0
    for ele in list:
        if(int(ele)%2 == 0):
            even_count += 1

    print("even count",even_count)
    





