# word2 = "python"
# word1 = "I Love"

# print(len(word1))
# print( word1 + " "+word2)

# word = "python"
# print(word[2])

# #word[2]='h' Not Possible in python
# so string is immutable in python 

# for ch in word:
#     print(ch)

#slicing

# str = "Python"
# print(str[:3])

# print(str[-4:-2])

#string formatting
 #dyanmic value
#1)
# a = 5
# b = 10
# print("language is {}".format("python"))
# print("sum of {} and {} is {}".format(a,b,a+b)) #normal formatting
# #index based formatting
# print("sum of {1} and {0} is {2}".format(b,a,a+b))
# #value based formatting
# print("sum of {a} and {b} is {c}".format(a=50,b=10,c = a+b))

#fstring
# a=5
# b=10
# print(f"sum of {a} and {b} is {a+b}")
 
# marks = [99,100,101.1,"list",101]
# marks[2]=1001#mutable
# print(marks)
# print(marks[2])
# print(len(marks))
# print(type(marks))

# print(marks[:2])
# print(marks[len(marks)-1:len(marks)])

#list specific methods
# marks = [1,2,3]
# marks.append(4)
# marks.insert(2,10)
# marks.sort()
# marks.reverse()
# print(marks)

# nums=[1,2,3,5]
# idx = 0
# for val in nums:
#     if(val == 3):
#         print(f"3  is found at {val}")
#         break
#     idx+=1

#tuple
#immutable not allow duplicates
# tup = (1,3,4.3,"abc",5,6)
# print(tup)
# print(len(tup))
# print(tup[2])
# tup[2]=34
# print(tup[3:])

# tup = ("abc",)
# print(type(tup))

# tup=(1,2,3,4,5,6)
# sum=0
# for val in tup:
#     sum+=val
# print(sum)

#tuple method

# t=(1,2,3,2,2)
# print(t.index(2))
# print(t.count(2))

#dictonary 
#key:value

# dict = {"name":"Shraddha", "roll_no":35,"subjects":["math","science","history"]}

# info = {
#     "name":"shraddha",
#     "cgpa":9.2,
#     "subjects":["math","science"]
# }
# print(type(info))
# print(info["name"])
# info["name"]="bhushan"
# print(info)
# print(type(info.keys()))
# dict_k =list( info.keys())
# print(type(dict_k))

# dict_vals = list(info.values())
# print(dict_vals)

# print(info.items())

# print(info.get("name"))


# info.update({"city":"delhi"})
# print(info)


# x = {1,2,3,3}
# print(type(x))
# print(x)
# print(len(x))

# s = {1,2,3}
# #{} empty dictoinary 

# s1 = {} #dictonary
# s2 = set() #set 
# print(type(s1))

# s={1,2,3,4,5}
# print(s)
# s.add(6)
# print(s)
# s.remove(4)
# print(s)
# s.pop() #remove random value in a set
# print(s)
# s.clear()
# print(s)
# s={1,2,3,4,5}
# s2={4,5,6,7}
# print(s.union(s2))
# s3 = s.intersection(s2)
# print(s3)

info = [
    ("Alice","Maht"),
    ("Bob","sci"),
    ("charan","math"),
    ("bobby","engl"),
    ("Alice","Maht")
]
unique_set = set()
for tup in info:
    unique_set.add(tup[1])
print(unique_set)

for name,course in info:
    print(name,course)

for name,course in info:
    if(course =="Maht"):
        print(name)
