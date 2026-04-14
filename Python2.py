#conditional statement
'''
age = 1
if(age > 18):
    print("Adult")
elif age < 18 and age > 13 :
    print("Tenager")
else:
    print("Child")
'''
'''
username = input("Enter Username ")
password = input("Enter Password ")

if(username =="admin" and password == "pass"):
    print("LOGIN")
elif( username !="admin"):
    print("Wrong Username")
else:
    print("Wrong password")
'''

# num = int(input("Enter number "))
# if(num % 5 == 0 ):
#     print("Multiple of 5 ")
# else:
#     print("Not multiple of 5")

# num = int(input("Enter number :")) 
# if(num %2==0):
#     print("EVEN")
# else:
#     print("ODD")
#nesting

# username = input("Enter Username ")
# password = input("Enter Password ")

# if(username =="admin" and password == "pass"):
#     print("LOGIN")
# else:
#     if(username != "admin"):
#         print("Wrong username")
#     else:
#         print("Wrong password")

# match 

# color = input("Enter color")

# match color:
#     case "Green":
#         print("Go")
#     case "Yellow":
#         print("Watch")
#     case "Read":
#         print("Stop")
#     case _:
#         print("Wrong color")

#loops
# while True:
#     print("HII")

#while loop
'''
i=0
while(i<5):
    print("HII",i+1)
    i+=1
print(i)
# 1 to 5 print numbers
i=1
while(i<=5):
    print(i)
    i+=1
# reverse
i=5
while(i>0):
    print(i)
    i-=1
  
  '''

# n = int(input("Enter any number:-"))
# i=0
# while(i<10):
#     print(n*(i+1))
#     i+=1


# break
# i = 1
# while(i<=10):
#     if(i % 6 ==0):
#         break
#     print(i)
#     i+=1
# print("outside loop")

#continue
# i=1
# while(i<=10):
#     if(i%3==0):
#         i+=1
#         continue
#     print(i)
#     i+=1

# odd numbers

# i = 1
# while(i<=10):
#     print(i)
#     i+=2

# i = 0
# while(i<10):
#     i+=1
#     if(i%2==0):
        
#         continue
#     print(i)

# string="hello"

# if 'x' in string:
#     print("o exists in string")

# for var in string:
#     print(var,end='')
    
#number sequence

# for i in range(5):
#     print(i)

# word = "artificial intelliengce"
# count=0
# for i in word:
#     if(i=='i'):
#         count+=1
# print(count)

# word = "artificial"
# count = 0
# for ch in word:
#     if(ch=='i' or ch == 'o' or ch =='a' or ch =='e' or ch == 'u'):
#         count +=1
# print(count)

# for i in range(2,11,2):
#     print(i)

#sum of n natural numbers
# n = int(input("Enter any number"))
# sum = 0 
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# def first():
#     print("hii")
# first()
# #runction definition
# def sum(a,b):
#     return a+b
# #function call
# print(sum(5,4))

#avergae
# def average(a,b,c):
#     print((a+b+c)/3)
# average(3,5,2)

# def sum(a,b=2):
#     print(a+b)
# sum(5,4)
# sum(4)

# sum = lambda a,b,c : a+b+c
# print(sum(4,5,6))

#factorial
def fact(n):
    fact = 1
    for i in range(2,n+1):
        fact *= i
    return fact
print(fact(6))