"""
Iterator
------------
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods
__iter__() and __next__().


Iterable - Iterable consists of only __iter__() method.
Iterator - Iterator consists of both __iter__() & __next__() method.
"""

# lst = [100, 200, 300, 400, 500]  # this belongs to a class called as list

# for i in lst:
#     print(i)

# print(dir(lst))
# print(dir(tuple))
# print(dir(set))
# print(dir(int))
# print(dir(set))
# print(dir(set))
# print(dir(dict))
# print(dir(float))
# print(iter(lst))

# lst_itr = iter(lst)  # lst.__iter__(), this belongs to class called as list_iterator.
# print(next(lst_itr))    # lst_itr.__next__()
# print(next(lst_itr))
# print(next(lst_itr))
# print(next(lst_itr))
# print(next(lst_itr))
# print(next(lst_itr))  # Here it encounters 'Stop iteration'

# for i in lst_itr:
#     print(i)


# lst = [100, 200, 300, 400, 500]
#
# lst_itr = iter(lst)
#
# while True:
#     i = next(lst_itr)  # this line will give 'StopIteration' error


# lst = [100, 200, 300, 400, 500]
#
# lst_itr = iter(lst)
#
# while True:
#     try:
#         i = next(lst_itr)
#     except StopIteration:
#         print('Elements iterated completely')
#         break
#     print(i)


# class MyItr:
#
#     def __init__(self, n):
#         self.n = n
#
#     def __iter__(self):
#         self.count = 0
#         return self
#
#     def __next__(self):
#         if self.count < self.n:
#             self.count += 1
#             return self.count
#         else:
#             raise StopIteration
#
#
# def main():
#
#     m = MyItr(10)
#
#     itr = iter(m)
#
#     # print(next(itr))
#     # print(next(itr))
#     # print(next(itr))
#     # print(next(itr))
#     # print(next(itr))
#     # print(next(itr))
#     # print(next(itr))
#     # print(next(itr))
#     # print(next(itr))
#     # print(next(itr))
#
#     for i in itr:
#         print(i)
#
#
# main()


# class Isstr:
#
#     def __init__(self, n):
#         self.n = n
#
#     def __iter__(self):
#         self.count = 0
#         return self
#
#     def __next__(self):
#         if self.count < self.n:
#             self.count += 1
#             return self.count
#         else:
#             raise StopIteration
#
#
# def main():
#     i = Isstr(20)
#     itr = iter(i)  # m.__iter__()

# print(next(itr))  # itr.__next__()
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
#     for i in itr:
#         print(i)
#
#
# main()


# class Mul:
#
#     def __init__(self, num, n):
#         self.num = num
#         self.n = n
#
#     def __iter__(self):
#         self.count = 0
#         return self
#
#     def __next__(self):
#         if self.count < self.n:
#             self.count += 1
#             return self.count * self.num
#         else:
#             raise StopIteration
#
#
# def main():
#     m = Mul(10, 870909)
#     itr = iter(m)
#
#     for i in itr:
#         print(i)
#
#
# main()


# class Mul:
#
#     def __init__(self, num, n):
#         self.num = num
#         self.n = n
#
#     def __iter__(self):
#         self.count = 0
#         return self
#
#     def __next__(self):
#         if self.count < self.n:
#             self.count += 1
#             return self.count * self.num
#         else:
#             raise StopIteration
#
#
# def main():
#     m = Mul(10, 10)
#
#     itr = iter(m)

# print(next(itr))
# print(next(itr))
# print(next(itr))

#     for i in itr:
#         print('Multiples of 10 is: ', i)
#
#
# main()

'''
Advantages of Iterator:
--> Memory efficient

'''

# def num(n):
#     count = 0
#         count < n:
#         count += 1
#         return count
#
#
# def main():
#     n = num(5)
#     print(n)
#     print(n)
#
#
#
# main()


# def num(n):
#     count = 0
#     while count < n:
#         count += 1
#         yield count
#
#
# def main():
#     n = num(10)
#     # print(next(n))
#     # print(next(n))
#     # print(next(n))
#     # print(next(n))
#     # print(next(n))
#
#     for i in n:
#         print(i)
#
#
# if __name__ == '__main__':
#     main()


# def my_range(n):
#     count = 0
#     while count < n:
#         count += 1
#         yield count
#
#
# def main():
#
#     for i in my_range(7):
#         print(i)
#
#
# main()


#
# def mul(num, n):
#     count = 0
#     while count < n:
#         count += 1
#         yield count * num
#
#
# def main():
#     M = mul(5, 7)
#     print(M)
#
#     print(next(M))
#     print(next(M))
#     print(next(M))
#     print(next(M))
#     print(next(M))
#     print(next(M))
#     print(next(M))
#     print(next(M))
#
#
# if __name__ == '__main__':
#     main()


# def multiple(num, n):
#     count = 0
#     while count < n:
#         count += 1
#         yield count * num
#
#
# def main():
#     mul = multiple(10, 15)
#
#     print(mul)
#
#     # print(next(mul))
#
#     for i in mul:
#         print(i)
#
#
# main()


# class Fibbo:
#
#     def __init__(self, n):
#         self.n = n
#         self.fib1 = 1
#         self.fib2 = 1
#
#     def __iter__(self):
#         self.count = 1
#         return self
#
#     def __next__(self):
#         if self.count <= 2:
#             self.count += 1
#             return 1
#         elif self.count <= self.n:
#             self.count = self.count + 1
#             res = self.fib1 + self.fib2
#             self.fib1, self.fib2 = self.fib2, res
#             return res
#         else:
#             raise StopIteration
#
#
# def main():
#     f = Fibbo(80)
#
#     itr = iter(f)
#
#     # print(next(itr))
#
#     for i in itr:
#         print(i, end=' ')
#
#
# main()


# lst = [10, 20, 30, 40, 50]
#
# res = [i * i for i in lst]
#
# print(res)


# lst = [10, 20, 30, 40, 50]
#
# res = [i * i for i in lst]
#
# res = (i * i for i in lst)
#
# # print((res))
# #
# # print(next(res))
# # print(next(res))
#
# for i in res:
#     print(i)


