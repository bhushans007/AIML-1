# class Student:
#     subject = "Python"
#     college="ABC"
#     year = "4th Year"

#     #constructor
#     def __init__(self):
#         print("This is constructor")
#         print(self.subject)

    

# s1 = Student()
# s2 = Student()
# s3 = Student()


# print(s1.subject)
# print(s2.college)
# print(s3.year)
# print(type(s1))


# class Student:
    
#     #constructor
#     def __init__(self,name,cgpa):#parametrized constructor but only one constructor at a time
#         self.name = name
#         self.cgpa = cgpa
    
#     def get_cgpa(self):
#         return self.cgpa

# s1 = Student("Rahul",9.0)
# s2 = Student("Bhushan",8.0)
# s3 = Student("Om",10.0)

# print(s1.name)
# print(s3.name)
# print(s2.name)

# print(s1.get_cgpa())
# print(f"{s1.name} has cgpa = {s1.get_cgpa()}")

# class Student:
#     college_name="ABC college"
#     PI = 3.124

#     def __init__(self,name,gpa,PI):
#         self.name = name
#         self.gpa = gpa
#         self.PI = PI
# s1  = Student("Rahul",9.2,3.1)
# print(s1.name)
# print(s1.college_name)
# print(Student.college_name)#instance have higher prrority

# print(s1.PI)
# print(Student.PI)

# class Laptop:
#     storage_type = "ssd"


#     def __init__(self,RAM,Storage):
#         self.RAM = RAM
#         self.Storage = Storage
#     @classmethod
#     def get_storage_type(cls):
#         print(f"storage type ={cls.storage_type}")
#         #print(cls.RAM) can't access objects or instance variable or methods

#     @staticmethod
#     def calc_discount(price,discount):
#         final_price = price - (discount * price/100)
#         print(f"discounted price = {final_price}")

#     def get_info(self):
#         print(f"laptop has {self.RAM} RAM & {self.Storage}  & storage type = {self.storage_type}")

# l1 = Laptop("16gb","512gb")
# l2 = Laptop("8gb","256gb")

# l1.get_info()
# l2.get_storage_type()
# Laptop.get_storage_type()

# l1.calc_discount(40_000, 10)

# class Product:
#     count = 0 
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price

#         Product.count +=1
    
#     def get_info(self):
#         print(f"price of {self.name} is Rs.{self.price}")

#     @classmethod
#     def total_products(cls):
#         print(f"total products = {cls.count}")

#     @staticmethod
#     def cal_discount(price,percentage):
#         print(f"discounted price ={price - (price*percentage/100)}")
# p1 = Product("phone",10_000)
# p2 = Product("Laptop",50_000)
# p3 = Product("Pen",10)

# p1.get_info()
# p2.get_info()
# p3.get_info()

# p3.total_products()
# Product.total_products()

# p1.cal_discount(10_000,2)
# p2.cal_discount(p2.price,10)


# OOP - Encapsulation
# class Bank_account:
#     def __init__(self, name, balance,mpin):
#         self.name = name#public
#         self._balance = balance #protected
#         self.__mpin = mpin #private
#     def get_balance(self):
#         return self.__mpin
    
#     def set_balance(self,newBalance):
#         self.__mpin = newBalance

# acc1 = Bank_account("Rahul Kumar",100_000,4000)

# print(acc1.name,acc1._balance)
# acc1.set_balance(5000)#setter
# print(acc1.get_balance())#getter

# print(acc1._Bank_account__mpin)

#Inheritance

# class Employee:
#     start_time = "10am"
#     end_time = "6pm"

#     def change_time(self,new_end_time):#method
#         self.end_time = new_end_time

# class Teacher(Employee):
#     def __init__(self,subject):
#         self.subject = subject

# class Admin_staff(Employee):
#     def __init__(self,role):
#         self.role = role

# class Accountant(Admin_staff):

#     def __init__(self,salary,role):
#        super().__init__(role)
#        self.salary = salary

# t1 = Teacher("Math")
# t1.change_time("7pm")
# print(t1.subject,t1.start_time,t1.end_time)

# s1 = Admin_staff("manager")
# print(s1.start_time,s1.end_time,s1.role)

# a1 = Accountant(25_000,"CA")
# print(a1.role,a1.salary,a1.start_time,a1.end_time)

# class Teacher:
#     def __init__(self,salary):
#         self.salary = salary

# class Student:
#     def __init__(self,gpa):
#         self.gpa = gpa

# class TA(Teacher,Student):
#     def __init__(self,salary,gpa,name):
#         super().__init__(salary)#default first class as Teacher as a parameter
#         Student.__init__(self,gpa)
#         self.name = name

# ta1 = TA(15_000,9.3,"Shraddha")
# print(ta1.name, ta1.gpa, ta1.salary)

#abstraction
# from abc import ABC,abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
# class Lion(Animal):
#     def make_sound(self):
#         print("Roar")

# class Cow(Animal):
#     def make_sound(self):
#         print("MOO!!")

# L1 = Lion()
# L1.make_sound()

# C1 = Cow()
# C1.make_sound()

#polymorphism

#function overriding

# class Employee:
#     def get_designation(self):
#         print("designation = Employee")
# class Teacher(Employee):
#     def get_designation(self):
#         print("designation = Teacher")
# t1 = Teacher()
# t1.get_designation()

#duck typing
class Teacher():
    def get_designation(self):
        print("designation = Teacher")

class Accountant():
    def get_designation(self):
        print("designation = Accountant")
t1 = Teacher()
t1.get_designation()
a1 = Accountant()
a1.get_designation()