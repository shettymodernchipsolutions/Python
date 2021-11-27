# print("-------------- Sort -----------------")
# lst = [25, 17, 36, 7, 55, 13]
# print("List before sorting: ", lst)
# lst = sorted(lst)
# print("List sorted in ascending order: ", lst)
#
# lst = [25, 17, 36, 7, 55, 13]
# print("List before sorting: ", lst)
# lst = sorted(lst, reverse=True)
# print("List sorted in descending order: ", lst)
#
# lst = [25, 17, 36, 7, 55, 13]
# print("List before sorting: ", lst)
# lst.sort()
# print("List sorted in ascending order: ", lst)
#
# lst = [25, 17, 36, 7, 55, 13]
# print("List before sorting: ", lst)
# lst.sort(reverse=True)
# print("List sorted in descending order: ", lst)

# Program to insert an element at right position within a sorted list

# lst = eval(input("Enter the sorted list between []\n"))
# n = int(input("Enter the list item\n"))
# print(lst)
#
# for i in range(len(lst)):
#     if n < lst[i]:
#         lst.insert(i, n)
#         break
#
# print(lst)
#
# lst = eval(input('Enter the sorted list between []\n'))
# n = int(input("Enter the list item\n"))
#
# print("List before sorting: ", lst)
#
# for i in range(len(lst)):
#     if n < lst[i]:
#         lst.insert(i, n)
#         break
#
# print("List after sorting: ", lst)

# Max and Min Sum (Hackerrank Problem)

# lst = [2, 4, 3, 5, 8]
# print(sum(lst)-max(lst), sum(lst)-min(lst))

# lst = eval(input('Enter the list: []\n'))
# max = lst[0]
# min = lst[0]
#
# for i in range(1, len(lst)):
#     if lst[i] > max:
#         max = lst[i]
#     elif lst[i] < min:
#         min = lst[i]
#
# print('Maximum number is: ', max)
# print('Minimum number is: ', min)
# print('Sum of Max + Min = ', max + min)


# lst = eval(input('Enter the list: \n'))
# highest = lst[0]
# lowest = lst[0]
#
# for i in range(1, len(lst)):
#     if lst[i] > highest:
#         highest = lst[i]
#     elif lst[i] < lowest:
#         lowest = lst[i]
#
# print('Highest value: ', highest)
# print('Lowest value: ', lowest)
# print('Sum of Highest and Lowest value: ', highest + lowest)

# Printing the length of a string

# lst = [32, 64, 13, 65, 12, 76, 113, 86]
# print(f'Length = {len(lst)}')


# lst = [53, 75, 32, 78, 34, 93, 73, 783]
# print(f'Length = {len(lst)}')
# count = 0
#
# for i in lst:
#     count += 1
#
# print('Count: ', count)

# Program to add all the list values.

# lst = [43, 55, 54, 76, 23, 86]
# print(f'Sum = {sum(lst)}')
# Sum = 0
#
# for i in lst:
#     Sum += i
#
# print('Sum of all the elements: ', Sum)


# Program to find the product of all the list values.

# lst = [43, 55, 54, 76, 23, 86]
# print(f'Product = {(lst)}')
# Product = 1
#
# for i in lst:
#     Product *= i
#
# print('Product of all the elements: ', Product)

# Program to check if the expression contains balanced parentheses

# s = input('Enter the expression: \n')
# lst = []
#
# for i in s:
#     if i == '[' or i == '(' or i == '{':
#         lst.append(i)
#     elif i == ']' and lst[-1] == '[':
#         lst.pop()
#     elif i == ')' and lst[-1] == '(':
#         lst.pop()
#     elif i == '}' and lst[-1] == '{':
#         lst.pop()
#     else:
#         break
#
# if len(lst) == 0:
#     print(s,'Expression is balanced')
# else:
#     print(s,'Expression is not balanced')


# s = input('Enter the expression: \n')
# lst = []
#
# for i in s:
#     if i == '[' or i == '(' or i == '{':
#         lst.append(i)
#     elif i == ']' and lst[-1] == '[':
#         lst.pop()
#     elif i == ')' and lst[-1] == '(':
#         lst.pop()
#     elif i == '}' and lst[-1] == '{':
#         lst.pop()
#     else:
#         break
#
# if len(lst) == 0:
#     print(s, 'expression is balanced')
# else:
#     print(s, 'expression is not balanced')
#
# s = input('Enter the expression: \n')
# lst = []
#
# for i in s:
#     if i == '[' or i == '(' or i == '{':
#         lst.append(i)
#     elif i == ']' and lst[-1] == '[':
#         lst.pop()
#     elif i == ')' and lst[-1] == '(':
#         lst.pop()
#     elif i == '}' and lst[-1] == '{':
#         lst.pop()
#     else:
#         break
#
# if len(lst) == 0:
#     print('Expression is balanced')
# else:
#     print('Expression is not balanced')


# Comparison of lists

# list1 = [7, 3, 5]
# list2 = [7, 3, 5]
# print(list1 == list2)

# list1 = [7, 3, 5]
# list2 = [7, 13, 5]
# print(list1 == list2)

# list1 = [7, 3, 5]
# list2 = [7, 3, 5]
# print(list1 != list2)

# list1 = [7, 3, 5]
# list2 = [7, 13, 5]
# print(list1 != list2)

# list1 = [7, 3, 5]
# list2 = [7, 13, 5]
# print(list1 != list2)

# list1 = [5, 3, 7, 6]
# list2 = [7, 3, 5, 6]
# print(list1 > list2)

# list1 = [7, 6, 2, 3]
# list2 = [7, 6, 1, 7]
# print(list1 > list2)

# list1 = [5, 3, 7, 1]
# list2 = [5, 3, 7]
# print(list1 > list2)

list1 = [1, 5, 7, 9]
list2 = [3, 2]
print(list1 > list2)