"""
Method Resolution Order:
-------------------------------

MRO is the order in which python is going to trace the classes and based on that the function is called. But first we
should know about C3 linearization algorithm, which is used to generate the order to resolve the name clashes.

Linearization of a class with single parent is class followed by its object. But the linearization of class with
multiple parents is class plus the merge of its parents and the list of parents.

"""


'''
Different ways to access the MRO

1st way:
'''

#1st way


class Alpha:

    def fun1(self):
        print('Alpha class fun1()')


class Beta:

    def fun1(self):
        print('Beta class fun1()')


class Gamma(Alpha, Beta):
    pass


g = Gamma()
g.fun1()


help(Gamma)


#2nd way


class Alpha:

    def fun1(self):
        print('Alpha class fun1()')


class Beta:

    def fun1(self):
        print('Beta class fun1()')


class Gamma(Alpha, Beta):
    pass


g = Gamma()
g.fun1()


print(Gamma.__mro__)


# 3rd way


class Alpha:

    def fun1(self):
        print('Alpha class fun1()')


class Beta:

    def fun1(self):
        print('Beta class fun1()')


class Gamma(Alpha, Beta):
    pass


g = Gamma()
g.fun1()


print(Gamma.mro())