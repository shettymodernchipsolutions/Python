# A Python program to define Student class and create an object to it.
# Also we will call the method and display the student's details.

class Student:
    def __init__(self):
        self.name = 'Vishnu'
        self.age = 21
        self.marks = 900

    def talk(self):
        print('Hi, my name is', self.name)
        print('My age is', self.age)
        print('I have scored', self.marks)


s1 = Student()
s1.talk()
