'''
Lists

A list object is an ordered collection of one or more data items, not
necessarily of the same type, put in square brackets

We can access single elements from list by using positive indices
or negative.

Lists are mutable, which means we can append elements and remove
whenever needed. By using append() and remove() respectively.
'''

# lst = [10, 20, 30, 40, 50]
# print(lst)
#
# lst = [10, 20.5, True, 1+3j, "Python"]
# print(lst)


#


# lst = [10, 20, 30, 40, 50, 60, 70]
#
# for i in lst:
#     print(i)
#
# lst = [10, 20, 30, 40, 50, 60, 70]
#
# for i in range(0,7):
#     print("\n",lst[i])
#
# lst = [10, 20, 30, 40, 50, 60, 70]
#
# for i in range(0,len(lst)):
#     print("\n",lst[i])


# lst = [10, 20, 30, 40, 50]
# print(lst)
# lst.insert(2, 99)
# print(lst)

# lst = [10, 20, 30, 40, 50]
# print(lst)
# lst[2] = 300
# print(lst)

# lst = [10, 20, 30, 40, 50]
# print(lst)
# lst[1:4] = 99 #Can only assign an iterable
# print(lst)

# lst = [10, 20, 30, 40, 50]
# print(lst)
# lst[1:4] = [99]
# print(lst)

# lst = [10, 20, 30, 40, 50]
# print(lst)
# lst[1:4] = [99, 88, 77]
# print(lst)
#
# lst = [10, 20, 30, 40, 50]
# print(lst)
# lst[1:4] = [99, 88, 77, 66]
# print(lst)

# lst = [10, 20, 30, 40, 50]
# print(lst)
# lst[::2] = [99, 99, 99]
# print(lst)


# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(lst)
# del lst[3]
# print(lst)

# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(lst)
# del lst[2:8]
# print(lst)

# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(lst)
# del lst[::2]
# print(lst)

# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(lst)
# del lst[-4:-9:-1]
# print(lst)

# lst1 = [10, 20, 30, 40, 50]
# lst2 = lst1[:]
# print(lst1)
# print(lst2)
# print(id(lst1))
# print(id(lst2))
# print(lst1 is lst2)

lst1 = [10, 20, 30, 40, 50]
lst2 = list(lst1)
print(lst1)
print(lst2)
print(id(lst1))
print(id(lst2))
print(lst1 is lst2)

# lst = [10, 20, 30, 40, 50]
# print(len(lst))
# print(max(lst))
# print(min(lst))
# print(sum(lst))

# lst = [10, 20, 30, 40, 50]
# for i in range(len(lst)):
#     print(i, lst[i])

# lst = [10, 20, 30, 40, 50]
# for i,j in enumerate(lst):
#     print(i, j)

# lst = [10, 20, 30, 40, 50, 20]

# print(lst)
# print(lst.count(20))
# print(lst.index(40))
# #print(lst.index(400))
# print(lst.index(20))
# print(lst.index(20, 2, 6))

# lst = [10, 20, 30, 40, 50, 20]
# print(lst)
# lst.clear()
# print(lst)


lst = [10, 20, 30, 40, 50]
print('Total list: ', lst)
print('First element = %d, Last element = %d' % (lst[0], lst[4]))

str = ['dilip', 'vaani', 'harish', 'harsha', 'akash']
print('string elementS: ', str)
print('First String Element = %s, Last string Element = %s' % (str[0], str[4]))

dec = [2, 5, 2.3, 6, 45.7, 89, 5.7]
print('Decimal Elements: ', dec)
print('First Decimal Element = %d, Last Decimal Element = =%s' % (dec[0], dec[6]))

gti = [10, 20, 30, 40, 50]
print('The list elements are : ', gti)
print('First Element = %d, Last Element = %d' % (gti[0], gti[4]))

tghi = ['dkadk', 'bcjadb', 'nbdakb', 'hbadkhhb', 'davkvh']
print('The String elements are: ', tghi)
print('First Elements  = %s, Last Elements = %s' % (tghi[0], tghi[4]))

ced = [2, 5, 3, 3.45, 8.64, 9]
print('Ced elements are: ', ced)
print('First element = %s, Last Element = %s' % (ced[0], ced[5]))

# A python program to create list using range() function

list1 = range(10)
for i in list1:
    print(i, ',', end=' ')
print()

list2 = range(5, 10)
for i in list2:
    print(i, ', ', end=' ')
print()

list3 = range(5, 20, 2)
for i in list3:
    print(i, ', ', end=' ')
print()

# A python program to access list elements using loops

lst = [10, 20, 30, 40, 50]
print('Using while loop')
i = 0
while i < len(lst):
    print(lst[i])
    i += 1

print('Using for loop')
for i in lst:
    print(i)

lst = [10, 20, 30, 40, 50]
print('Using while loop')
i = 0
while i < len(lst):
    print(lst[i])
    i += 1

print('Using for loop')
for i in lst:
    print(i)

day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(day)
print('In reverse order')
i = 0
i = len(day) - 1
while i >= 0:
    print(day[i])
    i -= 1

print('In reverse order')
i = -1
while i >= -len(day):
    print(day[i])
    i -= 1

deas = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(deas)
print('In reverse order')
i = len(deas) - 1
while i >= 0:
    print(deas[i])
    i -= 1

print('In reverse order')
i = -1
while i >= -len(deas):
    print(deas[i])
    i -= 1
