# A Python functions that accepts two values and thier sum.

# def sum(a, b):
#     c = a + b
#     print('Sum: ', c)
#
# sum(10, 5)
# sum(10.5, 7.5)

# A Python program to find the sum of two numbers and return the result from the function.

# def sum(a, b):
#     c = a + b
#     return c
#
#
# def main():
#     x = sum(10, 5)
#     print('Sum: ', x)
#     y = sum(10.5, 5.5)
#     print('Sum: ', y)
#
#
# main()


# A function to test whether a number is even or odd

# def num_odd_or_even(n):
#     if n % 2 == 0:
#         print('Entered number is even.')
#     else:
#         print('Entered number is odd.')
#
# num_odd_or_even(2453424)
# num_odd_or_even(12321)


# A Python program to calculate factorial values of numbers.

# def fact(n):
#     prod = 1
#
#     while n >= 1:
#         prod *= n
#         n -= 1
#     return prod
#
# for i in range(1, 11):
#     print('Factorial of {} is {}'.format(i, fact(i)))

# A Python function to check whether a given number is prime or not.

# def prime(n):
#     x = 1
#
#     for i in range(2, n):
#         if n % i == 0:
#             x = 0
#             break
#         else:
#             x = 1
#     return x
#
# num = int(input('Enter a number: '))
#
# result = prime(num)
#
# if result == 1:
#     print('Entered number is prime.')
# else:
#     print('Entered number is not prime.')
#


# A Python program that generates prime numbers using functions to test prime or not.

# def prime(n):
#     x = 1
#
#     for i in range(2, n):
#         if n % i == 0:
#             x = 0
#             break
#         else:
#             x = 1
#         return x
#
# num = int(input("Enter the number: "))
#
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

# def sum_sub(a, b):
#     c = a + b
#     d = a - b
#     return c, d
#
# x, y = sum_sub(10, 5)
#
# print('Result of addition: ', x)
# print('Result of subtraction: ', y)

# A function that returns the results of addition, subtraction, multiplication and division.

# def sum_sub_mul_div(a, b):
#     c = a + b
#     d = a - b
#     e = a * b
#     f = a / b
#     return c, d, e, f
#
# t = sum_sub_mul_div(10, 5)
#
# print('The results are: ')
# for i in t:
#     print(i, end=', ')

# A Python program to see how to assign a function to a variable.

# def display(str):
#     return 'Hai ' + str
#
# x = display('Krishna')
# print('After assigning function to a variable: ', x)

# A Python program to know how to define a function inside another function.

# def display(str):
#     def message():
#         return 'How are you? '
#     result = message() + str
#     return result
#
# print(display('Krishna'))

# A Python program to know how to pass a function as parameter to another function.

# def display(fun):
#     return 'Hai, ' + fun
#
# def message():
#     return 'How are you?'
#
# print(display(message()))

# A Python program to know how a function can return another function.

# def display():
#     def message():
#         return 'How are you?'
#     return message()
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