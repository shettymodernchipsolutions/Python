# A Python functions that accepts two values and thier sum.

# def sum(a, b):
#     c = a + b
#     print('Sum: ', c)
#
# sum(10, 25)
# sum(10.5, 7.5)


# A Python program to find the sum of two numbers and return the result from the function.

# def sum(a, b):
#     c = a + b
#     return c
#
# x = sum(10, 5)
# print('The sum is: ', x)
# y = sum(10.5, 5.5)
# print('The sum is: ', y)

# A function to test whether a number is even or odd

# def even_odd(n):
#     if n % 2 == 0:
#         print('Number is even.')
#     else:
#         print('Number is odd')
#
# even_odd(43151354)
# even_odd(43626735)

# A Python program to calculate factorial values of numbers.

# def fact(n):
#     prod = 1
#     while n >= 1:
#         prod *= n
#         n -= 1
#     return prod
#
#
# for i in range(1, 12):
#     print('The factorial of {} is {}'.format(i, fact(i)))

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
# num = int(input('Enter the number: '))
#
# result = prime(num)
#
# if result == 1:
#     print('Entered number is prime.')
# else:
#     print('Entered number is not prime.')

# A Python program that generates prime numbers using functions to test prime or not.

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
# num = int(input('Enter the range of prime numbers: '))
# c = 1
# i = 2
#
# while True:
#     if prime(i):
#         print(i)
#         c += 1
#     i += 1
#
#     if c > num:
#         break

# A Python program to understand how a function returns two values.

# def sum_sub(a, b):
#     c = a + b
#     d = a - b
#     return c, d
#
#
# x, y = sum_sub(10, 5)
#
# print('Result of Addition: ', x)
# print('Result of Subtraction: ', y)

# A function that returns the results of addition, subtraction, multiplication and division.

# def sum_sub_mul_div(a, b):
#     c = a + b
#     d = a - b
#     e = a * b
#     f = a / b
#     return c, d, e, f
#
#
# t = sum_sub_mul_div(10, 5)
#
# print('The results are: ')
# for i in t:
#     print(i, end=', ')

# A Python program to see how to assign a function to a variable.

# def string(fun):
#     return fun + 'is the best language in the world.'
#
#
# x = string('Python ')
# print(x)

# A Python program to know how to define a function inside another function.

# def display(str):
#     def message():
#         return 'How are you?'
#
#     return str + message()
#
#
# print(display('Krishna, '))

# A Python program to know how to pass a function as parameter to another function.

# def string(str):
#     return str + 'is the trending job in the 20th century.'
#
#
# def message():
#     return 'Data Science '
#
#
# print(string(message()))

# A Python program to know how a function can return another function.

# def display():
#     def message():
#         return 'I am a Python Developer.'
#
#     return message()
#
#
# fun = display()
# print(fun)

# A Python program to pass an integer to a function and modify it.

# def data(x):
#     x = 15
#     print(x, id(x))
#
#
# x = 10
# data(x)
# print(x, id(x))

# A Python program to pass a list to a function and modify it.

# def data(lst):
#     lst = [40, 50, 60]
#     print(lst, id(lst))
#
# lst = [10, 20, 30]
# data(lst)
# print(lst, id(lst))

# def data(lst):
#     lst.append(40)
#     print(lst, id(lst))
#
#
# lst = [10, 20, 30]
# data(lst)
# print(lst, id(lst))


# A Python program to create a new object inside the function does not modify outside object.

# def data(lst):
#     lst = [40, 50, 60]
#     print(lst, id(lst))
#
#
# lst = [10, 20, 30]
# data(lst)
# print(lst, id(lst))


# A Python program to understand the positional argument of a function.

# def pos_arg(s1, s2):
#     s3 = s1 + s2
#     print('The argument is: ', s3)
#
#
# pos_arg('New ', 'York')


# A Python program to understand the keyword argument of a function.

# def grocery(item, price):
#     print('Items: %s' % item)
#     print('Price: %.2f' % price)
#
#
# grocery(item='Rice', price=88)
# grocery(price=90, item='Imperial Blue')


# A Python program to understand the use of default arguments in a function.

# def grocery(item, price=50):
#     print('Item: ', item)
#     print('Price: ', price)
#
#
# grocery(item='Sunflower Oil', price=125)
# grocery(item='Flour')

# A Python program to show variable length argument and its use.

# def display(forArg, **kwargs):
#     print('Formal Arguments: ', forArg)
#
#     for x, y in kwargs.items():
#         print('keys = {} and values = {}'.format(x, y))
#
#
# display(5, rno=10)
# print()
# display(5, rno=10, name='Prakash')

# A Python program to understand keyword variable argument.

# def display(farg, **kwargs):
#     print('Formal argument: ', farg)
#
#     for x, y in kwargs.items():
#         print('key = {}, value = {}'.format(x, y))
#
# display(5, rno = 10)
# print()
# display(5, rno = 10, name = 'Prakash')


# A Python program to understand local variables and global variables.

# a = 1
#
#
# def local():
#     a = 2
#     print('a = ', a)
#
#
# local()
# print('a = ', a)

# A Python program to access global variable inside a function and modify it.

# a = 1
#
#
# def myfunction():
#     global a
#     print('a = ', a)
#     a = 2
#     print('a = ', a)
#
#
# myfunction()
# print('a = ', a)

# A Python program to get a copy of global variable into a function and work with it.

# a = 1
#
# def display():
#     a = 2
#     x = globals()['a']
#     print('global var a = ', x)
#     print('local var a = ', a)
#
# display()
# print('global var a = ', a)

# A function to accept a group of numbers and find their total average.

# def sum(lst):
#     n = len(lst)
#     sum = 0
#     for i in lst:
#         sum += i
#         avg = sum / n
#         return avg, sum
#
#
# print('Enter the numbers seperated by space: ')
# lst = [int(x) for x in input().split()]
#
# x, y = sum(lst)
# print('Average: ', x)
# print('Sum: ', y)


# A function to display a group of strings.

# def display(str):
#     for i in str:
#         print(i)
#
#
# print('Enter the group of strings: ')
# lst = [x for x in input().split()]
#
#
# display(lst)


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

# A Python program to solve towers of hanoi tower problem.

# def towers(n, a, c, b):
#     if n == 1:
#         print('Move disk %i from %s pole to %s pole' %(n, a, c))
#     else:
#         towers(n - 1, a, b, c)
#         print('Move disk %i from %s pole to %s pole' %(n, a, c))
#         towers(n - 1, b, c, a)
#
#
# n = int(input('Enter the number of disks: '))
#
# towers(n, 'A', 'C', 'B')


# A Python program to create a lambda function that returns a square value of a given number.

# f = lambda x : x * x
# value = f(8701)
# print('Value = ', value)

# A Python program to calculate the sum of two numbers.

# f = lambda x, y : x + y
# value = f(324.784307, 78032.78031)
# print('Value = ', value)

# A lambda function to find the bigger number in two given number.

# max = lambda x, y : x if x > y else y
# a, b = [int(n) for n in input('Enter two number: ').split(',')]
# print('Biggest number: ', max(a, b))

# big = lambda x, y: x if x > y else y
# a, b = [int(n) for n in input('Enter two number: ').split(',')]
# print('Biggest number: ', big(a, b))

# A Python program using filter() to filter out even numbers from a list.

# def even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
#
# lst = [1, 2, 3, 4, 5, 6, 76, 8, 4, 71839, 714809, 64319, 5268, 64290, 693278, 61379, 74280, 679563]
# print('Entered list items: ', lst)
#
# lst1 = list(filter(even, lst))
# print('Extracted even numbers: ', lst1)

# A lambda that returns even numbers from a list.

# lst = [132, 315, 31, 4426, 43, 472]
# print('Entered list items: ', lst)
# lst1 = list(filter(lambda x: (x % 2 == 0), lst))
# print('Extracted even numbers: ', lst1)


# A Python program to find squares of elements in a list.

# def square(x):
#     return x * x
#
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print('Entered list elements: ', lst)
# lst1 = list(map(square, lst))
# print('Square of all list elements: ', lst1)


# A lambda function that returns squares of a list.

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print('Find the squares of all list elements: ', lst)
# lst1 = list(map(lambda x : (x * x), lst))
# print('Square of all list elements: ', lst1)

# A Python program to find the products of elements of two different lists using lambda function.

# lst1 = [1, 2, 3, 4, 5]
# lst2 = [10, 20, 30, 40, 50]
# lst3 = list(map(lambda x, y : x * y, lst1, lst2))
# print('Product of two list elements: ', lst3)

# A lambda function to calculate products of elements in a list.

# from functools import *
#
# lst = [1, 2, 3, 4, 5]
# lst1 = reduce(lambda x, y: x * y, lst)
# print(lst1)

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
# n = int(input('Enter the number: '))
#
# result = prime(n)
#
# if result == 1:
#     print('Entered number is prime.')
# else:
#     print('Entered number is not prime.')
#
#
# def fact(f):
#     product = 1
#     while f >= 1:
#         product *= f
#         f -= 1
#     return product
#
# dic = {}
# def factori(n):
#     for n in dic:
#         return n
#
#
#
# n = int(input('Enter the factorial of: '))
#
# for i in range(n):
#     print('Factorial of {} is {}'.format(i, fact(i)))


# A decorator to increase the value of a function by 2.

# def decor(fun):
#     def inner():
#         value = fun()
#         return value + 2
#
#     return inner
#
#
# def num():
#     return 10
#
#
# result_fun = decor(num)
# print('Value of a function: ', result_fun())


# A Python program to apply a decorator to a function using @ symbol.

# def decor(fun):
#     def inner():
#         value = fun()
#         return value + 2
#
#     return inner()
#
#
# @decor
# def num():
#     return 10
#
#
# print('Value of a function: ', num)


# A Python program to create two decorators.

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
# def num():
#     return 10
#
#
# result_fun = decor(decor1(num))
# print('The value of a function: ', result_fun())


# A Python program to apply two decorators to the same function using @ symbol.

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
# print('Value of a function:', num())


# A Python program to create a generator that returns a sequence of numbers from x to y.

# def mygen(x, y):
#     while x <= y:
#         yield x
#         x += 1
#
#
# g = mygen(5, 10)
#
# for i in g:
#     print(i, end=' ')


# A generator that returns characters from A to C.

# def mygen():
#     yield 'A'
#     yield 'B'
#     yield 'C'
#
# g = mygen()
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# A Python program to calculate the gross salary and net salary of an employee.

# def da(basic):
#     da = basic * 80 / 100
#     return da
#
#
# def hra(basic):
#     hra = basic * 15 / 100
#     return hra
#
#
# def pf(basic):
#     pf = basic * 12 / 100
#     return pf
#
#
# def itax(gross):
#     tax = gross * 0.1
#     return tax
#
#
# basic = float(input('Enter basic salary: '))
#
# gross = basic + da(basic) + hra(basic)
# print('Your gross salary: {:10.2f}'.format(gross))
#
# net = gross - pf(basic) - itax(gross)
# print('Your net salary: {:10.2f}'.format(net))


