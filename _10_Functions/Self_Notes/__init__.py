'''
Functions
------------------
Definition: A Function is a set of statements that takes inputs, performs some specific task and produces output.

How do i declare a function in python?
The four steps to defining a function in Python are the following:
• Use the keyword def to declare the function and follow this up with the function name.
• Add parameters to the function: they should be within the parentheses of the function. End your line with a colon.
• Add statements that the functions should execute.
• End your function with a return statement if the function should output something

Types of Functions in python
----------------------------------
Python consists of four types of functions:
1. User Defined Functions
2. Built-in-functions.
3. Lambda functions.
4. Recursive Functions.

User Defined Functions: These functions are defined or created by user.
Built-in-functions: These functions are already defined in Python libraries and we can call them directly.
Lambda functions: A lambda function can take any number of arguments, but can only have one expression.
Recursive Functions: A Python function which is defined to call itself during its execution is known as python
recursive function

"""
A function is a block of code which only runs when it is called.

Creating a Function
=======================

In Python a function is defined using the def keyword:

def my_function():
  print("Hello from a function")


 Calling a Function
 ==================

To call a function, use the function name followed by parenthesis:

def my_function():
  print("Hello from a function")

my_function()

Arguments
============

Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


Parameters or Arguments
======================

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


Arbitrary Arguments, *args
===========================

If WE do not know how many arguments that will be passed into our function, add a * before the
parameter name in the function definition.

def my_function(*kids):
  print("The youngest child is " + kids[2])  #The youngest child is DABBI

my_function("JONNY", "DUGU", "DABBI")


Advantages of Function
1. Problem of Code duplication remove
2. Code reusability


"""

'''


# A function that accepts two value


def sum(a, b):
    c = a + b
    print("Sum = ", c)


sum(10, 15)
sum(10.5, 13.9)


# A program to find the of two program and send return the result from the function


def sum(a, b):
    c = a + b
    return c


x = sum(10, 15)
print('X : ', x)
y = sum(10.45, 19.890)
print('Y : ', y)


# A function to test whether the given number is even or odd


def even_odd(num):
    if num % 2 == 0:
        print('Entered number is even')
    else:
        print('Entered number is not even')


even_odd(10)
even_odd(89)


# Find factorial of a given number

def factorial(fact):
    prod = 1
    while fact >= 1:
        prod *= fact
        fact -= 1
    return prod


for i in range(1, 11):
    print('Factorial of {} is {}'.format(i, factorial(i)))


# Check whether the given number is prime or not.


# def prime(n):
#     x = 1
#     for i in range(2, n):
#         if n % i == 0:
#             x = 0
#             break
#         else:
#             x = 1
#     return x
#
#
# num = int(input('Enter the number: '))
#
# result = prime(num)
# if result == 1:
#     print('Number is prime')
# else:
#     print('Number is not prime')


# A program that generates prime numbers with the help of a functions to test whether they are prime or not.

# def prime(n):
#     x = 1
#     for i in range(2, n):
#         if n % i == 0:
#             x = 0
#             break
#         else:
#             x = 1
#     return x
#
#
# num = int(input('Enter the range: '))
# i = 2
# c = 1
#
# while True:
#     if prime(i):
#         print(i)
#         c += 1
#     i += 1
#
#     if c > num:
#         break


# A python to understand how a function returns two values

def sum(a, b):
    c = a + b
    d = a - b
    return c, d


c, d = sum(10, 5)
print('Sum: ', c)
print('Sub: ', d)


# A python program that returns the results of addition, multiplication, subraction and division

def sum_sub_mul_div(x, y):
    s = x + y
    su = x - y
    m = x * y
    d = x / y
    return s, su, m, d


x = sum_sub_mul_div(10, 5)

for i in x:
    print(i, end=' ''\n')
print('The solution is: ', x)


# A python program to see how to assign a function to a variable

def string(str):
    return 'Hare ' + str


x = string('Krishna')
print('The string is: ', x)


# A python program to know how to define one function inside another function.


# def display(n):
#     def message():
#         return 'Dear'
#
#     result = n + message()
#     return result
#
#
# x = display('Hi ')
# print(x)
#


def display(str):
    return str + 'Krishna'


x = display('Hare ')
print('X : ', x)


def maths(m, n):
    p = m + n
    q = m - n
    r = m * n
    s = m / n
    return p, q, r, s


a = maths(10, 5)

for i in a:
    print('The results are: ', i)


def display(str):
    def message():
        return 'How are you? '

    result = message() + str
    return result


print(display('Hare '))


def deer(str):
    return str + 'Shetty'


e = deer('Bhavesh V ')
print('Name: ', e)


def guy(ysd):
    def the():
        return ' Kauravas'

    return ysd + the()


print(guy('Pandavas'))


# def hate():
#     return 'I am a'
#
#
# def jus(ha):
#     return ha + ' Python developer'
#
#
# print(jus(hate()))
#
#
# def get(push):
#     return push + '3:"Python"'
#
#
# def put():
#     return '1:"C", 2:"Java", '
#
#
# print(get(put()))
#
#
def hat():
    def hit():
        return 'Hello World!'

    return hit


x = hat()
print(x())


def got(tr):
    return tr + 'Dear'


x = got('Hi ')
print(x)


def give(er):
    def take():
        return 'GOt it'

    return 'I ' + take() + er


we = give('d')
print(we)


def attach(s1, s3):
    s3 = s1 + s3
    print("Entered string is: ", s3)


attach('New', ' Delhi')


def define(x):
    x = 15
    print(x, id(x))


x = 10
define(x)
print(x, id(x))


def rate(f):
    lst.append(50)
    lst.append(60)
    print(lst, id(lst))


lst = [10, 20, 30, 40]
rate(lst)
print(lst, id(lst))


def ims(lit):
    lst = [5, 6, 7]
    print(lst, id(lst))


lst = [1, 2, 3, 4]
ims(lst)
print(lst, id(lst))


def str(s1, s2):
    s3 = s1 + s2
    print(s3)


str('Hi ', 'Hello')


def sum(farg, *args):
    print('The formal argument: ', farg)
    sum = 0
    for i in args:
        sum += i
    print('The sum is: ', (sum + farg))


sum(10, 20)
sum(10, 20, 30, 40, 50)


def add(farg, *args):
    print('The formal argument: ', farg)
    sum = 0
    for i in args:
        sum += i
    print('The total  sum is: ', sum + farg)


add(10, 20, 30, 40)
add(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)


def bkabd(tyi):
    return tyi + 'Good Morning!'


a = bkabd('Krishna! ')
print(a)


def display(rewst):
    def message():
        return 'Gastric '

    result = rewst + message() + 'Problem'
    return result


print(display("Tips for "))


def message(str):
    return str + 'Dear'


def display():
    return 'Hai '


print(message(display()))


def modify(x):
    x = 15
    print(x)


x = 10
modify(x)
print(x)


def sadad():
    def vxfvz():
        return 'Johnny '

    return vxfvz


a = sadad()
print(a())


def maths(m, n):
    a = m + n
    b = m - n
    c = m * n
    d = m / n
    return a, b, c, d


t = maths(10, 5)

print('Using Loops: ')
for i in t:
    print(i)


def display(str):
    return str + 'How are you?'


x = display('Krishna, ')
print("Entered string: ", x)


def gjlkg(str):
    def bjksb():
        return 'How are you? '

    c = str + bjksb() + 'Dear'
    return c


print(gjlkg('Hi '))


def display(srt):
    return srt + 'Have a good day'


def message():
    return 'Good morning! '


print(display(message()))


def gkhsg():
    def bdajl():
        return 'bdsjl bjsb'

    result = bdajl() + 'jbgajbhkb'
    return result


x = gkhsg()
print(x)


def modify(lst):
    lst = [45, 56, 644]
    print(lst)

lst = [1, 2, 3, 4]
modify(lst)
print(lst)