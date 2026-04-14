# File I/O
# .txt .csv
#f = open("data.txt","w")#not abosoulte path # return file object

# data = f.readline()

# print(data)
# data = f.readline()
# print(data)

# f.write("This is override file ...")

# f.close()

# f = open("data.txt","a")
# f.write("This is new text ")
# f.close()

# f = open("sample.txt","x")
# f.write("this is randoom file and random text")
# f.close()

# f = open("data.txt","w+")
# f.write("this is new line")
# print(f.read())
# f.close()

#with keyword

# with open ("data.txt","r") as f:
#     print(f.read())


#delete file
# import os
# os.remove("sample.txt")


#word search 
# line = 0
# data = True
# word = "Python"
# with open("data.txt","r") as f:
#     while data:
#         data = f.readline()
#         line+=1
#         if(word in data):
#             print(f"{word} fount at line {line}")
#             break

#exception handling

# try:
#     x = int(input("Enter x: "))
#     ans = 10/x
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except ValueError:
#     print("Invalid Input")
# else:
#     print("ans = ",ans)
# finally:
#     print("This is always excuted")
#     print("End of the program ")

#list comprehension
# sq = []
# for i in range(6):
#     sq.append(i*i)
# print(sq)
# #easy way
# list = [i*i for i in range(6)]
# print(list)

# #odd numbers only
# list1 = [i*i for i in range(6) if i%2!=0 ]
# print(list1)

# #if else
# nums =[-1,-4,5,3,-1]
# list3 = [ 0 if val<0 else val for val in nums]
# print(list3)

# words =["hello","welcome"]
# print(words[0].upper())
# words = [val.upper() for val in words]
# print(words)

# import json


# json_str = '{"name":"Shraddha","isTeacher":null}'
# py_obj = json.loads(json_str)
# print(type(py_obj))
# print(type(json_str))
# print(json_str)
# print(py_obj)

# import json
# py_obj = {
#     "name":"Shraddha",
#     "isTeacher":True
# }
# json_str = json.dumps(py_obj)
# print(type(py_obj),type(json_str))
# print(py_obj)
# print(json_str)

# import json
# with open("data.json","r") as f:
#     py_obj = json.load(f)
#     print(py_obj,type(py_obj))

import json
d = {
    "name":"Shraddha",
    "age":"25",
    "isTeacher":True
}
with open("data.json","w") as f:
    json.dump(d,f,indent = 4,sort_keys = True)
