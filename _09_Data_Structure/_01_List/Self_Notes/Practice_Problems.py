# A Python program to create lists with different types of elements.

# num = [10, 20, 30, 35.5]
# print('List elements = ', num)
# print('First = %d, Last = %.2f' % (num[0], num[3]))
#
# names = ['Harish', 'Vishnu', 'Rama', 'Letty']
# print('List names = ', names)
# print('First = %s, Last = %s' % (names[0], names[3]))
#
# lst = [10, 20, 30, 35.9, 'John', 'Sanjay']
# print('List data = ', lst)
# print('First = %d, Last = %.1f' % (lst[0], lst[3]))

# A Python program to create lists using range() function.

# list1 = range(10)
# for i in list1:
#     print(i, end=', ')
# print()
#
# list2 = range(5, 10)
# for i in list2:
#     print(i, end=', ')
# print()
#
# list3 = range(2, 11, 2)
# for i in list3:
#     print(i, end=', ')

# A Python program to access list elements using loops.

# lst = [10, 20, 30, 40, 50]
#
# i = 0
# print('Using while loop')
# while i < len(lst):
#     print(lst[i], end=' ')
#     i += 1
# print()
#
# print('Using for loop')
# for i in lst:
#     print(i, end=' ')

# lst = [10, 20, 30, 40, 50, 60]
# print(lst)
# lst.append(89)
# print(lst)
# lst[0] = 32
# print(lst)
# lst[0:3] = 12, 32, 21, 53, 31, 33
# print(lst)
# del lst[0]
# print(lst)
# lst.remove(33)
# print(lst)
# lst.reverse()
# print(lst)

# A Python program to display the elements of a list in reverse order.

# lst = ['Harish', 'Ganesh', 'Deepak', 'Deepthi', 'Krishna']
#
# print('In reverse order: ')
# i = len(lst) - 1
# while i >= 0:
#     print(lst[i], end=' ')
#     i -= 1
#
# print()
#
# i = -1
# while i >= -len(lst):
#     print(lst[i], end=' ')
#     i -= 1

# x = [10, 20, 30, 40]
# y = [50, 60, 70, 80]
# print(x)
# print(y)
# z = x + y
# print(z)
# print(x + y)
# print(x * 3)
# a = 20
# print(a in x)

# lst1 = [10, 20, 30, 40, 50]
# lst2 = lst1
# print(lst1)
# print(lst2)
# lst1[1] = 99
# print(lst1)
# print(lst2)

# lst1 = [10, 20, 30, 40]
# lst2 = lst1[:]
# print(lst1)
# print(lst2)
# lst2[1] = 99
# print(lst1)
# print(lst2)

# A Python program to understand list processing methods.

# lst = [10, 20, 30, 40, 50]
#
# n = len(lst)
# print(n)
#
# lst.append(35)
# print(lst)
#
# lst1 = lst.copy()
# print(lst1)
#
# lst.insert(1, 15)
# print(lst)
#
# lst.extend(lst1)
# print(lst)
#
# n = lst.count(30)
# print(n)
#
# lst.remove(50)
# print(lst)
#
# lst.pop()
# print(lst)
#
# lst.sort()
# print(lst)
#
# lst.reverse()
# print(lst)
#
# lst.clear()
# print(lst)

# A Python program to find maximum and minimum elements in a list.

# x = []
#
# print('Enter the number of list: ', end='')
# n = int(input())
#
# for i in range(n):
#     print('Enter the list elements: ', end='')
#     x.append(int(input()))
#
# big = x[0]
# small = x[0]
#
# for i in range(1, n):
#     if x[i] > big: big = x [i]
#     if x[i] < small: small = x[i]
#
# print('The biggest element: ', big)
# print('The smallest element: ', small)

# A Python program to sort the list elements using bubble sort technique.

# x = []
#
# print('Enter the number of elements: ', end='')
# n = int(input())
#
#
# for i in range(n):
#     print('Enter the elements: ', end='')
#     x.append(int(input()))
#
# print('List to be sorted: ', x)
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
# print('Sorted List: ', x)

# A Python program to know how many times an element occurred in the list.

# x = []
#
# print('Enter the number of list elements: ', end='')
# n = int(input())
#
# for i in range(n):
#     print('Enter the element: ', end='')
#     x.append(int(input()))
#
# print('The list is: ', x)
#
# y = int(input('Enter the list element to be counted: '))
# c = 0
# for i in x:
#     if y == i: c += 1
# print('{} has occurred {} times'.format(y, c))

# A Python program to find the common elements in two lists.

# scholar1 = ['Vinay', 'Harish', 'Saraswathi', 'Govind']
# scholar2 = ['Govind', 'Harry', 'Vinay', 'Vishal', 'Dheemanth']
#
# s1 = set(scholar1)
# s2 = set(scholar2)
# s3 = s1.intersection(s2)
#
# common = list(s3)
#
# print('Common elements in both list: ', common)

# A Python program to create a list with employee data and then retrieve a particular employee datails.

# emp = []
#
# print('Enter the total number of employees: ')
# n = int(input())
#
# for i in range(n):
#     print('Enter Id: ', end='')
#     emp.append(int(input()))
#     print('Enter name: ', end='')
#     emp.append(input())
#     print('Enter Salary: ', end='')
#     emp.append(float(input()))
#
# id = int(input('Enter the id: '))
#
# for i in range(len(emp)):
#     if id == emp[i]:
#         print('Id : {:d}, Name : {:s}, Salary : {:.2f}'.format(emp[i], emp[i + 1], emp[1 + 2]))
#     else:
#         break

# A Python program to create a nested list and display its elements.

# lst = [10, 20, 30, [80, 90]]
# print('List elements: ', lst)
# print('The first list element: ', lst[0])
# print('The last element in the list is a nested list: ', lst[3])
# print('The element of nested list: ', end='')
# for i in lst[3]:
#     print(i, end=' ')

# A Python program to retrieve elements from a matrix and display them.

# mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# print('Display the list as it is: ')
# print(mat)
#
# print('Display row by row: ')
# for r in mat:
#     print(r)
#
# print('Display each column of row 0: ')
# for c in mat[0]:
#     print('%d' % c, end=' ')
# print()
#
# print('Display each column of row 1: ')
# for c in mat[1]:
#     print('%d' % c, end=' ')
# print()
#
# print('Display each column of row 2: ')
# for c in mat[2]:
#     print('%d' % c, end=' ')
# print()
#
# print('Display all elements using for loop: ')
# for r in mat:
#     for c in r:
#         print('%d' % c, end=' ')
#     print()
#
# print('Display all elements using for loop: ')
# for i in range(len(mat)):
#     for j in range(len(mat[i])):
#         print('%d' % mat[i][j], end=' ')
#     print()

# A Python program to add two matrices and display the sum matrices using lists.

# m1 = [[1, 2, 3, 0], [4, 5, 6, 0], [7, 8, 9, 0]]
# m2 = [[1, 2, 3, 4], [1, 0, 1, 0], [2, -1, -2, 1]]
# m3 = [4 * [0] for i in range(3)]
#
# for i in range(3):
#     for j in range(4):
#         m3[i][j] = m1[i][j] + m2[i][j]
#
# print('The result of the matrice: ')
# for i in range(3):
#     for j in range(4):
#         print('%d' % m3[i][j], end=' ')
#     print()
#
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()

# squares = [x ** 2 for x in range(1, 11)]
# print(squares)

# Suppose if we want to get squares of integers from 1 to 10 and take only the even numbers from the result,
# we can write the list comprehension as:
# squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
# print(squares)

# square = [x ** 2 for x in range(2, 11, 2)]
# print(square)

# If we have two lists 'x' and 'y' and we want to add each element of 'x' with each element of 'y', we can write for loop as:

# x = [10, 11, 12, 13]
# y = [1, 2, 3, 4]
# lst = []
# for i in x:
#     for j in y:
#         lst.append(i + j)
# print(lst)

# x = [12, 54, 87, 32]
# y = [13, 57, 12, 365]
# lst = [i + j for i in x for j in y]
# print(lst)

# sum = [i + j for i in [12, 43, 32, 56] for j in [21, 65, 12, 57]]
# print(sum)

# The previous list comprehension can be written using string as:

# char = [i + j for i in 'ABC' for j in 'DE']
# print(char)

# Let's take two lists 'num1' and 'num2' with some numbers as:

# num1 = [89, 12, 22, 43, 32]
# num2 = [12, 43, 54, 23, 89]
# num3 = []
#
# for i in num1:
#     if i not in num2:
#         num3.append(i)
# print(num3)

# A Python program to accept elements in the form of a tuple and display their sum and average.

# num = eval(input('Enter the number: '))
# sum = 0
# n = len(num)
# for i in range(n):
#     sum += num[i]
# print('Sum = ',sum)
# print('Average = ', sum / n)

# A Python program to find the first occurence of an element in a tuple.

# char = input('Enter the characters seperated by comma: ').split(',')
# lst = [int(i) for i in char]
# tup = tuple(lst)
# print(tup)
# ele = int(input('Enter the element to find the position: '))
#
# try:
#     pos = tup.index(ele)
#     print('Entered element found at position: ', pos + 1)
# except ValueError:
#     print('Entered element not found.')

# A Python program to sort a tuple with nested tuples.

# emp = ((10, 'Ajay', 91891), (11, 'John', 781731), (12, 'Kundan', 7801731), (13, 'Ivan', 98018))
#
# print(sorted(emp))
# print(sorted(emp, reverse=True))
# print(sorted(emp, key=lambda s: s[1]))
# print(sorted(emp, key=lambda x: x[2]))

# A Python program to insert a new element into a tuple of elements at a specified position.

# names = ('Harsha', 'Adithya', 'Yash', 'Gani', 'Madhukar')
# print(names)
#
# lst = input('Enter the name: ').split(',')
# new = tuple(lst)
# position = int(input('Enter the position no.: '))
#
# names1 = names[0: position]
# names1 = names1 + new
# names = names1 + names[position: ]
#
# print(names)

# A Python program to modify or replace an existing element of a tuple with a new element.

# num = (10, 20, 30, 40, 50)
# print(num)
#
# lst = [int(input('Enter the number: '))]
# new = tuple(lst)
# position = int(input('Enter the position: '))
#
# num1 = num[0: position - 1]
# num1 = num1 + new
# num = num1 + num[position: ]
# print(num)

# A program to delete an element from a particular position in the tuple.

num = (10, 20, 30, 40, 50)
print(num)

pos = int(input('Enter the position no.: '))

num1 = num[0: pos - 1]
num = num1 + num[pos:]
print(num)