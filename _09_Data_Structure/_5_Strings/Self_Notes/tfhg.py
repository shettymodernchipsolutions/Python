# s1 = ""
# print(s1)
# s2 = "p"
# print(s2)
# s3 = "Python"
# print(s3)
# s4 = '''C
# Java
# Python'''
# print(s4)
# s5 = str(99.5)
# print(s5)
# print(type(s5))

# s = 'Practice makes Perfect'
# print(s)
# s = 'Practice makes 'Perfect''
# print(s)
#
# s = 'Practice makes "Perfect"'
# print(s)
#
# # s = "Practice makes "Perfect""
# # print(s)
#
# s = "Practice makes \"Perfect\""
# print(s)
#
# str = 'Python'
# print(str)
# print(str[2])
# for i in str:
#     print(i)
#
# s = 'Python'
# print(s[4])
# s[4] = 'i'
# print(s)
#
# s1 = "Hello"
# s2 = "World"
# print(s1)
# print(s2)
# print(id(s1))
# print(id(s2))
# print(s1[4])
# print(s2[1])
# print(id(s1[4]))
# print(id(s2[1]))
#
# s1 = 'P'
# s2 = 'P'
# print(s1)
# print(s2)
# print(id(s1))
# print(id(s2))
#
# s1 = "hello"
# s2 = "world"
# print(s1,s2)
# print(id(s1),id(s2))
# print(s1[2],s1[3],s2[3])
# print(id(s1[2]),id(s1[3]),id(s2[3]))
# print(s1[4],s2[1])
# print(id(s1[4]),id(s2[1]))
# print(s1[4] is s2[1])

# s = "Guido Van Rossum"
# print(s)
# print(s[10])
# print(s[0:5])
# print(s[-12:-17:-1])
# print(s[0:5:2])
# print(s[6:9])
# print(s[-8:-12:-1])
# print(s[6:9:2])
# print(s[10:16])
# print(s[-1:-7:-1])
# print(s[10:16:2])
# print(s[15:9:-1])
# print(s[::-1])

# s = input("Enter a string: \n")
#
# for i in range(0,len(s)-2):
#     print(s[i:i+3])

# s = input("Enter the string: \n")
# print(s[1:len(s)-1])
#
# s = input("Enter the string: \n")
# print(s[len(s)-2:0:-1])

# s1 = input("Enter the string: ")
# s2= s1[::-1]
#
# if s1 == s2:
#     print("Entered string is palindrome.")
# else:
#     print("Not a palindrome")

# s1 = "Python"
# s2 = "Python"
#
# if s1 == s2:
#     print("String values are equal.")
# else:
#     print("String values are not equal.")
#
# s1 = "Python"
# s2 = "Java"
#
# if s1 == s2:
#     print("String values are equal.")
# else:
#     print("String values are not equal.")


# s1 = "Python"
# s2 = "Python"
#
# if id(s1) == id(s2):
#     print("String references are equal.")
# else:
#     print("String references are not equal.")
#
# s1 = "Python"
# s2 = "Java"
#
# if id(s1) == id(s2):
#     print("String references are equal.")
# else:
#     print("String references are not equal.")
#
# s1 = "Python"
# s2 = "Python"
#
# if s1 is s2:
#     print("String references are equal.")
# else:
#     print("String references are not equal.")
#
# s1 = "Python"
# s2 = "Java"
#
# if id(s1) == id(s2):
#     print("String references are equal.")
# else:
#     print("String references are not equal.")

# s1 = "python"
# s2 = "PYTHON"
#
# if s1 == s2:
#     print("String values are equal.")
# else:
#     print("String values are not equal.")
#
# s1 = "python"
# s2 = "PYTHON"
#
# if s1 is s2:
#     print("String references are equal.")
# else:
#     print("String references are not equal.")

# s = "Python"
# print(s[:len(s)//2:]
#       +
#       s[len(s)-1:(len(s)//2)-1:-1])

# s = input("Enter the string: \n")
# print(s[:len(s)//2:]
#       +
#       s[len(s)-1:(len(s)//2)-1:-1])
#
# s = "hello" + "world"
# print(s)

# s = "hello"
# print(s)
# s + "world"
# print(s)

# s1 = "hello"
# print(s1)
# s2 = s1 + "world"
# print(s1)
# print(s2)

# s = "hello"
# print(s)
# s = s + "world"
# print(s)

# s = 'a'
# print(ord(s))
# print(ord(s)-32)
# print(chr(ord(s)-32))
#
# s = 'y'
# print(ord(s))
# print(ord(s)-32)
# print(chr(ord(s)-32))
#

# s = input("Enter a string: \n")
# s_upper = ""
# for i in s:
#     if ord(i) >= 97 and ord(i) <=122:
#         s_upper += chr(ord(i) - 32)
#     else:
#         s_upper += i
#
# print(s)
# print(s_upper)
#
# s = input("Enter a string: \n")
# s_upper = s.upper()
#
# print(s)
# print(s_upper)

# s = input("Enter a string: \n")
# s_lower = s.lower()
#
# print(s)
# print(s_lower)

# s1 = "python"
# s2 = "PYTHON"
#
# if s1 == s2:
#     print("String values are equal.")
# else:
#     print("String values are not equal")

# s1 = "python"
# s2 = "PYTHON"
#
# if s1.upper() == s2.upper():
#     print("String values are equal.")
# else:
#     print("String values are not equal")
#
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
# st = 'Core Python'
#
# t = len(st)
#
# i = 0
#
# while i < t:
#     print(st[i], end=' ')
#     i += 1
#
# print()
#
# i = -1
#
# while i >= -t:
#     print(st[i], end=' ')
#     i -= 1
#
# print()
#
# i = 1
#
# while i <= t:
#     print(st[-i], end=' ')
#     i += 1

# # A program to access each element of a string in forward and reverse orders using while loop
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


# A program to access character of a string using for loop

# str = 'Core Python'
#
# for i in str:
#     print(i, end=' ')
#
# print()
#
# for i in str[::-1]:
#     print(i, end=' ')


# # A python program to know whether a sub string exists in main string or not
#
# char = input("Enter the main string: ")
# sub = input("Enter the sub string: ")
# if sub in char:
#     print(sub + ' is found in main string')
# else:
#     print(sub + ' not found in main string')


# char = 'Core Python'
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
# i = 1
#
# print()
#
# while i <= n:
#     print(char[-i], end=' ')
#     i += 1


# chr = 'Core Python'
#
# for i in chr:
#     print(i, end=' ')
#
# print()
#
# for i in chr[::-1]:
#     print(i, end=' ')
#
# print()
#
# char = input("Enter the string: ")
# sub = input("Enter the string: ")
#
# if sub in char:
#     print(sub + ' is present in char')
# else:
#     print(sub + ' is not present in char')


# A program to find the first occurence of sub string in a given main string.

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
# stat = input('Enter the string: ')
# ghy = input("Enter the string: ")
#
# n = stat.find(ghy, 0, len(stat))
#
# if n == -1:
#     print("Sub string is not found")
# else:
#     print("Sub sting is found at position", n + 1)


# A Python program to find the first occurence of sub string in a given main string using index() method.
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


# char = input("Enter the string: ")
# chr = input("Enter the sub string: ")
#
# try:
#     n = char.index(chr, 0, len(char))
# except ValueError:
#     print("Sub string is not found")
# else:
#     print("Sub string is found at position", n + 1)


# A Python program to display all positions of a sub string in a given main string.

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


# char = 'Core Python'
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
# print()
#
# char = 'Core Python'
#
# for i in char:
#     print(i, end=' ')
#
# print()
#
# for i in char[::-1]:
#     print(i, end=' ')
#
# print()
#
# str = input("Enter the string: ")
# sub = input("Enter the string: ")
#
# if sub in str:
#     print(sub + ' string found in str')
# else:
#     print(sub + ' string not found in str')
#
# print()
#
# char = input('Enter a string: ')
# chr = input('Enter a sub string: ')
#
# n = char.find(chr, 0, len(char))
#
# if n == -1:
#     print("Sub string not found")
# else:
#     print("Sub string found at position ", n + 1)


# char = input("Enter a string: ")
# chr = input("Enter a string: ")
#
# try:
#     n = char.index(chr, 0, len(char))
# except ValueError:
#     print("Sub string not found")
# else:
#     print("Sub string found at position", n + 1)
#
# char = input("Enter a string: ")
# chr = input("Enter a sub string: ")
#
# n = len(char)
# flag = False
# i = 0
#
# while i < n:
#     pos = char.find(chr, i, n)
#     if pos != -1:
#         print('Sub string found at position: ', pos + 1)
#         i = pos + 1
#         flag = True
#     else:
#         i += 1
#
# if flag == False:
#     print('Sub string not found')
#


# char = input("Enter a string: ")
# chr = input("Enter a sub string: ")
#
# flag = False
# i = 0
# n = len(char)
#
# while i < n:
#     pos = char.find(chr, i, n)
#     if pos != -1:
#         print("Sub string found at position ", pos + 1)
#         i = pos + 1
#         flag = True
#     else:
#         i += 1
# if flag == False:
#     print("Sub string not found")

# A Python program to display all positions of a sub string in a given main string.

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


# s = '     I am a Python Developer       '
# print(s.lstrip())
# print(s.rstrip())
# print(s.strip())


# A Python program to accept and display a group of numbers.

# char = ['10', '20', '30', '40', '50']
#
# str = ':'
#
# char1 = str.join(char)
#
# print(char1)

# str = 'Python is the future'
#
# str = str.upper()
# str = str.lower()


# A Python program to find the length of a string without using len() function.

# str = input('Enter the string: ')
#
# s = 0
#
# for i in str:
#     print(str[s], end='')
#     s += 1
#
# print('\nNo. of characters: ', s)

# A Python program to find the number of words in a string.

# str = input('Enter the no. of words to count: ')
#
# i = c = 0
# flag = True
# for s in str:
#     if flag == False and str[i] == ' ':
#         c += 1
#     elif str[i] == ' ':
#         flag = True
#     else:
#         flag = False
#     i += 1
#
# print('No. of words: ', c + 1)

# print(len(str.split()))


# A Python program to insert a sub string in a string in a particular position.

# str = input('Enter a string: ')
# sub = input('Enter a sub string: ')
# n = int(input('Enter the position: '))
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


