"""

Multiple inheritance
----------------------------

A class can be derived from more than one base class in Python,
similar to C++. This is called multiple inheritance. In multiple
inheritance, the features of all the base classes are inherited into
the derived class

"""


class Alpha:

    def fun1(self):
        print('Alpha class fun1()')


class Beta():

    def fun1(self):
        print('Beta class fun1()')


class Gamma(Alpha, Beta):
    pass


g = Gamma()
g.fun1()

"""
We see that python doesn’t raise any issue instead it resolves it by 
following an algorithm called as method resolution order (MRO).
"""