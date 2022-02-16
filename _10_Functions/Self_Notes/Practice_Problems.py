# A function that accepts two values and finds their sum.

# def sum(a, b):
#     c = a + b
#     print('Sum is: ', c)
#
#
# sum(10, 5)
# sum(7.5, 5.5)
# sum(8, 8.31)
# sum(7, 7.313)

# A Python program to find the sum of two numbers and return the result from the function.

# def add(a, b):
#     c = a + b
#     return c
#
#
# x = add(10, 15)
# print('Sum : ', x)
# y = add(9.5, 10.5)
# print('Sum : ', y)
# z = add(9, 5.48906)
# print('Sum : ', z)

# A function to test whether a number is even or odd.

# def even_odd(n):
#     if n % 2 == 0:
#         print('Number is even.')
#     else:
#         print('Number is odd.')
#
#
# even_odd(int(input('Enter the number: ')))

# A Python program to calculate factorial of numbers.

# def factorial(n):
#     product = 1
#     while n >= 1:
#         product *= n
#         n -= 1
#     return product
#
#
# for i in range(1, 11):
#     print('Factorial of {} is {}'.format(i, factorial(i)))

# A Python function to check whether a given number is prime or not.

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
# res = prime(num)
#
# if res == 1:
#     print('Entered number is prime.')
# else:
#     print('Entered number is not prime.')

# A Python program that generates prime numbers with the help of a function to test prime or not.

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
#
# i = 2
# c = 1
#
# while True:
#     if prime(i):
#         print(i)
#         c += 1
#     i += 1
#     if c > num:
#         break

# A Python program to understand how a function returns two values.

# def math(a, b):
#     c = a + b
#     d = a - b
#     return c, d
#
#
# x, y = math(10, 5)
#
# print('Sum : ', x)
# print('Subtraction : ', y)


# A function that returns the results of addition, subtraction, multiplication and division.

# def math(a, b):
#     c = a + b
#     d = a - b
#     e = a / b
#     f = a // b
#     return c, d, e, f
#
#
# t = math(10, 5)
#
# print('The results are: ')
# for i in t:
#     print(i, end=', ')

# A Python program to see how to assign function to a variable.

# def fun(char):
#     return 'Hi ' + char
#
#
# x = fun('Krishna')
#
# print(x)

# A Python program to know how to define a function inside another function.

# def cha(n):
#     def ping():
#         return 'How are you? '
#     res = ping() + n
#     return res
#
#
# print(cha('Krishna'))

# A Python program to know how to pass a function as parameter to another function.

# def display(fun):
#     return 'Darling ' + fun
#
#
# def message():
#     return 'Satish'
#
#
# print(display(message()))

# A Python program to know how a function can return another function.

# # a = 10
#
#
# def fun():
#     # print(a)
#
#     def message():
#         # global a
#         # print(a)
#         # a = a + 10
#         # print(a)
#         return 'How are you?'
#
#     return message
#
#
# x = fun
# print(x()())


# A function that accepts two values and finds their sum.

# def sum(a, b):
#     c = a + b
#     print('Sum: ', c)
#
#
# sum(10, 5)
# sum(32.3113, 31.31213)
# sum(12, 31.31221)

# A Python program to find the sum of two numbers and return the result from the function.

# def sum(a, b):
#     c = a + b
#     d = a - b
#     return c, d
#
#
# res = sum(10, 5)
# print('Sum: ', res)

# A function to test whether a number is even or odd.

# def even_odd(n):
#     if n % 2 == 0:
#         print('Entered number is even.')
#     else:
#         print('Entered number is odd.')
#
#
# even_odd(int(input('Enter the number: ')))

# A Python program to calculate factorial of numbers.

# def fact(n):
#     product = 1
#     for i in range(n):
#         product *= n
#         n -= 1
#     return product
#
#
# for i in range(1, 11):
#     print('Factorial of {} is {}'.format(i, fact(i)))

# A Python function to check whether a given number is prime or not.

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
# res = prime(num)
#
# if res == 1:
#     print('Entered number is prime.')
# else:
#     print('Entered number is not prime.')

# A Python program that generates prime numbers with the help of a function to test prime or not.

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
# num = int(input('Enter the numbers: '))
#
# i = 2
# c = 1
#
# while True:
#     if prime(i):
#         print(i)
#         c += 1
#     i += 1
#     if c > num:
#         break

# A Python program to understand how a function returns two values.

# def add_sub(a, b):
#     c = a + b
#     d = a - b
#     return c, d
#
#
# x, y = add_sub(10, 5)
# print(x)
# print(y)

# A function that returns the results of addition, subtraction, multiplication and division.

# def math(a, b):
#     c = a + b
#     d = a - b
#     e = a / b
#     f = a // b
#     return c, d, e, f
#
#
# t = math(10, 5)
#
# for i in t:
#     print(i, end=' ')

# A Python program to see how to assign function to a variable.

# def fun(n):
#     return 'Hi' + n
#
#
# print(fun(' Satish'))

# A Python program to know how to define a function inside another function.

# def fun(n):
#     def char():
#         return 'Hi, How are you?'
#
#     res = n + char()
#     return res
#
#
# print(fun(' Krishna, '))

# def sum(a, b):
#     c = a + b
#     print(c)
#
#
# sum(10, 5)
# sum(819.910, 810.9310980)

# def sum(a, b):
#     c = a + b
#     d = a - b
#     return c, d
#
#
# x, z = sum(10, 5)
# print('Sum: ', x)
# print('Diff: ',z )
# y, w = sum(34.89139, 12.331)
# print('Sum: ', y)
# print('Diff: ', w)

# def even_odd(n):
#     for i in range(n):
#         if i % 2 == 0:
#             print(i, end=' ')
#     print()
#     for i in range(n):
#         if i % 2 != 0:
#             print(i, end=' ')
#
#
# num = int(input('Enter the number: '))
#
# even_odd(num)

# def fact(n):
#     product = 1
#     for i in range(1, n):
#         product *= i
#         n -= 1
#     return product
#
#
# for i in range(1, 11):
#     print('Factorial of {} is {}'.format(i, fact(i)))

# 1.
# def sum(a, b):
#     c = a + b
#     print('Sum: ', c)
#
#
# sum(10, 5)
#
#
# 2.
# def sum(a, b):
#     c = a + b
#     return c
#
#
# x = sum(10, 5)
# print('Sum: ', x)
# y = sum(7.5, 9.32)
# print('Sum: ', y)

# 3.
# def even(n):
#     if n % 2 == 0:
#         print('Entered number is even.')
#     else:
#         print('Entered number is not even.')
#
#
# num = int(input('Enter the number: '))
#
# even(num)

# 4.
# def fact(n):
#     product = 1
#     while n >= 1:
#         product *= n
#         n -= 1
#     return product
#
#
# for i in range(1, 11):
#     print('Factorial of {} is {}'.format(i, fact(i)))

# 5.
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
#
# if result == 1:
#     print('Entered number is prime.')
# else:
#     print('Entered number is not prime.')

# 6.

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
#
# c = 1
# i = 2
#
# while True:
#     if prime(i):
#         print(i, end=' ')
#         c += 1
#     i += 1
#     if c > num:
#         break

# 7.

# def sum(a, b):
#     c = a + b
#     d = a - b
#     e = a / b
#     f = a // b
#     return c, d, e, f
#
#
# w, x, y, z = sum(10, 5)
# print('Sum: ', w)
# print('Diff: ', x)
# print('Remainder: ', y)
# print('Divisor: ', z)

# 8.

# def math(a, b):
#     c = a + b
#     d = a - b
#     e = a / b
#     f = a // b
#     return c, d, e, f
#
#
# x = math(10, 5)
#
# for i in x:
#     print(i, end=', ')


# 9.

# def fun(n):
#     return 'Hi! ' + n + 'How are you?'
#
#
# x = fun('Krishna, ')
# print(x)

# 10.

# def fun(n):
#     def message():
#         return 'How are you?'
#
#     res = n + message()
#     return res
#
#
# print(fun('Hi! Krishna, '))

# A Python program to pass an integer to a function and modify it.

# def modify(x):
#     x = 15
#     print(x, id(x))
#
#
# x = 10
# modify(x)
# print(x, id(x))

# A Python program to pass list to a function and modify it.

# def lst(n):
#     n.append(50)
#     print(n, id(n))
#
#
# t = [10, 20, 30, 40]
# lst(t)
# print(t, id(t))

# A Python to create a new object inside the function does not modify outside object.

# def lst(n):
#     n = [40, 50, 60]
#     print(n, id(n))
#
#
# t = [10, 20, 30]
# lst(t)
# print(t, id(t))

# A Python program to understand positional arguments of a function.

# def string(s1, s2):
#     s3 = s1 + s2
#     print('Total String: ', s3)
#
#
# string('New ', 'York')

# A Python program to understand keyword arguments of a function.

# def grocery(items, price):
#     print('Item: %s' % items)
#     print('Item:', items)
#     print('Price: %.2f' % price)
#     print('Price:', price)
#
#
# grocery(items='Coconut', price=80.50)
# grocery(price=150.60, items='Biscuits')

# A Python program to understand the use of default arguments in a function.

# def grocery(items, price=100):
#     print('Items: %s' % items)
#     print('Price: %.2f' % price)
#
#
# grocery(items='Sugar', price=100)
# grocery(items='Sugar')

# A Python program to show variable length argument and it's use.

# def add(fa, *args):
#     sum = 0
#     for i in args:
#         sum += i
#     print('Sum:', fa + sum)
#
#
# add(5, 10)
# add(12, 33, 33, 3, 44, 545, 454, 54, 646, 45, 54, 454, 56, 4, 45, 64, 645, 5, 46, 4)

# A Python program to understand keyword variable length argument.

# def display(fa, **kwargs):
#     print(fa)
#     for x, y in kwargs.items():
#         print('Keys = {}, Values = {}'.format(x, y))
#
#
# display(5, RNo=15)
# display(5, RNo=15, Name='Prakash')

# A Python program to understand local and global variables.

# a = 1
#
#
# def lox():
#     a = 2
#     print(a)
#
#
# lox()
# print(a)

# A Python program to access global variable inside a function and modify it.

# a = 1
#
#
# def display():
#     global a
#     a = 2
#     print(a)
#
#
# display()
# print(a)

# A Python program to get a copy of global variable into a function and work with it.

# a = 1
#
#
# def num():
#     a = 2
#     x = globals()['a']
#     print('Global variable: ', x)
#     print('Local variable: ', a)
#
#
#
# num()
# print('Global variable: ', a)

# A function to accept a group of numbers and find their total average.

# def add(list):
#     n = len(list)
#     sum = 0
#     for i in list:
#         sum += i
#         avg = sum / n
#     return sum, avg
#
#
# print('Enter the number seperated by space: ')
# lst = [int(x) for x in input().split()]
#
# x, y = add(lst)
# print('Sum: ', x)
# print('Average: ', y)

# A function to display a group of strings.

# def char(n):
#     for i in n:
#         print(i)
#
#
# print('Enter the characters seperated by spaces: ')
# ch = [x for x in input().split(', ')]
#
# char(ch)

# A Python program to calculate factorial values using recursion.

# def factorial(n):
#     if n == 0:
#         result = 1
#     else:
#         result = n * factorial(n - 1)
#     return result
#
#
# for i in range(1, 11):
#     print('Factorial of {} is {}'.format(i, factorial(i)))

# A Python program to solve towers of hanoi problem.

# def towers(n, a, c, b):
#     if n == 1:
#         print('Move disk %i from pole %s to pole %s' % (n, a, c))
#     else:
#         towers(n - 1, a, b, c)
#         print('Move disk %i from pole %s to pole %s' % (n, a, b))
#         towers(n - 1, a, c, b)
#
#
# n = int(input('Enter the number of disks: '))
#
# towers(n, 'A', 'C', 'B')

# A Python program to create a lambda function that returns a square value of a given number.

# f = lambda x: x * x
# value = f(int(input('Enter the number: ')))
# print('Square root: ', value)

# A lambda function to calculate the sum of two numbers.

# f = lambda x, y: x + y
# value = f(10, 5)
# print('Sum: ', value)

# A lambda function to find the bigger number in two given numbers.

# max = lambda x, y: x if x > y else y
# a, b = [int(n) for n in input('Enter the two numbers: ').split()]
# print('Bigger number: ', max(a, b))

# A function that accepts two values and finds their sum.

# def sum(a, b):
#     c = a + b
#     print('Sum :', c)
#
#
# sum(10, 5)
# sum(12.313, 3113.3131)

# A Python program to find the sum of two numbers and return the result from the function.

# def sum(a, b):
#     c = a + b
#     return c
#
#
# x = sum(10, 5)
# print('Sum: ', x)
# y = sum(12.313132, 4.14131)
# print('Sum: ', y)

# A function to test whether a number is even or odd.

# def even(n):
#     if n % 2 == 0:
#         print('Entered number is even.')
#     else:
#         print('Entered number is odd.')
#
#
# even(int(input('Enter the number: ')))

# A Python program to calculate factorial values of numbers.

# def fact(n):
#     prod = 1
#     while n >= 1:
#         prod *= n
#         n -= 1
#     return prod
#
#
# for i in range(1, 11):
#     print('Factorial of {} is {}'.format(i, fact(i)))

# A Python function to check whether a given number is prime or not.

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
# result = prime(num)
#
# if result == 1:
#     print('Entered number is prime.')
# else:
#     print('Entered number is not prime.')

# A Python program that generates prime numbers with the help of a function to test prime or not.

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
# while True:
#     if prime(i):
#         print(i)
#         c += 1
#     i += 1
#     if c > num:
#         break

# A Python program to understand how a function returns two values.

# def math(a, b):
#     c = a + b
#     d = a - b
#     return c, d
#
#
# x, y = math(10, 5)
# print('Sum: ', x)
# print('Diff: ', y)

# A function that returns the results of addition, subtraction, multiplication and division.

# def math(a, b):
#     c = a + b
#     d = a - b
#     e = a / b
#     f = a // b
#     return c, d, e, f
#
#
# t = math(10, 5)
#
# for i in t:
#     print(i)

# A Python program to see how to assign a function to a variable.

# def display(n):
#     return 'Hi! ' + n
#
#
# x = display('Krishna')
# print(x)

# A Python program to know how to assign a function inside another function.

# def display(n):
#     def message():
#         return 'How are you?'
#     result = n + message()
#     return result
#
#
# print(display('Krishna, '))

# A Python program to know how to pass a function as parameter to another function.

# def display(n):
#     return 'Hi! ' + n
#
#
# def message():
#     return 'How are you?'
#
#
# print(display(message()))

# A Python program to know how a function can return another function.

# def display():
#     def message():
#         return 'Hi! , How are you?'
#     return message()
#
#
# x = display()
# print(x)

# A Python program to pass an integer to a function and modify it.

# def fun(a):
#     a = 2
#     print(a, id(a))
#
#
# a = 1
# fun(a)
# print(a, id(a))

# A Python program to pass a list to a function and modify it.

# def fun(lst):
#     lst.append(50)
#     print(lst, id(lst))
#
#
# lst = [10, 20, 30, 40]
# fun(lst)
# print(lst, id(lst))

# A Python program to create a new object inside the function does not modify outside object.

# def fun(lst):
#     lst = [2, 4, 6, 8]
#     print(lst, id(lst))
#
#
# lst = [10, 20, 30, 40]
# fun(lst)
# print(lst, id(lst))

# A Python program to understand the positional arguments of a function.

# def fun(a, b):
#     c = a + b
#     print(c)
#
#
# fun('New ', 'York')

# A Python program to understand the keyword arguments of a function.

# def grocery(items, price):
#     print('Items: %s' % items)
#     print('Price: %.2f' % price)
#
#
# grocery(items='Sugar', price=90)
# grocery(price=100, items='Coconut Oil')

# A Python program to understand the use of default arguments in a function.

# def grocery(items, price= 100):
#     print('Items: %s' % items)
#     print('Price: %.2f' % price)
#
#
# grocery(items='Horlicks', price=250)
# grocery(items='Chocolate')

# A Python program to show variable length argument and its use.

# def add(fg, *args):
#     print('Formal argument: ', fg)
#
#     sum = 0
#     for i in args:
#         sum += i
#     print('Sum: ', (fg + sum))
#
#
# add(5, 10)
# add(5, 10, 20, 30, 40)

# A Python program to understand keyword variable argument.

# def argu(fg, **kwargs):
#     print('The formal arguments: ', fg)
#
#     for x, y in kwargs.items():
#         print('Key: {}, Value: {}'.format(x, y))
#
#
# argu(5, rno=15)
# argu(5, RollNo=10, Name='Bhavesh')

# A Python program to understand local and global variables.

# a = 1
#
#
# def modify():
#     a = 2
#     print('Local: ', a)
#
#
# modify()
# print('Global: ', a)

# A Python program to access global variable inside a function and modify it.

# a = 1
#
#
# def modify():
#     global a
#     print('Global: ', a)
#     a = 2
#     print('Modified: ', a)
#
#
# modify()
# print('Global: ', a)

# A Python program to get a copy of global variable into a function and work with it.

# a = 1
#
#
# def modify():
#     a = 2
#     x = globals()['a']
#     print('Global: ', x)
#     print('Local: ', a)
#
#
# modify()
# print('Global: ', a)

# A function to accept a group of numbers and find their total average.

# def sum(n):
#     l = len(n)
#     sum = 0
#     for i in n:
#         sum += i
#         avg = sum / l
#     return sum, avg
#
#
# print('Enter the numbers seperated by space: ')
# num = [int(n) for n in input().split()]
#
# x, y = sum(num)
# print('Sum: ', x)
# print('Average: ', y)

# A funtion to display a group of strings.

# def name(n):
#     for i in n:
#         print(i)
#
#
# print('Enter the name seperated by comma: ')
# char = [n for n in input().split(',')]
#
# name(char)

# A Python program to calculate factorial values using recursion.

# def factorial(n):
#     if n == 1:
#         result = 1
#     else:
#         result = n * factorial(n - 1)
#     return result
#
#
# for i in range(1, 11):
#     print('Factorial of {} is {}'.format(i, factorial(i)))

# A Python program to create a lambda function that returns a square value of a given number.

# f = lambda x: x * x
# x = f(int(input('Enter the number: ')))
# print('Square root: ', x)

# A lambda function to calculate the sum of two numbers.

# f = lambda x, y: x + y
# x, y = [int(x) for x in input('Enter two numbers: ').split()]
# print('Sum: ', f(x, y))

# A lambda function to find the bigger number in two given numbers.

# max = lambda x, y: x if x > y else y
# a, b = [int(n) for n in input('Enter two numbers: ').split()]
# print('Bigger number: ', max(a, b))

# A Python program using filter() to filter out even numbers from a list.

# def even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
#
# lst = [int(n) for n in range(101)]
#
# num = list(filter(even, lst))
#
# print('Even numbers: ', num)


# A lambda that returns even numbers from a list.

# lst = [int(n) for n in range(51)]
#
# even = list(filter(lambda x: (x % 2 == 0), lst))
#
# print('Even numbers:', even)

# A Python program to find squares of elements in a list.

# def sqr(n):
#     return n * n
#
#
# lst = [int(n) for n in range(40)]
#
# square = list(map(sqr, lst))
#
# print(square)

# A lambda function that returns squares of element in a list.

# lst = [int(n) for n in range(31)]
#
# square = list(map(lambda x: x * x, lst))
#
# print(square)

# A Python program to find the products of elements of two different lists using lambda function.

# lst = [1, 2, 3, 4, 5]
#
# lst1 = [10, 20, 30, 40, 50]
#
# product = list(map(lambda x, y: x * y, lst, lst1))
#
# print('Product: ', product)

# A lambda function to calculate the products of elements in a list.

# from functools import *
# lst = [21, 53, 73, 23, 56]
#
# product = reduce(lambda x, y: x * y, lst)
#
# print(product)

# A decorator to increase the value of a function by 2.

# def decor(fun):
#     def inner():
#         value = fun
#         return value + 2
#     return inner()
#
#
# def num():
#     return 12
#
#
# result = decor(num())
# print(result)

# A Python program to apply a decorator to a function using @ symbol.

# def display(fun):
#     def inner():
#         value = fun()
#         return value + 2
#     return inner()
#
#
# @display
# def num():
#     return 12
#
#
# print(num)

# A Python program to create two decorators.

# def decor(fun):
#     def inner():
#         value = fun()
#         return value + 2
#     return inner
#
#
# def decor1(fun):
#     def inner():
#         value = fun()
#         return value * 2
#     return inner
#
#
# @decor
# @decor1
# def num():
#     return 10
#
#
# def num1():
#     return 10
#
#
# result = decor(decor1(num1))
#
# print(result())

# A Python program to apply two decorators to the same function using @ symbol.

# def decor(fun):
#     def inner():
#         value = fun()
#         return value + 2
#     return inner
#
#
# def decor1(fun):
#     def inner():
#         value = fun()
#         return value * 2
#     return inner
#
#
# @decor
# @decor1
# def num():
#     return 10
#
#
# print(num())

# A Python program to create a generator that returns a sequence of numbers from x to y.

# def mygen(x, y):
#     while x <= y:
#         yield x
#         x += 1
#
#
# g = mygen(5, 10)
#
#
# lst = list(g)
#
# print(lst)
#
# for i in g:
#     print(i, end=' ')

# A generator that returns character from 'A' to 'C'.

# def mygen():
#     yield 'A'
#     yield 'B'
#     yield 'C'
#
#
# g = mygen()
#
# print(next(g))
# print(next(g))
# print(next(g))


# f = lambda x: x * x
# square = f(int(input('Enter the number: ')))
# print('Square root: ', square)
#
# add = lambda x, y: x + y
# a, b = [int(x) for x in input('Enter the two numbers: ').split()]
# print('Sum: ', add(a, b))
#
# max = lambda x, y: x if x > y else y
# a, b = [int(x) for x in input('Enter the two numbers: ').split()]
# print('Bigger: ', max(a, b))
#
# def even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
#
# lst = [int(n) for n in range(51)]
#
# lst1 = list(filter(even, lst))
#
# print('Even numbers: ', lst1)
#
# lst = [int(n) for n in range(51)]
# lst1 = list(filter(lambda x: x % 2 == 0, lst))
# print('Even numbers: ', lst1)
#
# def square(x):
#     return x * x
#
#
# lst = [int(n) for n in range(51)]
#
# lst1 = list(map(square, lst))
#
# print('Square root: ', lst1)
#
#
# lst = [int(n) for n in range(51)]
# lst1 = list(map(lambda x: x * x, lst))
# print('Square root: ', lst1)
#
# lst1 = [1, 2, 3, 4, 5]
# lst2 = [10, 20, 30, 40, 50]
# lst3 = list(map(lambda x, y: x * y, lst1, lst2))
# print('Product: ', lst3)
#
# from functools import *
# lst = [1, 2, 3, 4, 5]
# lst1 = reduce(lambda x, y: x * y, lst)
# print('Product: ', lst1)

# def decor(fun):
#     def inner():
#         value = fun()
#         return value + 2
#     return inner()
#
#
# def num():
#     return 123
#
#
# result = decor(num)
# print(result)

# def decor(fun):
#     def inner():
#         value = fun()
#         return value + 2
#
#     return inner
#
#
# def decor1(fun):
#     def inner():
#         value = fun()
#         return value * 2
#
#     return inner
#
#
# @decor
# @decor1
# def num():
#     return 10
#
#
# print(num())

# def decor(fun):
#     def inner():
#         value = fun()
#         return value + 2
#     return inner()
#
# @decor
# def num():
#     return 10
#
#
# print(num)

# def mygen(x, y):
#     while x <= y:
#         yield x
#         x += 1
#
#
# x = mygen(5, 10)
#
# for i in x:
#     print(i, end=' ')


n = int(input('Enter the number of score: '))
l = []
for i in range(n):
    l.append(int(input()))

print(sorted(list(set(l)))[-2])


