# n = int(input('Enter the number: '))
# t = n
# r = 0
# while n > 0:
#     dig = n % 10
#     r = r * 10 + dig
#     n = n // 10
#
# if t == r:
#     print('Entered number is palindrome.')
# else:
#     print('Entered number is not palindrome.')

# def isPalindrome(x):
#     return str(x) == str(x)[::-1]
#
#
# palindrome = int(input('Enter the number: '))
#
# for x in range(palindrome):
#     for y in range(palindrome):
#         if ( x + y < palindrome) and isPalindrome(x + y):
#             print(x + y)


from itertools import permutations


num = int(input('Enter the number: '))

n = str(num)

char = []

palin = permutations(n, len(n))

for i in palin:
    t = ''.join(i)
    if t == t[::-1]:
        char.append(t)

s = set(char)

for i in s:
    print(i)

# def ret_pallindrome(num: str):
#     a = 0
#     outnum = [[], []]
#     if len(num) % 2 == 0:
#         a = 1
#     dic1 = {}
#     for i in num:
#         if i not in dic1:
#             dic1[i] = num.count(i)
#     # print(dic1)
#     if a == 1:
#         for key, value in dic1.items():
#             if value % 2 != 0:
#                 return -1
#             else:
#                 for _ in range(value // 2):
#                     outnum[0].append(key)
#                     outnum[1].append(key)
#         outnum = outnum[0] + outnum[1][::-1]
#         # print(outnum)
#         return ''.join(outnum)
#     if a == 0:
#         temp_list = []
#         for key, value in dic1.items():
#             if value % 2 == 0:
#                 temp_list.append(True)
#                 for _ in range(value // 2):
#                     outnum[0].append(key)
#                     outnum[1].append(key)
#             else:
#                 temp_list.append(False)
#                 key1 = key
#                 value1 = value
#                 # print(temp_list)
#         outnum[0] += [key1 * value1]
#         if temp_list.count(False) > 1:
#             return -1
#         else:
#             outnum = outnum[0] + outnum[1][::-1]
#             # print(outnum)
#             return ''.join(outnum)

import itertools
# largest_no = -1
innum = int(input("Enter a Number"))
a = str(innum)
lst = []
for i in itertools.permutations(a):
    x = ''.join(i)
    if x == x[::-1]:
        lst.append(x)
print(set(lst))