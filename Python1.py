print("Hello \n World"+"This is next line")
print("HELLO","World")

#variables
#containers
name = "Bhushan"
age = 35
PI = 3.14

print(name,age,PI)

_name = "Bhushan "
_age = 35
_PI = 35


#data types

print(type(_PI))
print(type(_name))

isPrime = True
print(type(isPrime))
none = None
print(type(none))

#keywords
# reserved words
#False  = 23

#comments 
# use # 
#  Multiline comments
"""
This is multiline comments
"""
#style guide -> snake case
tot_price = 100

#WAP to calculate sum of two numbers

#operator
#arithmetic
a = 50
b = 8
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)
#relational
print(a<b)
print(a<=b)
print(a>b)
print(a>=b)
print(a==b)
print(a!=b)
#asignment
a=20
print(a)
a+=20
print(a)# *= -= += /= %= **= //=
#Logical
print(not False)
print(5>9 and 5<9)
print(5>9 or 5<9)

x = 3
x+= 5
print(x)

#operator precedance
'''
()
**
* / %
+ -
== != > >= < <=
not 
and
or

same precedance -> left to right solve
'''
#type conversion 
#1) automatic implicit type conversion
ans= 5+10.0
print(type(ans),ans)
#2) casting explicit 
ans2 = int(5+10.0)
print(type(ans2),ans2)

#input
'''a = input("Enter any name")
print("Welcome",a)'''
#sum
'''a = int(input("Enter a "))
b = int(input("Enter b "))
print(a+b)'''

#average

a = float(input("Enter 1st num "))
b = float(input("Enter 2nd num "))
print((a+b)/2)
