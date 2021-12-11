#Python Data Types:

"""Data types are the classification or categorization of data items. It represents the kind
of value that tells what operations can be performed on a particular data. Since
everything is an object in Python programming, data types are actually classes and
variables are instance (object) of these classes.
There are 5 types
1 Numeric--------integer,float,complex number.
2 Dictionary
3 Boolean
4 set
5 sequence type------------tupl=[--[[[[[[[[[[[e,strings,list"""

#Numeric:

"""In Python, numeric data type represent the data which has numeric value. Numeric
value can be integer, floating number or even complex numbers. These values are
defined as int, float and complex class in Python.
Integers – This value is represented by int class. It contains positive or negative
whole numbers (without fraction or decimal). In Python there is no limit to how
long an integer value can be.
Float – This value is represented by float class. It is a real number with floating
point representation. It is specified by a decimal point. Optionally, the character e or
E followed by a positive or negative integer may be appended to specify scientific
notation.
Complex Numbers – Complex number is represented by complex class. It is
specified as (real part) + (imaginary part)j. For example – 2+3j"""

#Example problems:
'''a = 5
print("Type of a: ", type(a))
b = 5.0
print("Type of b: ", type(b))
c = 5+3j
print("Type of c: ", type(c))'''

"""
# int   integers
x = 10
age = 15
num = 20
print("----int-------")
print(x, age, num)
print(id(x), id(age), id(num))
print(type(x), type(age), type(num))
# float
print("----float-----")
bill = 15.5
mobile_bill = 235.43
petrol_bill = 120.32
print(bill, mobile_bill, petrol_bill)
print(type(bill), type(mobile_bill), type(petrol_bill)) 
"""
""" x = 1
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z)) """


"""x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
"""
""" x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))"""

"""x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
"""
"""x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))
"""
"""#convert from int to float:
x = float(1)
#convert from float to int:
y = int(2.8)
#convert from int to complex:
z = complex(x)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
"""

#BOOLEAN_DATATYPE:

"""Data type with one of the two built-in values, True or False. Boolean objects that are
equal to True are truthy (true), and those equal to False are falsy (false).
But nonBoolean objects can be evaluated in Boolean context as well and determined to be true
or false. It is denoted by the class bool.
###--– True and False with capital ‘T’ and ‘F’ are valid booleans otherwise python will
throw an error.
"""
"""x = True
#display x:
print(x)
#display the data type of x:
print(type(x)) 
x = bool(5)
#display x:
print(x)
"""

#sequence_type:
"""In Python, sequence is the ordered collection of similar or different data types.
Sequences allows to store multiple values in an organized and efficient fashion. There
are several sequence types in Python"""

### STRING_DATATYPE

"""
-->The string formatting is used to print the string exactly the way we want. In the string formatting we use the {} as the place holders and use the format() method to fill the placeholders. We pass the values to the format() method.
exmaple:
--------
a = {'name': 'suma', 'age' : 26}
sentence = 'my name is {}, age is {}'.format(a['name'], a['age'])
print(sentence)
-->we can also grab the specific things. Directly write the values in placeholders.
example:
--------
a = {'name': 'suma', 'age' : 26}
sentence = 'my name is {0[name]}, age is {1[age]}'.format(a,a)
print(sentence)
-->In the above program we just write the dictionary a 2 times in the format(). Instead of the we can write the 'a' one time and write the 0 in the all the place holders. which means the values in the dictionary will be passed to the placeholders. 
example:
---------
a = {'name': 'suma', 'age' : 26}
sentence = 'my name is {0[name]}, age is {0[age]}'.format(a)
print(sentence)
-->This is the same way that we access the list values also.
exmaple:
----------
a = {'name': 'suma', 'age' : 26}
l = ['suma', 26]
sentence = 'my name is {0[0]}, age is {0[1]}'.format(l)
print(sentence)
-->we can put the numbers in the placeholders, like which value should by stored in which placeholder. the number in the placeholder denotes the order of the values we passed in the fomat() method.
exmpale:
---------
a = {'name': 'suma', 'age' : 26}
sentence = 'my name is {0}, age is {1}'.format(a['name'], a['age'])
print(sentence)
->we can also use the tags.
example:
--------
tag = h1
text  = 'this is the heading tag'
sentence = '<{0}> {1} </{0}>'.format(tag, text)
print(sentence)
----------------------------------------------------------------------------------------------------------
-->Shorthand if else statement
example:
--------
a = input(int("enter the fist number"))
b = input(int("entere the second number"))
print(" b is greater than a") if a < b else print("a is greater than b")
"""