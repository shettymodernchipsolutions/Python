'''
Decorators
-----------------
'''


# def fun1():
#     print('Inside fun1()')
#
#
# fun1()
# print(fun1)


# def fun1():
#     print('Inside fun1()')
#
#
# fun1()
# print(fun1)
#
# fun2 = fun1
# fun2()
# print(fun2)

# def alpha(ref):
#     print('Inside alpha()')
#     ref()
#
#
# def beta():
#     print('Inside beta()')
#
#
# alpha(beta)

# def sum_lst(lst):
#     print(sum(lst))
#
#
# def product_lst(lst):
#     p = 1
#     for i in lst:
#         p *= i
#     print(p)
#
#
# def fun(choice):
#     if choice == 'sum':
#         return sum_lst
#     else:
#         return product_lst
#
#
# fun1 = fun('sum')
# fun1([10, 20, 30, 40])
# fun2 = fun('product')
# fun2([10, 20, 30, 40])

# def outer():
#     print('Inside outer()')
#
#     def inner():
#         print('Inside inner()')
#
#     inner()
#
#
# outer()


# def outer():
#     print('Inside outer()')
#
#     def inner():
#         print('Inside inner()')
#
#     return inner
#
#
# inner_ref = outer()

# def outer():
#     print('Inside outer()')
#
#     def inner():
#         print('Inside inner()')
#
#     return inner
#
#
# in_ref = outer()
# in_ref()


# def get_product(lst):
#     p = 1
#     for i in lst:
#         p *= i
#     print(p)
#
#
# get_product([10, 20, 30])

def get_product(lst):
    p = 1
    for i in lst:
        p *= i
    print(p)


get_product([10, 0, 30])