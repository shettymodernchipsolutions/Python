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

#lst = [10, 20, 30, 40, 50, 20]

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

