# A Python program to access each element of a string in forward and reverse orders using while loop.

# char = 'Core Python'
#
# n = len(char)
# i = 0
#
# while i < n:
#     print(char[i], end=' ')
#     i += 1
# print()
#
# i = 1
# while i <= n:
#     print(char[-i], end=' ')
#     i += 1
# print()
#
# i = -1
# while i >= -n:
#     print(char[i], end=' ')
#     i -= 1

# A Python program to access the characters of the string using for loop.

# char = 'Core Python'
#
# for i in char:
#     print(i, end=' ')
# print()
#
# for i in char[::-1]:
#     print(i, end=' ')

# A Python program to know whether a sub string exists in main string or not.

# st = input('Enter the main string: ')
# st1 = input('Enter the sub string: ')
#
# if st1 in st:
#     print(st1+' is found in main string.')
# else:
#     print(st1+' is not found in main string.')


"""-------------------------Comparing Strings-------------------------"""

# s1 = 'Python'
# s2 = 'Python'
# if s1 == s2:
#     print('Both are same.')
# else:
#     print('Both are not same.')
#
# if s1 < s2:
#     print('s1 is less than s2.')
# else:
#     print('s1 is greater than or equal to s2.')

'''-------------------------Removing Spaces from Strings-------------------------'''

# s1 = 'Mukesh '
# s2 = 'Mukesh'
#
# if s1 == s2:
#     print('Welcome.')
# else:
#     print('Not Found.')

# name = ' Mukesh Deshmukh '
# print(name.lstrip())
# print(name.rstrip())
# print(name.strip())

# A Python program to find the first occurence of sub string in a given main string.

# s1 = input('Enter the main string: ')
# s2 = input('Enter the sub string: ')
#
# n = s1.find(s2, 0, len(s1))
#
# if n == -1:
#     print(s2+' is not found in main string.')
# else:
#     print(s2+' is found in main string.')

# A Python program to find the first occurence of sub string in a given main string using index() method.

# s1 = input('Enter the main string: ')
# s2 = input('Enter the sub string: ')
#
# try:
#     n = s1.index(s2, 0, len(s1))
# except ValueError:
#     print(s2+' is not found in main string.')
# else:
#     print(s2+' is found in main string.')

# A Python program to display all positions of a sub string in a given main string.

# s1 = input('Enter the main string: ')
# s2 = input('Enter the sub string: ')
#
# i = 0
# flag = False
# n = len(s1)
# while i < n:
#     pos = s1.find(s2, i, n)
#     if pos != -1:
#         print('String found at position: ', pos + 1)
#         i = pos + 1
#         flag = True
#     else:
#         i += 1
#
# if flag == False:
#     print('String not found.')

# A Python program to display all positions of a sub string in a given main string - version 2.

# s1 = input('Enter the main string: ')
# s2 = input('Enter the sub string: ')
#
# n = len(s1)
# flag = False
# pos = -1
#
# while True:
#     pos = s1.find(s2, pos + 1, n)
#     if pos == -1:
#         break
#
#     print('String found at position: ', pos + 1)
#     flag = True
#
# if flag == False:
#     print('String not found.')

# A Python program to display all positions of a sub string in a given main string - version 3.

# s1 = input('Enter the main string: ')
# s2 = input('Enter the sub string: ')
# length = len(s2)
#
# for i in range(len(s1)):
#     print('before loop',s1[i: i + length])
#     if s1[i: i + length] == s2:
#         print('Sliced string: ', s1[i: i + length])
#         print('String found at position: ', s1.find(s1[i: i + length], i))

'''----------------------Replacing a String with another String----------------------'''
# char = 'That is a beautiful girl'
# s1 = 'girl'
# s2 = 'car'
# chr = char.replace(s1, s2)
# print(char)
# print(chr)

'''---------------------------Splitting and Joining Strings---------------------------'''
# num = 'one, two, three, four, five'
# num1 = num.split(',')
# print(num)
# print(num1)

# A Python program to display a group of numbers.

# num = input('Enter the numbers seperated by space: ')
#
# lst = num.split(' ')
#
# for i in lst:
#     print(i, end=' ')

'''------------------------Join Method------------------------'''
# s1 = ['one', 'two', 'three', 'four', 'five']
# s2 = ', '.join(s1)
# print(s1)
# print(s2)
#
# fruit = ('apple', 'guava', 'grapes', 'mango')
# fruit1 = ' : '.join(fruit)
# print(fruit)
# print(fruit1)

'''-------------------------------Changing case of a String-------------------------------'''
# char = 'I am a Python Developer.'
# print(char.upper())
# print(char.lower())
# print(char.swapcase())
# print(char.title())

'''-----------------------Checking Starting and Ending of a String-----------------------'''
# char = 'Python is the future'
# print(char.startswith('Python'))
# print(char.endswith('future'))

'''------------------------String Testing Methods------------------------'''

# char = 'Delhi'
# print(char.isalnum())
# print(char.isalpha())
# print(char.isdigit())
# print(char.isupper())
# print(char.islower())
# print(char.isspace())
# print(char.istitle())

'''-------------------------Formating Strings-------------------------'''

# id = 10
# Name = 'Shankar'
# Salary = 9080.5
# print('Id = {}, Name = {}, Salary = {}'.format(id, Name, Salary))

# id = 10
# Name = 'Shankar'
# Salary = 19500.75
# print('Id = {0}\tName = {1}\tSalary = {2}'.format(id, Name, Salary))

'''----------------------------Working with Characters----------------------------'''
# char = 'Hello'
# ch = char[0]
# print(ch)
# ch = char[1]
# print(ch)
# ch = char[0:3]
# print(ch)
# print(char.isalpha())
# print(char.isalnum())

# A Python program to know the type of character entered by the user.

# char = input('Enter the character: ')
# ch = char[0]
#
# if ch.isalnum():
#     print('Entered character is either alphabet or number.')
#     if ch.isalpha():
#         print('Entered character is alphabets.')
#         if ch.isupper():
#             print('Entered character is in upper case.')
#         else:
#             print('Entered character is in lower case.')
#     else:
#         print('Entered character is digit.')
# elif ch.isspace():
#     print('Entered character is space.')
# else:
#     print('Entered character is special character.')

# A Python program to sort a group of string into ascending order.

# lst = []
#
# n = int(input('Enter the number of string: '))
#
# print('Enter the string: ')
# for i in range(n):
#     lst.append(input())
#
# srt = sorted(lst)
#
# print('Sorted string: ')
# for i in srt:
#     print(i)

# char = input('Enter the main string: ')
# sub = input('Enter the sub string: ')
# length = len(sub)
#
# for i in range(len(char)):
#     if char[i : i + length] == sub:
#         print('String found at position: ', char.find(char[i : i + length], i))

# A Python program to search for the position of a string in a given group of strings.

# s1 = []
#
# n = int(input('Enter the number of strings: '))
#
# print('Enter the string: ')
# for i in range(n):
#     s1.append(input())
#
# s2 = input('Enter the string to search: ')
#
# for i in range(len(s1)):
#     if s1[i] == s2:
#         print('String found at position: ', i)

# A Python program to find the length of a string without using len() function.

ch = input('Enter the string: ')

i = 0
for i in range(len(ch)):
    print(ch[i], end='')
    i += 1
print()
print('No. of characters: ', i)