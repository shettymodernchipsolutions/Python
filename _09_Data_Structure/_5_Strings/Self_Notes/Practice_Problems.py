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

# ch = input('Enter the string: ')
#
# i = 0
# for i in range(len(ch)):
#     print(ch[i], end='')
#     i += 1
# print()
# print('No. of characters: ', i)

# A Python program to find the number of words in a string.

# char = input('Enter the string: ')
#
# i = 0
# c = 1
# flag = True
#
# for s in range(len(char)):
#     if flag == False and char[i] == ' ':
#         c += 1
#     if char[i] == ' ':
#         flag = True
#     else:
#         flag = False
#     i += 1
#
# print('No. of words: ', c)
#
# char = input('Enter the string: ')
# words = []
#
# for i in char.split():
#     words.append(i)
#
# print('No. of words: ', len(words))

# class A:
#     def __init__(self):
#         self.name = 'Bhavesh'
#         self.age = 30
#
#
# B = A()
# print(B.__dict__)
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_dict = {n: n * n for n in lst}
# print(my_dict)

# print('Total words',len([x for x in input('Enter :').split()]))
#
# letter1=[]
# for word in input('enter :').split():
#     letter1.append(word[0])
# print(letter1)
#
# c=[word[0] for word in input('enter :').split()]
# print(c)

# A Python program to insert a sub string in a string in a particular position.

# s1 = input('Enter the main string: ')
# s2 = input('Enter the sub string: ')
# n = int(input('Enter the position no.: '))
#
# l1 = len(s1)
# l2 = len(s2)
#
# lst = []
#
# for i in range(n):
#     lst.append(s1[i])
#
# for i in range(l2):
#     lst.append(s2[i])
#
# for i in range(n, l1):
#     lst.append(s1[i])
#
# lst = ''.join(lst)
#
# print('The main string after inserting sub string: ', lst)

# s1 = input('Enter the main string: ')
# s2 = input('Enter the sub string: ')
#
# if s2 in s1:
#     print(s2+' found in s1')
# else:
#     print(s2+' not found in s1')

# s1 = input('Enter the main string: ')
# s2 = input('Enter the sub string: ')
#
# n = s1.find(s2, 0, len(s1))
#
# if n == -1:
#     print(s2+' not found.')
# else:
#     print(s2+' found in s1.')

# n1 = input('Enter the main string: ')
# n2 = input('Enter the sub string: ')
#
# try:
#     s = n1.index(n2, 0, len(n1))
# except ValueError:
#     print('Sub string not found.')
# else:
#     print('Sub string found at position: ', s)

# s1 = input('Enter the main string: ')
# s2 = input('Enter the sub string: ')
# n = len(s2)
#
# for i in range(len(s1)):
#     if s1[i: i + n] == s2:
#         print('String found at position: ', s1.find(s1[i: i + n], i))

# s1 = input('Enter the main string: ')
# s2 = input('Enter the sub string: ')
# i = 0
# flag = False
# n = len(s1)
# while i < n:
#     pos = s1.find(s2, i, n)
#     if pos != -1:
#         print('String found at position: ', pos)
#         i = pos + 1
#         flag = True
#     else:
#         i += 1
#
# if flag == False:
#     print('String not found.')

# s1 = input('Enter the main string: ')
# s2 = input('Enter the sub string: ')
# pos = -1
# flag = False
# n = len(s1)
#
# print('String found at position: ')
# while True:
#     pos = s1.find(s2, pos + 1, n)
#     if pos == -1:
#         break
#
#     if pos != -1:
#         print(pos)
#         flag = True
#
# if flag == False:
#     print('Strin not found.')

# s1 = input('Enter the main string: ')
# s2 = input('Enter the sub string: ')
# i = 0
# flag = False
# n = len(s1)
#
# while i < n:
#     pos = s1.find(s2, i, n)
#     if pos != -1:
#         print('String found at position: ', pos)
#         i = pos + 1
#         flag = True
#     else:
#         i += 1
# if flag == False:
#     print('String not found.')

# s1 = input('Enter the main string: ')
# s2 = input('Enter the sub string: ')
# l = len(s2)
#
# for i in range(len(s1)):
#     if s1[i: i + l] == s2:
# print('String found at position: ', s1.find(s1[i: i + l], i))

# s1 = input('Enter the main string: ')
# s2 = input('Enter the sub string: ')
# pos = -1
# flag = False
# n = len(s1)
# while True:
#     pos = s1.find(s2, pos + 1, n)
#     if pos == -1:
#         break
#
#     print('String found at position: ', pos)
#     flag = True
#
# if flag == False:
#     print('String not found.')

# cahr = input('Enter the number seperated by spaces: ')
#
# lst = cahr.split(' ')
#
# for i in lst:
#     print(i, end=' ')

# char = input('Enter the string: ')
# lst = char[0]
#
# if lst.isalnum():
#     print('Enter character is either string or digits.')
#     if lst.isalpha():
#         print('Entered character is a string.')
#         if lst.isupper():
#             print('Entered character is in upper case.')
#         else:
#             print('Entered character is in lower case.')
#     else:
#         print('Entered character is digits.')
# elif lst.isspace():
#     print('Enter character is space.')
# else:
#     print('Enter character is a special character.')

# char = []
#
# n = int(input('Enter the no. of strings: '))
#
# print('Enter the string: ')
# for i in range(n):
#     char.append(input())
#
# s = sorted(char)
#
# print('Sorted string: ')
# for i in s:
# print(i)

# n = input('Enter the string seperated by spaces: ')
#
# s = n.split(' ')
#
# for i in s:
#     print(i, end=' ')

# char = []
#
# n = int(input('Enter the no. of strings: '))
#
# print('Enter the string: ')
# for i in range(n):
#     char.append(input())
#
# s = sorted(char)
#
# print('Sorted string: ')
# for i in s:
#     print(i)

# s = []
#
# n = int(input('Enter the no. of strings: '))
#
# print('Enter the string: ')
# for i in range(n):
#     s.append(input())
#
# t = input('Enter the string to search: ')
#
# flag = False
#
# for i in range(len(s)):
#     if s[i] == t:
#         print('String found at position: ', i)
#         flag = True
#
# if flag == False:
#     print('String not found.')

# char = input('Enter the string: ')
# count = 0
#
# print('String: ')
# for i in char:
#     print(char[count], end='')
#     count += 1
# print()
#
# print('Length of the string: ', count)

# s = input('Enter the string: ')
#
# c = 1
# i = 0
# flag = False
#
# for i in range(len(s)):
#     if flag == False and s[i] == ' ':
#         c += 1
#
#     if s[i] == ' ':
#         flag = True
#     else:
#         flag = False
#     i += 1
#
# print('No. of words: ', c)

# s1 = input('Enter the main string: ')
# s2 = input('Enter the sub string: ')
#
# n = int(input('Enter the position at which you want to insert sub string: '))
#
# ch = []
#
# for i in range(n):
#     ch.append(s1[i])
#
# for i in range(len(s2)):
#     ch.append(s2[i])
#
# for i in range(n, len(s1)):
#     ch.append(s1[i])
#
# ch = ''.join(ch)
#
# print('After inserting sub string: ', ch)

# for i in range(10, 15, 1):
#     print(i, end=',')
# print()
#
# my_tuple = [x for x in range(1, 6, 1)]
# print(my_tuple)

# n = input('Enter the number seperated by spaces: ')
#
# lst = n.split(' ')
#
# for i in lst:
#     print(i, end=' ')

# lst = []
#
# n = int(input('Enter the number of strings: '))
#
# print('Enter the string: ')
# for i in range(n):
#     lst.append(input())
#
# ch = sorted(lst)
#
# print('Sorted string: ')
# for i in ch:
#     print(i)

# ch = []
#
# n = int(input('Enter the number of strings: '))
#
# print('Enter the string: ')
# for i in range(n):
#     ch.append(input())
#
# s = input('Enter the string to search: ')
#
# for i in range(len(ch)):
#     if ch[i] == s:
#         print('String found at position: ', i)

# char = input('Enter the string: ')
#
# i = 0
# print('Entered string: ')
# for s in range(len(char)):
#     print(char[i], end='')
#     i += 1
# print()
# print('Length of String: ', i)

# char = input('Enter the string: ')
# sum = 0
# print(len(char.split()))
# for ch in char.split():
#     character = len(ch)
#     sum = sum + character
#
# average = sum / len(char.split())
# print(average)

# char = input('Enter the string: ')
# print('Length of words: ', len(char.split()))

# char = input('Enter the strings: ')
#
# i = 0
# c = 1
# flag = True
# for s in char:
#     if flag == False and char[i] == ' ':
#         c += 1
#     if char[i] == ' ':
#         flag = True
#     else:
#         flag = False
#     i += 1
#
# print('No. of words: ', c)

# char = input('Enter the main string: ')
# sub = input('Enter the sub string: ')
#
# i = 0
# flag = False
# n = len(char)
# while i < n:
#     pos = char.find(sub, i, n)
#     if pos != -1:
#         print('String found at position: ', pos)
#         i = pos + 1
#         flag = True
#     else:
#         i += 1
#
# if flag == False:
#     print('String not found.')

# s1 = input('Enter the main string: ')
# s2 = input('Enter the sub string: ')
#
# pos = -1
# flag = False
# n = len(s1)
# while True:
#     pos = s1.find(s2, pos + 1, n)
#     if pos == -1:
#         break
#
#     print('String found at position: ', pos)
#     flag = True
#
# if flag == False:
#     print('String not found.')

# A Python program to access each element of a string in forward and reverse orders using while loop.

# char = input('Enter the string: ')
# n = len(char)
# i = 0
# while i < n:
#     print(char[i], end=' ')
#     i += 1
# print()
#
# i = -1
# while i >= -n:
#     print(char[i], end=' ')
#     i -= 1
# print()
#
# i = 1
# while i <= n:
#     print(char[-i], end=' ')
#     i += 1

# A Python program to access the characters of the string using for loop.

# char = input('Enter the string: ')
#
# for i in range(len(char)):
#     print(char[i], end=' ')
#     i += 1
# print()
#
# n = len(char)
#
# for i in char[::-1]:
#     print(i, end=' ')

# A Python program to know whether a sub string exists in main string or not.

# s1 = input('Enter the main string: ')
# s2 = input('Enter the main string: ')
# if s2 in s1:
#     print(s2+' found in s1.')
# else:
#     print(s2+' not found.')

# A Python program to find the first occurence of sub string in a given main string.

# s1 = input('Enter the main string: ')
# s2 = input('Enter the main string: ')
#
# n = s1.find(s2, 0, len(s1))
#
# if n == -1:
#     print(s2+' not found in s1.')
# else:
#     print(s2+' found in s1.')

# A Python program to find the first occurence of sub string in a given main string using index() method.

# s1 = input('Enter the main string: ')
# s2 = input('Enter the main string: ')
#
# try:
#     n = s1.index(s2, 0, len(s1))
# except ValueError:
#     print(s2+' not found in s1.')
# else:
#     print(s2+' found in s1.')

# A Python program to display all positions of a sub string in a given main string.

# s1 = input('Enter the main string: ')
# s2 = input('Enter the main string: ')
#
# i = 0
# flag = False
# n = len(s1)
# while i < n:
#     pos = s1.find(s2, i, n)
#     if pos != -1:
#         print('String found at position: ', pos)
#         i = pos + 1
#         flag = True
#     else:
#         i += 1
#
# if flag == False:
#     print('String not found.')

# A Python program to display all positions of a sub string in a given main string. - version 2.

# s1 = input('Enter the main string: ')
# s2 = input('Enter the main string: ')
#
# n = len(s1)
# pos = -1
# flag = False
# while True:
#     pos = s1.find(s2, pos + 1, n)
#     if pos == -1:
#         break
#
#     print('String found at position: ', pos)
#     flag = True
#
# if flag == False:
#     print('String not found.')

# A Python program to know the type of character entered by the user.


# A Python program to sort a group of string into ascending order.

# char = []
#
# n = int(input('Enter the number of strings: '))
#
# print('Enter the string: ')
# for i in range(n):
#     char.append(input())
#
# ch = sorted(char)
#
# print('Sorted string: ')
# for i in ch:
#     print(i)

# A Python program to search for the position of a string in a given group of strings.

# char = []
#
# n = int(input('Enter the no. of string: '))
#
# print('Enter the string: ')
# for i in range(n):
#     char.append(input())
#
# ch = input('Enter the string to search: ')
#
# for i in range(len(char)):
#     if char[i] == ch:
#         print('String found at position: ', i)


# A Python program to find the length of a string without using len() function.

# char = input('Enter the string: ')
#
# i = 0
# print('Entered String: ')
# for i in range(len(char)):
#     print(char[i], end='')
#     i += 1
# print()
#
# print('Length of the string: ', i)

# A Python program to find the number of words in a string.

# char = input('Enter the string: ')
# print('Number of words: ', len(char.split()))
# i = 0
# count = 1
# flag = False
# for s in char:
#     if flag == False and char[i] == ' ':
#         count += 1
#     if char[i] == ' ':
#         flag = True
#     else:
#         flag = False
#     i += 1
#
# print('No. of words: ', count)

# A Python program to insert a sub string in a string in a particular position.

# s1 = input('Enter the main string: ')
# s2 = input('Enter the sub string: ')
#
# n = int(input('Enter the position at which you want to insert sub string: '))
#
# l1 = len(s1)
# l2 = len(s2)
#
# ch = []
#
# for i in range(n):
#     ch.append(s1[i])
#
# for i in range(l2):
#     ch.append(s2[i])
#
# for i in range(n, l1):
#     ch.append(s1[i])
#
# ch = "".join(ch)
#
# print('After inserting the sub string: ', ch)

# s1 = input('Enter the main string: ')
# s2 = input('Enter the sub string: ')
# l = len(s2)
#
# for i in range(len(s1)):
#     if s1[i: i + l] == s2:
#         print('String found at position: ', s1.find(s1[i: i + l], i))
