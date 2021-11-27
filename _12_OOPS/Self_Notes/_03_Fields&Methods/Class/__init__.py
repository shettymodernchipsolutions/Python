'''
Classes
-------------

Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object,
allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining
its state. Class instances can also have methods (defined by its class) for modifying its state.

Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

How to create a class?

To create a class, use the keyword class:

Example
Create a class named MyClass, with a property named x:

class MyClass:
  x = 5


The __init__() Function
---------------------------
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when
the object is being created:

Example
Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

Object Methods
---------------------

Objects can also contain methods. Methods in objects are functions that belong to the object.

Let us create a method in the Person class:

Example
Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

The self Parameter
-------------------------------

The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to
the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any
function in the class:

Example
Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

'''

class FootBaller:

    def __init__(self, name, team, goals):
        self.name = name
        self.team = team
        self.goals = goals

    def shooting(self):
        print(self.name,'is shooting')

    def