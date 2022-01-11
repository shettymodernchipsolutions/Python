# A Python program to define Student class and create an object to it.
# Also we will call the method and display the student's details.

# class Student:
#     def __init__(self):
#          self.name = 'Vishnu'
#          self.age = 20
#          self.marks = 900
#
#     def talk(self):
#         print('Hi, I am', self.name)
#         print('My age is', self.age)
#         print('My marks are', self.marks)
#
# s1 = Student()
#
# s1.talk()

# A Python program to create Student class with a constructor having more than one parameter.

# class Student:
#     def __init__(self, n = '.', m = 0):
#         self.name = n
#         self.marks = m
#
#     def display(self):
#         print('Hi', self.name)
#         print('Your marks', self.marks)
#
# s = Student('Arun', 878)
# s.display()
# print('--------------------------')
#
# s1 = Student('Lakshmi Roy', 880)
# s1.display()
# print('--------------------------')


# A Python program to understand instance variables.

# class Sample:
#     def __init__(self):
#         self.x = 10
#
#     def modify(self):
#         self.x += 1
#
# s1 = Sample()
# s2 = Sample()
# print('x in s1 = ', s1.x)
# print('x in s2 = ', s2.x)
#
# s1.modify()
# print('x in s1 = ', s1.x)
# print('x in s2 = ', s2.x)


# A Python program to understand class variables or static variables.

# class Sample:
#     x = 10
#
#     @classmethod
#     def modify(cls):
#         cls.x += 1
#
# s1 = Sample()
# s2 = Sample()
# print('x in s1 = ', s1.x)
# print('x in s2 = ', s2.x)
#
# s1.modify()
# print('x in s1 = ', s1.x)
# print('x in s2 = ', s2.x)


# A Python program using a student class with instance methods to process the data of several students.

# class Student:
#     def __init__(self, n='', m=0):
#         self.name = n
#         self.marks = m
#
#     def display(self):
#         print('Hi', self.name)
#         print('Your marks', self.marks)
#
#     def calculate(self):
#         if(self.marks >= 600):
#             print('You got first grade')
#         elif(self.marks >= 500):
#             print('You got second grade')
#         elif(self.marks >= 350):
#             print('You got third grade')
#         else:
#             print('You are failed')
#
# n = int(input('How many students? '))
#
# i = 0
# while(i < n):
#     name = input('Enter a name: ')
#     marks = int(input('Enter the marks: '))
#
#     s = Student(name, marks)
#     s.display()
#     s.calculate()
#     i += 1
#     print('--------------------------')


# A Python program to store data into instances using mutator methods and to retrieve data from instances
# using accessor methods.

# class Student:
#     def setName(self, name):
#         self.name = name
#
#     def getName(self):
#         return self.name
#
#     def setMarks(self, marks):
#         self.marks = marks
#
#     def getMarks(self):
#         return self.marks
#
# n = int(input('How many students? '))
#
# i = 0
# while(i < n):
#     s = Student()
#     name = input('Enter name: ')
#     s.setName(name)
#     marks = int(input('Enter marks: '))
#     s.setMarks(marks)
#
#     print('Hi', s.getName())
#     print('Your marks', s.getMarks())
#
#     i += 1
#     print('----------------------')

# A Python program to use class method to handle the  common feature of all the instances of Bird class.

# class Bird:
#     wings = 2
#
#     @classmethod
#     def fly(cls, name):
#         print('{} flies with {} wings'.format(name, cls.wings))
#
#
# Bird.fly('Sparrow')
# Bird.fly('Pigeon')


# A Python program to create static method that counts the number of instances created for a class.

# class Myclass:
#     n = 0
#
#     def __init__(self):
#         Myclass.n = Myclass.n + 1
#
#     @staticmethod
#     def noObjects():
#         print('No. of instances created: ', Myclass.n)
#
#
# obj1 = Myclass()
# obj2 = Myclass()
# obj3 = Myclass()
# Myclass.noObjects()

# A Python program to create a static method that calculates the square root value of a given number.

# import math
#
#
# class Sample:
#     @staticmethod
#     def calculate(x):
#         result = math.sqrt(x)
#         return result
#
#
# num = float(input('Enter a number: '))
#
# res = Sample.calculate(num)
# print('The square root of {} is {:.2f}'.format(num, res))

# A Python program to create a Bank class where deposits and withdrawals can be handled by using
# instance methods.

# import sys
#
#
# class Bank(object):
#     def __init__(self, name, balance=0.0):
#         self.name = name
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
#
#     def withdrawal(self, amount):
#         if amount > self.balance:
#             print('Balance amount is less, so no withdrawal')
#         else:
#             self.balance -= amount
#         return self.balance
#
#
# name = input('Enter a name: ')
# b = Bank(name)
#
# while (True):
#     print('d -Deposit, w -Withdraw, e -Exit')
#     choice = input('Your choice: ')
#     if choice == 'e' or choice == 'E':
#         sys.exit()
#
#     amt = float(input('Enter amount: '))
#
#     if choice == 'd' or choice == 'D':
#         print('Balance after deposit: ', b.deposit(amt))
#     elif choice == 'w' or choice == 'W':
#         print('Balance after withdrawal: ', b.withdrawal(amt))
#


# A Python program to define Student class and create an object to it.
# Also we will call the method and display student's details.

# class Student:
#     def __init__(self):
#         self.name = 'Vishnu'
#         self.age = 20
#         self.marks = 900
#
#     def talk(self):
#         print('Hi, my name is', self.name)
#         print('My age is', self.age)
#         print('I have scored', self.marks)
#
#
# s1 = Student()
#
# s1.talk()


# A Python program to create a Student class with a constructor having more than one parameter.

# class Student:
#     def __init__(self, name='Bhavesh', age=20, job='Software Developer'):
#         self.name = name
#         self.age = age
#         self.job = job
#
#     def talk(self):
#         print('Hi, my name is', self.name)
#         print('My age is', self.age)
#         print('I am a', self.job)
#
#
# print('-----------------------------')
# s1 = Student()
# s1.talk()
#
# print('-----------------------------')
# s1 = Student('Venkat', 28, 'Software Developer')
# s1.talk()
# print('-----------------------------')

# A Python program to understand instance method.

# class Sample:
#     def __init__(self):
#         self.x = 10
#
#     def modify(self):
#         self.x += 2
#
#
# s1 = Sample()
# s2 = Sample()
# print('Value of x = ', s1.x)
# print('Value of x = ', s2.x)
#
# s1.modify()
# print('Value of x = ', s1.x)
# print('Value of x = ', s2.x)

# A Python program to understand class variables or static variables.

# class Sample:
#     x = 10
#
#     @classmethod
#     def modify(cls):
#         cls.x += 2
#
#
# s1 = Sample()
# s2 = Sample()
#
# print("Value of s1 = ", s1.x)
# print("Value of s2 = ", s2.x)
#
# s1.modify()
#
# s1 = Sample()
# s2 = Sample()
#
# print("Value of s1 = ", s1.x)
# print("Value of s2 = ", s2.x)


# A Python program using a student class with instance methods to process the data of several students.

# class Student:
#     def __init__(self, n='', m=0):
#         self.name = n
#         self.marks = m
#
#     def display(self):
#         print('Hi', self.name)
#         print('Your marks is', self.marks)
#
#     def calculate(self):
#         if self.marks >= 600:
#             print('You got first grade.')
#         elif self.marks >= 450:
#             print('You got second grade.')
#         elif self.marks >= 350:
#             print('You got third grade.')
#         else:
#             print('You are failed.')
#
#
# n = int(input("Enter the number of students: "))
#
# i = 0
# while i < n:
#     name = input("Enter the name: ")
#     marks = int(input('Enter the marks: '))
#
#     s = Student(name, marks)
#     s.display()
#     s.calculate()
#     i += 1
# print('-----------------------------------------')

# A Python program to store data into instances using mutator methods and to retrieve data from the instances
# using accessor methods.

# class Student:
#     def setName(self, name):
#         self.name = name
#
#     def getName(self):
#         return self.name
#
#     def setMarks(self, marks):
#         self.marks = marks
#
#     def getMarks(self):
#         return self.marks
#
#
# n = int(input('Enter the number of students: '))
#
# i = 0
# while i < n:
#     s = Student()
#     name = input('Enter the name: ')
#     s.setName(name)
#     marks = int(input('Enter the marks: '))
#     s.setMarks(marks)
#
#     print('Hi', s.getName())
#     print('Your marks', s.getMarks())
#     i += 1
#
# print('-------------------------------------')

# A Python program to use class method to handle the common feature of all the instances of bird class.

# class Bird:
#     wings = 2
#
#     @classmethod
#     def fly(cls, name):
#         cls.name = name
#         print('{} flies with {} wings'.format(name, cls.wings))
#
#
# Bird.fly('Sparrow')
# Bird.fly('Pigeon')
#
#
# class Dog:
#     legs = 4
#
#     @classmethod
#     def run(cls, name):
#         cls.name = name
#         print('{} runs with {} legs'.format(name, cls.legs))
#
#
# Dog.run('Rottweiler')
# Dog.run('Dashchund')

# A Python program to create a static method that counts the number of instances created for a class.

# class Myclass:
#     n = 0
#
#     def __init__(self):
#         Myclass.n = Myclass.n + 1
#
#     @staticmethod
#     def noObjects():
#         print('The number instances created are: ', Myclass.n)
#
#
# obj1 = Myclass()
# obj2 = Myclass()
# obj3 = Myclass()
# obj4 = Myclass()
# obj5= Myclass()
# Myclass.noObjects()

# A Python program to create a static method that calculates the square value of a given number.

# import math
#
#
# class Sample:
#     @staticmethod
#     def calculate(x):
#         result = math.sqrt((x))
#         return result
#
#
# num = float(input('Enter a number: '))
#
# res = Sample.calculate(num)
# print('The square root of {} is {:.2f}'.format(num, res))

# A Python program to create a Bank class where deposits and
# withdrawal can be handled by using instance methods.

import sys


# class Bank:
#     def __init__(self, name, balance=0.0):
#         self.name = name
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print('Balance amount is less, so no withdrawal.')
#         else:
#             self.balance -= amount
#         return self.balance
#
#
# name = input('Enter the name: ')
# b = Bank(name)
#
# while True:
#     print('d -Deposit, w -Withdraw, e -Exit')
#     choice = input('Your choice: ')
#     if choice == 'e' or choice == 'E':
#         sys.exit()
#
#     amt = float(input('Enter amount: '))
#
#     if choice == 'd' or choice == 'D':
#         print('Balance after deposit: ', b.deposit(amt))
#     elif choice == 'w' or choice == 'W':
#         print('Balance after withdrawal: ', b.withdraw(amt))


































class Bank:
    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdrawal(self, amount):
        if self.balance > amount:
            print('Entered amount should be less than the balance.')
        else:
            self.balance -= amount
            return self.balance

name = input('Enter the name: ')
b = Bank(name)

while True:
    print('d -deposit, w -withdrwal, e -exit')
    choice = input('Enter the choice: ')
    if choice == 'e' or choice == 'E':
        sys.exit()

    amt = int(input('Enter the amount: '))
    if choice == 'd' or choice == 'D':
        print('Enter the amount to be deposited: ', b.deposit(amt))
    elif choice == 'w' or choice == 'W':
        print('Enter the withdrawal amount: ', b.withdrawal(amt))