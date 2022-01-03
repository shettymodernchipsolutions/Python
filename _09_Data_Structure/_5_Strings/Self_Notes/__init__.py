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
#s = 'Practice makes 'Perfect''
#print(s)
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

s1 = "python"
s2 = "PYTHON"

if s1.upper() == s2.upper():
    print("String values are equal.")
else:
    print("String values are not equal")