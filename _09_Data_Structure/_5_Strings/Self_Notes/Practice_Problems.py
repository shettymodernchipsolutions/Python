# A program to access each element of a string in forward and reverse orders using while loop

# char = 'Bhavesh V Shetty'
#
# n = len(char)
#
# i = 0
#
# while i < n:
#     print(char[i], end=' ')
#     i += 1
#
# print()
#
# i = -1
#
# while i >= -n:
#     print(char[i], end=' ')
#     i -= 1
#
# print()
#
# i = 1
#
# while i <= n:
#     print(char[-i], end=' ')
#     i += 1
#
# # A program to access character of a string using for loop
#
# str = 'Core Python'
#
# print()
# for i in str:
#     print(i, end=' ')
#
# print()
#
# for i in str[::-1]:
#     print(i, end=' ')
#
# # A python program to know whether a sub string exists in main string or not
#
# char = input("\nEnter the main string: ")
# sub = input("Enter the sub string: ")
# if sub in char:
#     print(sub + ' is found in main string')
# else:
#     print(sub + ' not found in main string')
#
# # A program to find the first occurence of sub string in a given main string.
#
# char = input("Enter the string: ")
# chr = input("Enter the string: ")
#
# n = char.find(chr, 0, len(char))
#
# if n == -1:
#     print('Sub string is not found')
# else:
#     print('Sub string is found at position', n + 1)
#
# # A Python program to find the first occurence of sub string in a given main string using index() method.
#
# char = input("Enter the string: ")
# chr = input("Enter the string: ")
#
# try:
#     n = char.index(chr, 0, len(char))
# except ValueError:
#     print("Entered string is not found")
# else:
#     print("Sub string is found at position ", n + 1)
#
#
# # A Python program to display all positions of a sub string in a given main string.
#
# char = input("Enter the string: ")
# chr = input("Enter the sub string : ")
#
# i = 0
# flag = False
# n = len(char)
#
# while i < n:
#     pos = char.find(chr, i, n)
#     if pos != -1:
#         print("Sub string found at position: ", pos + 1)
#         i = pos + 1
#         flag = True
#     else:
#         i += 1
#
# if flag == False:
#     print("Sub string is not found")
#
#
# # A Python program to display all positions of a sub string in a given main string.
#
# char = input("Enter a string: ")
# chr = input("Enter a sub string: ")
#
# i = 0
# flag = False
# n = len(char)
#
# while True:
#     pos = char.find(chr, pos + 1, n)
#     if pos == -1:
#         break
#     print('Sub string found at position: ', pos + 1)
#     flag = True
#
# if flag == False:
#     print('Sub string not found')
#
# # A Python program to find all the positions of a sub string in a given main string.
#
# char = input("Enter a string: ")
# chr = input("Enter the sub string: ")
#
# i = 0
# n = len(char)
# flag = False
#
# while True:
#     pos = char.find(chr, pos + 1, n)
#     if pos == -1:
#         break
#     print('Sub string found at position: ', pos + 1)
#     flag = True
#
# if flag == False:
#     print("Sub string not found")
#
# s = '     I am a Python Developer       '
# print(s.lstrip())
# print(s.rstrip())
# print(s.strip())
#
# # A Python program to accept and display a group of numbers.
#
# char = ['10', '20', '30', '40', '50']
#
# str = ':'
#
# char1 = str.join(char)
#
# print(char1)
#
# str = 'Python is the future'
# print(str)
#
# str = str.upper()
# print(str)
#
# str = str.lower()
# print(str)
#
# str = 'Python is the future'
# str = str.swapcase()
# print(str)
#
# str = 'Python is the future'
# print(str.title())
#
# str = 'Delhi999'
#
# print(str.isalpha())
# print(str.isalnum())
# print(str)
#
# id = 10
# name = 'Shankar'
# sal = 10000
#
# str = '{}, {}, {}'.format(id, name, sal)
#
# print(str)
#
# id = 10
# name = 'Shankar'
# sal = 19500.75
#
# str = 'id= {} \nname= {} \nsal = {}'.format(id, name, sal)
# print(str)
#
# str = 'Delhi999'
# print(str.isalpha())
# print(str.isalnum())
#
# str = 'Udupi'
# print(str.isalnum())
# print(str.isalpha())
# print(str.isascii())
# print(str.isdigit())
# print(str.istitle())
#
# id = 10
# name = 'Shankar'
# sal = 19500.75
#
# str = '{}, {}, {}'.format(id, name, sal)
# print(str)
#
# id = 10
# name = 'shankar'
# sal = 19500.75
#
# str = 'id = {0} \nname = {2} \nsal = {1}'.format(id, name, sal)
#
# print(str)
#
# # A Python program to know the type of character entered by the user.
#
# str = input("Enter the string: ")
# ch = str[0]
#
# if ch.isalnum():
#     print('Entered character is either alphabet or number')
#     if ch.isalpha():
#         print('Entered character is alphabet')
#         if ch.isupper():
#             print('Entered character is upper case')
#         else:
#             print('Entered character is lower case')
#     else:
#         print('Entered character is digit')
# elif ch.isspace():
#     print('Entered charcter is space')
# else:
#     print('Entered  character is special symbol')
#
# # A Python program to accept and display a group of numbers
#
# str = input("Enter the numbers to be displayed: ")
#
# n = str.split(' ')
#
# for i in n:
#     print(i)
#
# str = ['one', 'two', 'three']
#
# str1 = ' '.join(str)
#
# print(str1)
#
# # A Python program to sort the group of string into alphabetical order.
#
# str = []
#
# n = int(input("Enter the number of string: "))
#
# for i in range(n):
#     print('Enter the string: ', end=' ')
#     str.append(input())
#
# str1 = sorted(str)
#
# print('Sorted string: ')
#
# for i in str1:
#     print(i)
#
# # A Python program to search for a string in a given group of string.
#
# str = []
#
# n = int(input("Enter the number of string: "))
#
# for i in range(n):
#     print('Enter the string: ', end=' ')
#     str.append(input())
#
# s = input('Enter the string to search: ')
#
# flag = False
#
# for i in range(len(str)):
#     if s == str[i]:
#         print('Found at position: ', i + 1)
#         flag = True
#
# if flag == False:
#     print('String not found')
#
# # A Python program to find the length of a string without using len() function.
#
# str = input('Enter the string: ')
#
# i = 0
#
# print('Entered string: ')
# for s in str:
#     print(str[i], end='')
#     i += 1
#
# print('\nThe length of th string: ', i)
#
# # A Python program to find the number of words in a string.
#
# str = input('Enter a string: ')
#
# i = c = 0
# flag = True
#
# for s in str:
#     if flag == False and str[i] == ' ':
#         c += 1
#
#     if str[i] == ' ':
#         flag = True
#     else:
#         flag = False
#     i += 1
#
# print('Number of words: ', c + 1)
#
# # A Python program to insert a sub string in a string in a particular position.
#
# str = input('Enter a string: ')
# sub = input('Enter a sub string: ')
# n = int(input('Enter position number: '))
#
# n -= 1
#
# l1 = len(str)
# l2 = len(sub)
#
# str1 = []
#
# for i in range(n):
#     str1.append(str[i])
#
# for i in range(l2):
#     str1.append(sub[i])
#
# for i in range(n, l1):
#     str1.append(str[i])
#
# str1 = ''.join(str1)
#
# print(str1)


# def sub_string(input, j, k):
#   count = 0
#   while j >= 0 and k < len(input):
#     if input[j] != input[k]:
#       break
#     print(input[j: k + 1])
#     count += 1
#
#     j -= 1
#     k += 1
#
#   return count
#
#
# def palindrome_substrings(input):
#   count = 0
#   for i in range(0, len(input)):
#     count += sub_string(input, i - 1, i + 1)
#     count += sub_string(input, i, i + 1)
#
#   return count
#
#
# s = input('Enter the string: ')
# print("Total palindrome substrings: ", palindrome_substrings(s))