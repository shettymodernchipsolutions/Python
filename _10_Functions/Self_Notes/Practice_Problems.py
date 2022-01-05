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

# def modify(x):
#     x = 15
#     print(x, id(x))
#
# x = 10
# modify(x)
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
#     print('Items: ', item)
#     print('Price: ', price)
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

def sum(farg, *args):
    print('Formal argument: ', farg)

    sum = 0
    for i in args:
        sum += i
    print('Sum: ', farg + sum)


sum(5, 10)
sum(5, 10, 15, 20)