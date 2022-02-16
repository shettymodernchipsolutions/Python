# print("--------------- Remove -----------------")
#
# lst = [10, 20, 30, 40, 50, 60, 70]
# print("List of all elements: ", lst)
# print("List of 1st element: ", lst[0])
# print("Prints all the list elements: ", lst[::])
# print("List elements of specified range: ", lst[1:5:])
# print("Alternate list elements: ", lst[::2])
# print("Returns empty list: ", lst[-2:-5:])
# print("List of specified range in reverse order: ", lst[-2:-5:-1])
# print("List of all elements in reverse order: ", lst[::-1])
#

# x = []
#
# print('Enter the elements? ', end='')
#
# n = int(input())
#
# for i in range(n):
#     print('Enter the elements: ', end='')
#     x.append(int(input()))
#
# print('The list elements are: ', x)
#
# big = x[0]
# small = x[0]
#
# flag = False
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if x[j] > x[j + 1]:
#             t = x[j]
#             x[j] = x[j + 1]
#             x[j + 1] = t
#             flag = True
#     if flag == False:
#         break
#     else:
#         flag = False
#
# print(x)


# def factorial(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res
#
#
# def main():
#     n = int(input("Enter the factorial: "))
#     print('The factorial is: ', factorial(n))
#
# if __name__ == '__main__':
#     main()

# Write a program to count the number of digits.

# def count_digits(n):
#
#     count = 0
#
#     while(n > 0):
#         n = n // 10
#         count += 1
#     return count
#
# def main():
#     n = int(input('Enter the values: '))
#     print('The total count is: ', count_digits(n))
#
# main()


# Given a number find the number of trailing zeros of it's factorial.

# def trailing_zeros(n):
#     res = 0
#     powerOf5 = 5
#     while n >= powerOf5:
#         res = res + (n // powerOf5)
#         powerOf5 *= 5
#     return res
#
#
# def fact(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
#
# def main():
#     n = int(input("Enter the number: "))
#     print(trailing_zeros(n))
#     print(fact(n))
#
#
# if __name__ == '__main__':
#     main()


# Given two numbers, calculate the greatest common divisors or the highest common factor(HCF)

# def gcd(a, b):
#     min = 0
#     if a < b:
#         min = a
#     else:
#         min = b
#
#     for i in range(min, 0, -1):
#         if(a % i == 0 and b % i ==0):
#             return i


# def euclid_gcd(a, b):
#     while a != b:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a
#     return a
#
#
# def main():
#     a = int(input("Enter the first value: "))
#     b = int(input("Enter the first value: "))
#     print(euclid_gcd(a, b))
#
#
# main()


# def euclid_gcd(a, b):
#     while (a != 0 and b != 0):
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#
#     if a != 0:
#         return a
#     else:
#         return b
#
#
# def main():
#     a = int(input('Enter the first value: '))
#     b = int(input('Enter the first value: '))
#     print(euclid_gcd(a, b))
#
#
# if __name__ == '__main__':
#     main()


# Write a program to calculate the LCM of two numbers.

# def lcm(a, b):
#     result = max(a, b)
#     while(True):
#         if(result % a == 0 and result % b == 0):
#             break
#         result += 1
#     return result

# def lcm(a, b):
#     return a * b / euclid_gcd(a, b)
#
#
# def euclid_gcd(a, b):
#     while (a != 0 and b != 0):
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#
#     if a != 0:
#         return a
#     else:
#         return b
#
#
# def main():
#     a = int(input('Enter the first number: '))
#     b = int(input('Enter the second number: '))
#     print(lcm(a, b))
#
#
# if __name__ == '__main__':
#     main()


# Print all the divisors of given number 'n'


# def print_divisors(n):
#     for i in range(1, n + 1):
#         if n % i == 0:
#             print(i)
#
#
# def main():
#     n = int(input('Enter the value: '))
#     print(print_divisors(n))
#
#
# if __name__ == '__main__':
#     main()
#
#
# # Find all the prime factors of a given number
#
# def prime_factors(n):
#     i = 2
#
#     while (n > 1):
#         while (n % i == 0):
#             print(i)
#             n = n // i
#         i += 1
#
#
# def main():
#     n = input(input("Enter the number: "))
#     prime_factors(n)
#
#
# if __name__ == '__main__':
#     main()


# def prime_numbers(n):
#     for i in range(2, n + 1):
#         if n % i == 0:
#             flag = True
#             break
#         else:
#             print(i)
#
#
# def main():
#     n = int(input('Enter the range: '))
#     # p = int(input('Enter the range: '))
#     print(prime_numbers(n))
#
# if __name__ == '__main__':
#     main()


