# class FootBaller:
#
#     def __init__(self, name, team, goals):
#         self.name = name
#         self.team = team
#         self.goals = goals
#
#     def shooting(self):
#         print(self.name,'is shooting')
#
#     def passing(self):
#         print(self.name,'is passing')
#
#     def running(self):
#         print(self.name,'is running')
#
# def main():
#     cr = FootBaller('Cristiano','Juventus', 746)
#     print(cr.name)
#     print(cr.team)
#     print(cr.goals)
#     cr.shooting()
#     cr.passing()
#     cr.running()
#
#     messi = FootBaller('Messi', 'Barcelona', 700)
#     print(messi.name)
#     print(messi.team)
#     print(messi.goals)
#     messi.shooting()
#     messi.passing()
#     messi.running()
#
# if __name__ == '__main__':
#     main()

# class FootBaller:
#
#     def __init__(self, name, team, goals):
#         self.name = name
#         self.team = team
#         self.goals = goals
#
#     def shooting(self):
#         print(self.name,'is shooting')
#
#     def passing(self):
#         print(self.name,'is passing')
#
#     def running(self):
#         print(self.name,'is running')
#
#     def display(self):
#         print(self.name)
#         print(self.team)
#         print(self.goals)
#
# def main():
#     cr = FootBaller('Cristiano','Juventus', 746)
#     cr.display()
#     cr.shooting()
#     cr.passing()
#     cr.running()
#
#     messi = FootBaller('Messi', 'Barcelona', 700)
#     messi.display()
#     messi.shooting()
#     messi.passing()
#     messi.running()
#
# if __name__ == '__main__':
#     main()

# class FootBaller:
#
#     def __init__(self, name, team, goals):
#         self.name = name
#         self.team = team
#         self.goals = goals
#
#     def shooting(self):
#         print(self.name,'is shooting')
#
#     def passing(self):
#         print(self.name,'is passing')
#
#     def running(self):
#         print(self.name,'is running')
#
#     def display(self):
#         print(self.name)
#         print(self.team)
#         print(self.goals)
#         print(self.age)
#         print(self.jersey_no)
#
# def main():
#     cr = FootBaller('Cristiano','Juventus', 746)
#     cr.age = 35
#     cr.jersey_no = 7
#     cr.display()
#     cr.shooting()
#     cr.passing()
#     cr.running()
#
# if __name__ == '__main__':
#     main()

# class FootBaller:
#
#     def __init__(self, name, team, goals):
#         self.name = name
#         self.team = team
#         self.goals = goals
#
#     def shooting(self):
#         print(self.name,'is shooting')
#
#     def passing(self):
#         print(self.name,'is passing')
#
#     def running(self):
#         print(self.name,'is running')
#
#     def display(self):
#         print(self.name)
#         print(self.team)
#         print(self.goals)
#         print(self.age)
#         print(self.jersey_no)
#
# def main():
#     cr = FootBaller('Cristiano','Juventus', 746)
#
#     setattr(cr,'age',35)
#     setattr(cr,'jersey_no',7)
#
#     cr.display()
#     cr.shooting()
#     cr.passing()
#     cr.running()
#
# if __name__ == '__main__':
#     main()

# class FootBaller:
#
#     def __init__(self, name, team, goals):
#         self.name = name
#         self.team = team
#         self.goals = goals
#
#     def shooting(self):
#         print(self.name,'is shooting')
#
#     def passing(self):
#         print(self.name,'is passing')
#
#     def running(self):
#         print(self.name,'is running')
#
#     def display(self):
#         print(self.name)
#         print(self.team)
#         print(self.goals)
#         print(self.age)
#         print(self.jersey_no)
#
# def main():
#     cr = FootBaller('Cristiano','Juventus', 746)
#
#     setattr(cr,'age',35)
#     setattr(cr,'jersey_no',7)
#
#     print(cr.name)
#     print(getattr(cr,'name'))
#
#     print(hasattr(cr, 'name'))
#     print(hasattr(cr, 'gender'))
#
# if __name__ == '__main__':
#     main()

# class FootBaller:
#
#     def __init__(self, name, team, goals):
#         self.name = name
#         self.team = team
#         self.goals = goals
#
#     def shooting(self):
#         print(self.name,'is shooting')
#
#     def passing(self):
#         print(self.name,'is passing')
#
#     def running(self):
#         print(self.name,'is running')
#
#     def display(self):
#         print(self.name)
#         print(self.team)
#         print(self.goals)
#         print(self.age)
#         print(self.jersey_no)
#
# def main():
#     cr = FootBaller('Cristiano','Juventus', 746)
#
#     setattr(cr,'age',35)
#     setattr(cr,'jersey_no',7)
#
#     print(cr.__dict__)
#     print(cr.name)
#     print(cr.__dict__['name'])
#
# if __name__ == '__main__':
#     main()

# class Citizens:
#
#     def __init__(self, name, age, gender, state, nationality):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.state = state
#         self.nationality = nationality
#
#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.gender)
#         print(self.state)
#         print(self.nationality)
#
# def main():
#     Rohith = Citizens('Rohith', 28, 'M', 'Kar', 'Ind')
#     Swathi = Citizens('Swathi', 27, 'F', 'Kar', 'Ind')
#     Rita = Citizens('Rita', 25, 'F', 'Kar', 'Ind')
#
#     Rohith.display()
#     Swathi.display()
#     Rita.display()
#
# if __name__ == '__main__':
#     main()

# class Citizens:
#
#     def __init__(self, name, age, gender, state, nationality):
#
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.state = state
#         self.nationality = nationality
#
#     def display(self):
#
#         print(self.name)
#         print(self.age)
#         print(self.gender)
#         print(self.state)
#         print(self.nationality)
#
# def main():
#     rohith = Citizens('Rohith', 28, 'M', 'Kar', 'Ind')
#     swathi = Citizens('Swathi', 27, 'F', 'Kar', 'Ind')
#     rita = Citizens('Rita', 26, 'F', 'Kar', 'Ind')
#
#     rohith.display()
#     swathi.display()
#     rita.display()
#
# if __name__ == '__main__':
#     main()

# classmethod() in Python:
"""The classmethod() is an inbuilt function in Python, which returns a class method for a given function.

Syntax: classmethod(function)"""

"""
Parameter :This function accepts the function name as a parameter.
Return Type:This function returns the converted class method.
Syntax: 

@classmethod
   def fun(cls, arg1, arg2, ...):


   Where, 

fun: the function that needs to be converted into a class method
returns: a class method for function.
classmethod() methods are bound to a class rather than an object.
 Class methods can be called by both class and object.
 These methods can be called with a class or with an object. 
"""

"""
Class method vs Static Method:

A class method takes cls as the first parameter while a static method needs no specific parameters.
A class method can access or modify the class state while a static method can’t access or modify it.
In general, static methods know nothing about the class state. They are utility-type methods that take 
some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
We use @classmethod decorator in python to create a class method and we use @staticmethod decorator 
to create a static method in python.

"""

"""
Example 1: Create a simple classmethod:

In this example, we are going to see a how to create classmethod, for this we created a class
 with geeks name with member variable course and created a function purchase which prints the object.

Now we passed the method geeks.purchase into classmethod which converts the methods to 
a class method and then we call the class function purchase without creating a function object.

"""

"""
class geeks:
    course = 'DSA'

    def purchase(obj):
        print("Puchase course : ", obj.course)


geeks.purchase = classmethod(geeks.purchase)
geeks.purchase()
"""

"""
Example 2: Create class method using classmethod():

# Python program to understand the classmethod

class Student:

    # create a variable
    name = "Geeksforgeeks"

    # create a function
    def print_name(obj):
        print("The name is : ", obj.name)


# create print_name classmethod
# before creating this line print_name()
# It can be called only with object not with class
Student.print_name = classmethod(Student.print_name)

# now this method can be called as classmethod
# print_name() method is called a class method
Student.print_name()
"""
# Example 3: Factory method using Class method:
"""
# Python program to demonstrate
# use of a class method and static method.
from datetime import date

class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    def display(self):
        print("Name : ", self.name, "Age : ", self.age)

person = Person('mayank', 21)
person.display()
"""
"""The @classmethod Decorator:

The @classmethod decorator is a built-in function decorator which is an expression that gets
 evaluated after your function is defined. The result of that evaluation shadows your function definition. 
A class method receives the class as the implicit first argument, just like an instance method 
receives the instance.

 Syntax:

class C(object):
    @classmethod
    def fun(cls, arg1, arg2, ...):
       ....
"""

"""Where,

fun: the function that needs to be converted into a class method
returns: a class method for function.
Note:

A class method is a method which is bound to the class and not the object of the class.
They have the access to the state of the class as it takes a class parameter
that points to the class and not the object instance.
It can modify a class state that would apply across all the instances of the class. For example, it can 
modify a class variable that would be applicable to all the instances."""

"""
# Python program to demonstrate
# use of a class method and static method.
from datetime import date

class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a
    # Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18

person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))
"""

'''
class Class:
    pass
    # STATE
        # ==> Fields(1,2)  which represents data

        1. Class variables
        2. Instance variables
        3. local variables

    # BEHAVIOR
        # ==> Methods which represents implementation

       1. Class Method
       2. Instance Method
       3. Static method
'''


# Get employee count at a given point of time.


class Employee:
    comp = 'ORACLE'  # sharing
    emp_count = 0  # sharing + Modifying

    def _init_(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal
        Employee.emp_count += 1

    # instance method(can access instance,class variables)
    def get_edata(self):
        print("Employee information : ", self.eid, self.name, self.sal)

    # class method (can access only class variables)
    @classmethod
    def get_ecount(cls):
        print("Employee count : ", cls.comp, " -- ", cls.emp_count)


Employee.get_ecount()
madhu = Employee(100, 'Madhu N', 10000)
madhu.get_edata()  # instance method ==> Employee.get_edata(madhu)
Employee.get_ecount()  # class method    ==> Employee.get_ecount(Employee)

# To call class method, we can call using object,But don't do it.
# madhu.get_ecount()

jaya = Employee(101, 'Jayadeep  Chowdary A', 20000)
jaya.get_edata()
Employee.get_ecount()

mohan = Employee(102, 'Mohan Kumar', 45000)
mohan.get_edata()
Employee.get_ecount()

'''
btech : stu_id, name, marks ==> instance variables
        college name        ==> class variables(share)
        attendance          ==> class variable (share+Modify)


employees : eid,name,sal   Instance vars  UNIQUE(INDIVIDUAL DATA)
            comp_name      class vars     SHARABLE to all employees
            emp_count      class vars     SHARABLE + MODIFY
            attendance     class vars     SHARABLE + MODIFY 



class variables    : data which is sharable to all objects
                     data which is SHARE + MODIFY actions
class methods      : 1. To act only on class variables


instance variables : data is unique for each object 
instance methods   : 1. To act only on instance variables OR 
                     2. Both instance and class variables



CV   - ClassMethod, InstanceMethod 
IV   - InstanceMethod

'''


class Sample:
    bank_name = 'icici'

    def get_data(self):
        self.bank_name = 'axis'
        print(self.bank_name)


s = Sample()
print(dir(s))
s.get_data()
s.bank_name = 'axis'
print(dir(s))
s.get_data()
[10: 44
AM, 11 / 7 / 2021] Katta
Satish
Babu: '''
Instance variables
Instance methods
'''

"""Instance method in Python
A class is a user-defined blueprint or prototype from which objects are created.
Classes provide a means of bundling data and functionality together.
Creating a new class creates a new type of object, allowing new instances of that type to be made. 
Each class instance can have attributes attached to it for maintaining its state. 
Class instances can also have methods (defined by its class) for modifying its state.

Instance Method
Instance attributes are those attributes that are not shared by objects. Every object
has its own copy of the instance attribute.
For example, consider a class shapes that have many objects like circle, square,
triangle, etc. having its own attributes and methods. An instance attribute refers to the
properties of that particular object like edge of the triangle being 3, while the edge of
the square can be 4.
An instance method can access and even modify the value of attributes of an instance.
It has one default parameter:-
self – It is a keyword which points to the current passed instance. But it need not be
passed every time while calling an instance method.

"""
"""class shape:
# Instance Method

     def finEdges(self):
      return self.edge

# Instance Method

     def modifyEdges(self, newedge):
      self.edge = newedge
# Driver Code
circle = shape(0, 'red')
square = shape(4, 'blue')
# Calling Instance Method
print("No. of edges for circle: "+ str(circle.finEdges()))
# Calling Instance Method
square.modifyEdges(6)
print("No. of edges for square: "+ str(square.finEdges()))"""

"""# Python program to demonstrate
# classes  

class Person:  

    # init method or constructor   
    def _init_(self, name):  
        self.name = name  

    # Sample Method   
    def say_hi(self):  
        print('Hello, my name is', self.name)  

p = Person('Nikhil')  
p.say_hi() 
"""
'''
def func1():
    print("Funciton1 body")

func1()

class Employee:
    # local variables   - eid, name, sal
    # instance variables - self.eid self.name self.sal - instance variables

    def _init_(self, eid, name, sal):
        print("Self address : ", self)
        self.eid = eid
        self.name = name
        self.sal = sal

    # instance methods
    def get_edata(self):
        print("Employee information : ", self.eid, self.name, self.sal)


venkat = Employee(100, 'satsh', 15000)
venkat.get_edata()  # Employee.get_edata(madhu)




li1 = [1, 2, 3]  # list1 is of type class list
li1.append(100)  # list.append(li1,100)
li1.pop()        # list.pop(li1)
'''
[10: 44
AM, 11 / 7 / 2021] Katta
Satish
Babu:  # Constructors in Python

"""Constructors are generally used for instantiating an object. The task of constructors is
to initialize(assign values) to the data members of the class when an object of the
class is created. In Python the _init_() method is called the constructor and is always
called when an object is created.
Syntax of constructor declaration :
def _init_(self):
# body of the constructor
Types of constructors :

Attention geek! Strengthen your foundations with the Python Programming
Foundation Course and learn the basics.
To begin with, your interview preparations Enhance your Data Structures concepts
with the Python DS Course. And to begin with your Machine Learning Journey, join
the Machine Learning - Basic Level Course

default constructor: The default constructor is a simple constructor which doesn’t
accept any arguments. Its definition has only one argument which is a reference to
the instance being constructed.

parameterized constructor: constructor with parameters is known as
parameterized constructor. The parameterized constructor takes its first argument
as a reference to the instance being constructed known as self and the rest of theparameterized constructor
"""
"""
Features of Python Constructors: 

In Python, a Constructor begins with double underscore () and is always named as __init_().
In python Constructors, arguments can also be passed.
In Python, every class must necessarily have a Constructor.
If there is a Python class without a Constructor, a default Constructor is automatically created without any arguments and parameters."""
"""
Counting the number of objects of a class
The constructor is called automatically when we create the object of the class. Consider the following example."""
"""
class Student:    
    count = 0    
    def _init_(self):    
        Student.count = Student.count + 1    
s1=Student()    
s2=Student()    
s3=Student()    
print("The number of students:",Student.count)    
"""


class Employees():

    def _init_(self, Name, Salary):
        self.Name = Name
        self.Salary = Salary

    def details(self):
        print("Employee Name : ", self.Name)
        print("Employee Salary: ", self.Salary)
        print("\n")


first = Employees("Khush", 10000)
second = Employees("Raam", 20000)
third = Employees("Lav", 10000)
fourth = Employees("Sita", 30000)
fifth = Employees("Lucky", 50000)

first.details()
second.details()
third.details()
fourth.details()
fifth.details()
"""
"""


class Employee:
    def _init_(self, name, id):
        self.id = id
        self.name = name

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))


emp1 = Employee("John", 101)
emp2 = Employee("David", 102)

# accessing display() method to print employee 1 information

emp1.display()

# accessing display() method to print employee 2 information
emp2.display()
"""
class GeekforGeeks:

# default constructor
      def _init_(self):
        self.geek = "GeekforGeeks"
# a method for printing data members
         def print_Geek(self):
print(self.geek)
# creating object of the class
obj = GeekforGeeks()
# calling the instance method using the object obj
obj.print_Geek()"""


class Employee:
    pass


'''
converts as below
                        class Employee:
                            def _init_(self):
                                pass
'''
print("Employee class @ ", Employee)
obj = Employee()


# Default constructor
class Employee:

    def _init_(self):  # Default constructor
        pass  # to perform any generic action

    def getedata(self, eid, sal):
        print("Employee Data", eid, sal)


venkat = Employee()
venkat.getedata(101, 10000)  # Employee.getedata(madhu,101,10000)

# while defining class, default constructor is not mandatory. Python give automatically


# Employee CRUD Operations

'''
REQUIREMENT :
1. Create an employee with eid,name,sal  #
2. Retrieve emp details 
3. Give hike for employee based on experience
    Acceptance Criteria : 0 to 2 exp  => 5% hike
                          2 to 3 exp  => 10% hike
                          3 to 5 exp  => 20% hike
                          5+          => 30% hike

4. Delete emp once he exits from company

GUI  -->  Backend             ---> Database

UI  --->  Python/Java/.Net    --->  Oracle/Postgresql/Mysql/Mongodb
'''

print("-----------Employee hike---------------")


class Employee:
    # create employee
    def _init_(self, eid, name, sal):  # emailid,mobiileno,perm_address,pre_add,joining_date,bloodgr,gendder
        self.eid = eid
        self.name = name
        self.sal = sal

    # 2. Retrieve emp details
    def get_emp_info(self):
        print("Employee details : ", self.eid, self.name, self.sal)

    # 3. Update emp sal based on exp
    '''
        3. Give hike for employee based on experience
        Acceptance Criteria : 0 to 2 exp  => 5% hike
                              2 to 3 exp  => 10% hike
                              3 to 5 exp  => 20% hike
                              5+          => 30% hike
    '''

    def update_emp_sal(self, exp):
        # Server validations
        if exp < 0:
            print("Please enter valid experience.")
            return None
        if exp >= 0 and exp < 2:
            hike = (self.sal * 5) // 100
            self.sal = self.sal + hike
        elif exp >= 2 and exp < 3:
            hike = (self.sal * 10) // 100
            self.sal = self.sal + hike
        elif exp >= 3 and exp < 5:
            hike = (self.sal * 20) // 100
            self.sal = self.sal + hike
        elif exp >= 5:
            hike = (self.sal * 30) // 100
            self.sal = self.sal + hike
        print("Employee  after hike : ", self.eid, self.name, self.sal)

    def delete_emp(self):
        pass


# Data hard coding
satish = Employee(100, 'satish', 1500000)
satish.get_emp_info()
satish.update_emp_sal(4)

'''
UI PAGE:
---------
EmmpID: 101
name  : satish
exp   : -10 
Mobileno : 34232443243

# client validations 
# server validations
'''
[10: 44
AM, 11 / 7 / 2021] Katta
Satish
Babu: """Python Parameterized Constructor:

The parameterized constructor has multiple parameters along with the self.
"""
"""class Student: 

    # Constructor - parameterized  
    def _init_(self, name):  
        print("This is parametrized constructor")  
        self.name = name  
    def show(self):  
        print("Hello",self.name)  
student = Student("John")  
student.show()
 """
# Positional arguments

"""
class Employee:
    # Parameterized Constructor
    def _init_(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def getedata(self):
        pass

satish = Employee(200, 'satish', 10000)
"""

'''
# Defining Constructor
    - Default constructor
    - Parameterized constructor
            - Positional arguments
            - Default arguments
            - keyword arguments

'''
# Default arguments example
"""
class Employee:
    # parameterized constructors
    def _init_(self, eid=None, name=None, sal=None):  # Constructor overloading
        self.eid = eid
        self.name = name
        self.sal = sal

    def getedata(self):
        print("Employee info : ", self.eid, self.name, self.sal)


satish = Employee()
satish.getedata()

sam = Employee(201)
sam.getedata()

venkat = Employee(201, 'Chandra Sekhar')
venkat.getedata()

ravi = Employee(200, 'MadhuN', 10000)
ravi.getedata()

raju= Employee(name='Farooq', sal=20000)
raju.getedata()


class Student:
    def _init_(self):
        print("The First Constructor")

    def _init_(self):
        print("The second contructor")


st = Student()  
"""
"""
lass Student:  
    def _init_(self, name, id, age):  
        self.name = name  
        self.id = id  
        self.age = age  

    # creates the object of the class Student  
s = Student("John", 101, 22)  

# prints the attribute name of the object s  
print(getattr(s, 'name'))  

# reset the value of attribute age to 23  
setattr(s, "age", 23)  

# prints the modified value of age  
print(getattr(s, 'age'))  

# prints true if the student contains the attribute with name id  

print(hasattr(s, 'id'))  
# deletes the attribute age  
delattr(s, 'age')  

# this will give an error since the attribute age has been deleted  
print(s.age)  
"""

"""
class Student:    

    def _init_(self,name,id,age):    
        self.name = name;    
        self.id = id;    
        self.age = age    

    def display_details(self):    
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id))

s = Student("John",101,22)    
print(s._doc_)    
print(s._dict_)    
print(s._module_) 
"""
[10: 44
AM, 11 / 7 / 2021] Katta
Satish
Babu: '''
Self:
--> Self is key word which represents the instance of the class.
--> By using the “self” keyword we can access the attributes and methods of the
 class in python
--> Self is a object which wraps the instance variables.
--> Self is a Special parameter.
--> We should declare instance methods or function using self parameter only
'''


# Ex:


class Person:

    def _init_(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)

p1.myfunc()

'''
Self:
--> Self is key word which represents the instance of the class.
--> By using the “self” keyword we can access the attributes and methods of the
 class in python
--> Self is a object which wraps the instance variables.
--> Self is a Special parameter.
--> We should declare instance methods or function using self parameter only
'''


# Ex:


class Person:

    def _init_(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)

p1.myfunc()
[10: 44
AM, 11 / 7 / 2021] Katta
Satish
Babu: '''
Class Variable:
--> The Variable which is created inside the class.

--> We can access the class variable anywhere in the class and any method
inside the class can access the class variable.

--> The better way to access the Class variable is "class name.variable name"

--> But we can also access the variable using self keyword too.
"self.variable name"

'''


class Addition:

    def _init_(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        add1 = self.a + self.b + self.c
        return add1


x = Addition(20, 30, 40)
print("The addition".ljust(40, '.'), ':', x.add())


class Addition:
    d = 40  # Class Variable

    def _init_(self, a, b, c):
        self.a = a  # Instance Variable
        self.b = b  # Instance Variable
        self.c = c  # Instance Variables

    def add(self):  # Instance Method
        add1 = self.a + self.b + self.c + Addition.d
        # Class Variable accessing Method 1
        return add1


x = Addition(20, 30, 40)
print("The addition".ljust(40, '.'), ':', x.add())


class Addition:
    d = 50

    def _init_(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        add1 = self.a + self.b + self.c + self.d
        '''self.d --> since its a Class Variable so we can access this using 
        self object'''
        return add1


x = Addition(20, 30, 40)
print("The addition".ljust(40, '.'), ':', x.add())


class Addition:
    d = 70
    e = 80

    def _init_(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        add1 = self.a + self.b + self.c
        return add1

    @classmethod
    def getadd(cls):  # --> This is the syntax to get the class method
        add2 = Addition.d + Addition.e
        return add2


x = Addition(20, 30, 40)
print("The addition".ljust(40, '.'), ':', x.add() + x.getadd())
print("Hello Everyone".ljust(40, '.'), ': ', x.add())
[10: 44
AM, 11 / 7 / 2021] Katta
Satish
Babu: str1 = "Madhu"  # str("Madhu")

"""Student
------------
 IV : r_no name   marks   percentage   section   fee    student_address

 CV : school_name school_address student_count


Instance variable : Individual to each object
Class variable : Sharable and modifiable by all objects


CV  ----> CM
IV  ----> IM

CV  ----> IM  Correct
IV  ----> CM  XXX

'''
'''
STATE 
 - Fields
    - Class variables 
    - Instance variables 

BEHAVIOR
 - Methods
    - Class method
    - Instance method
    - Static method

STATE  - BEHAVIOR
Fields - Methods

OOPs concepts:
--------------------
Class Object
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction


Encapsulation :  Binding the data members and 
                             member methods into single entity
                - data members   ==> fields
                - member methods ==> methods                   object   Methods     Fields


                Ex: Class, object

                             Logical     Physical
Class    Fields      Methods

Abstraction    : Hiding implementation details and exposing only method signature 

Abstraction   :      Class          -  0% abstraction
                     Abstract class -  0% to 100% abstraction
                     Interface      - 100%  abstraction 



class,object

1. Encapsulation :
-----------------
Definition: Binding the data members & member methods into single entity

entity         : class/object
data members   : Fields/Variables/Attributes  (class,instance variables)
member methods : Methods (Instance Methods,Class Methods,Static Methods)

madhu = Employee(100,'satish, 15000)

Class  ===> Logical  -- DATA    Physical -- METHODS
Object ===> Physical -- DATA    Logical  -- METHODS (Through method access)

Ex : class is an example for encapsulation
     object is also an example


madhu = Employee1(100,"satish",15000)

2. Abstraction :
---------------
Hiding the implementation details in the methods of  a class

In a "Normal class" Abstraction is 0%        # all concrete methods
In "Abstract Class" Abstraction is 0-100 %   # 1. all concrete methods,
                                               2. all abstract methods
                                               3. Comb of concrete+abstract methods
In an "Interface"   Abstraction is 100%      # all abstract methods

During inheritance : Normalclass,

3. Inheritance :
---------------
super class, sub class mechanism

4. Polymorphism :
---------------
    - Static Polymorphism  -- Method overloading
    - Dynamic Polymorphism -- Method overriding

'''

'''
 1. Class Defined and provided special method i.e, 
   _init_(constructor) method to initialize instance variables, 
    define respective methods to get the BEHAVIOR
2.  Create object for the respective class.
        Internally 
         Python creates empty object for us,and gives reference to self parameter
         Reamining parameters, we are passing the arguments
         In empty object, instance variables will be initialized with the given data
3. Finally whole object reference will be given to LHS
4. We can perform method calls using created object       
'''

'''
class var                  instance var
-------------------------- ----------------------------
while loading class        at the time of object creation

class var                  instance var
class methods              instance methods

instance variables cant be used inside class method**

++ Within instance methods we can use class variables***
viceversa is not True ==> within class methods we can't use instance varibales
'''

class Employee:
    '''This class give details about employee'''
    def _init_(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def get_data(self):
        print("Employee data : ", self.eid, self.name, self.sal)

# Built in class attributes '''
print("Employee._dict:", Employee.dict_)
print("Employee._name:", Employee.name)print("Employee.doc:", Employee.doc_)

print("Employee._module:", Employee.module_)
print("Employee._bases:", Employee.bases_)

# CRUD - Create Retrieve Update Delete

satish = Employee(100, "satish", 10000)  # CREATE


setattr : To set IV value inside object  # UPDATE
getattr : To retrieve IV value           # RETRIEVE 
hasattr : To check IV has specific value # RETRIEVE
delattr : To delete IV                   # DELETE   

# getter - RETRIEVE
print("satish name :", getattr(satish, "name"))
print("satish eid  :", getattr(satish, "eid"))
# print("satish addr  :", getattr(satish, "addr"))

# setter - UPDATE
print("Setting name :", setattr(satish, "name", "MAD"))
print("Setting eid  :", setattr(satish, "eid", 200))
print("Setting addr :", setattr(satish, "address", 'Bangalore'))

print("Get name:", getattr(satish, "name"))
print("Get eid :", getattr(satish, "eid"))
print("Get addr:", getattr(satish, "address"))

print("Has attr sal :", hasattr(satish, "sal"))
print("Has attr addr:", hasattr(satish, "address"))

print("Delete attr :", delattr(satish, "sal"))
print(getattr(satish, "sal"))
"""
[10: 44
AM, 11 / 7 / 2021] Katta
Satish
Babu: """
1. Encapsulation :
-----------------
Definition: Binding the data members & member methods into single entity

entity         : class/object
data members   : Fields/Variables/Attributes  (class,instance variables)
member methods : Methods (Instance Methods,Class Methods,Static Methods)

satish = Employee(100,'satish, 15000)

Class  ===> Logical  -- DATA    Physical -- METHODS
Object ===> Physical -- DATA    Logical  -- METHODS (Through method access)

Ex : class is an example for encapsulation
     object is also an example


satish = Employee1(100,"satish",15000)
"""
"""
Encapsulation is the packing of data and functions that work on that data within a 
single object. By doing so, you can hide the internal
state of the object from the outside. This is known as information hiding.

A class is an example of encapsulation. A class bundles data and methods into a single unit.
 And a class provides the access to its attributes via methods.

The idea of information hiding is that if you have an attribute that isn’t visible to the outside, 
you can control the access to its value to make sure your object is always has a valid state.
"""
"""
class Counter:
    def _init_(self):
        self.current = 0

    def increment(self):
        self.current += 1

    def value(self):
        return self.current

    def reset(self):
        self.current = 0
        """
"""
The Counter class has one attribute called current which defaults to zero. And it has three methods:
increment() increases the value of the current attribute by one.
value() returns the current value of the current attribute
reset() sets the value of the current attribute to zero.
The following creates a new instance of the Counter class and calls the increment() method three
 times before showing the current value of the counter to the s
 """
"""
counter = Counter()


counter.increment()
counter.increment()
counter.increment()

print(counter.value())
"""
"""
class Counter:
    def _init_(self):
        self._current = 0

    def increment(self):
        self._current += 1

    def value(self):
        return self._current

    def reset(self):
        self._current = 0
        """

"""
class Counter:
    def _init_(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current

    def reset(self):
        self.__current = 0
        """
"""# Creating a base class
class Base:
    def _init_(self):

        # Protected member
        self._a = 2

# Creating a derived class   
class Derived(Base):
    def _init_(self):

        # Calling constructor of
        # Base class
        Base._init_(self)
        print("Calling protected member of base class: ")
        print(self._a)

obj1 = Derived()

obj2 = Base()

# Calling protected member
# Outside class will  result in
# AttributeError
print(obj2.a)

Calling protected member of base class: 

Private members
Private members are similar to protected members, the difference is that the class members declared private should neither be accessed outside the class nor by any base class. In Python, there is no existence of Private instance variables that cannot be accessed except inside a class. However, to define a private member prefix the member name with double underscore “__”.


Note: Python’s private and protected member can be accessed outside the class through python name mangling.

# Python program to
# demonstrate private members

# Creating a Base class
class Base:
    def _init_(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"

# Creating a derived class
class Derived(Base):
    def _init_(self):

        # Calling constructor of
        # Base class
        Base._init_(self)
        print("Calling private member of base class: ")
        print(self.__c)
# Driver code
obj1 = Base()
print(obj1.a)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class
"""
"""
class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def _init_(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu._class_.species))
print("Woo is also a {}".format(woo._class_.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))
"""
"""
class Parrot:

    # instance attributes
    def _init_(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the object
blu = Parrot("Blue", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())
"""

"""
class Teacher:

   #state
    def _init_(self,name,id,subject,phno):
        self.name = name
        self.id = id
        self.subject = subject
        self.phno = phno

        #behaviour
    def satish_get(self):
        print("Enter the teacher Details:",self.name, self.id,self.subject,self.phno)

employee = Teacher("satish",101,"java","9556566563")
employee.satish_get()
"""
"""
class Computer:

    def _init_(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
"""

"""
class Bankemployee:

#state

  def _init_(self,bankemployeename,bankemployeeid,bankemployeeemail):
      self.bankemployeename = bankemployeename
      self.bankemployeeid = bankemployeeid
      self.bankemployeeemail = bankemployeeemail

              #behaviour

  def satish_get(self):
      print("Enter the bank employee Details:",self.bankemployeename,self.bankemployeeid,self.bankemployeeemail)


venkat = Bankemployee("venkat",101,"venkat143@gmail.com")
venkat.satish_get()
"""
