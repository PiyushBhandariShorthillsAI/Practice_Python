# class Student:
#     name = "Karan"

# s1 = Student()
# print(s1.name)

# class Car:
#     color = "Blue"

# Constructor

# class Student:
#     # name = "Karan"
#     def __init__(self, name, marks):
#             self.name = name
#             self.marks = marks
#             # print(self)
#             print("adding new studetn in the database..")

# s1 = Student("karan", 92) 
# print(s1.name, s1.marks)

# s2 = Student("Piyush", 93)
# print(s2.name, s2.marks)
# print(s2)


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod
#     def hello():
#         print("Hello")

#     def avg(self):
#         sum = 0
#         for value in self.marks:
#             sum += value
#         print(self.name, "your average score is" , sum/3)

# s1 = Student("Piyush", [92,93,88])
# s1.hello()
# s1.avg()

# class Account:

#     def __init__(self, balance, accountNo):
#         self.balance = balance
#         self.accountNo = accountNo

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "debited")

#     def credit(self,amount):
#         self.balance += amount
#         print("Rs.", amount, "credited")

#     def get_balance(self):
#         return self.balance


# acc1 = Account(10000, 9875366356)
# print(acc1.balance)
# acc1.debit(3000)
# acc1.credit(5000)
# print(acc1.get_balance())


# del keyword

# class Student:
#     def __init__(self,name) -> None:
#         self.name = name

# s1 = Student("Piyush")
# print(s1.name)
# del s1.name
# print(s1.name)

# private attributes
# __ we can make any attribute private by putting two underscores in it

#  Inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stoppped..")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Prius")

# car1.start()

# classmethod

# class Person:
#     name = "anonymous"

#     # def changeName(self, name):
#     #     self.__class__.name = name

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName("Rahul")
# print(p1.name)
# print(Person.name)


# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

    # def claPercentage(self):
    #     self.percentage = str((self.phy+self.chem+self.math)/3) + "%"
    #     return self.percentage

#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)/3) + "%"

# s1 = Student(98,93,91)
# print(s1.percentage)

# s1.phy = 88
# print(s1.percentage)

# # s1.claPercentage()
# print(s1.claPercentage())
 

#  polyphormism
# operator overloading
  
# def add(a, b):
     
#     """
#     Adds two numbers and returns the result.
    
#     Parameters:
#     a (int, float): The first number.
#     b (int, float): The second number.
    
#     Returns:
#     int, float: The sum of a and b.
#     """
#     return a+b

# print(add.__doc__)

# import sys
# # print(sys.__dict__.keys())

# print(sys.ps1)


# a = 15
 
 
# # function to change a global value
# def change():
#     # increment value of a by 5
#     a = 5
#     print(a)

# change()
# print(a) 

# def myfunc1():
#   x = "John"
#   def myfunc2():
#     x = "hello"
#   myfunc2()
#   return x

# print(myfunc1())

