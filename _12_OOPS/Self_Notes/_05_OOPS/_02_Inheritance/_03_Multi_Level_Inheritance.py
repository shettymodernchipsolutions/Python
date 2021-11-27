"""
Multilevel inheritance
---------------------------

In multilevel inheritance, features of the base class and the derived
class are inherited into the new derived class. That is we can
also inherit from a derived class.

"""


class Alpha:

    def fun1(self):
        print('Inside Alpha fun1()')


class Beta(Alpha):

    def fun2(self):
        print('Inside Beta fun2()')


class Gamma(Beta):
    pass


g = Gamma()
g.fun1()
g.fun2()
print(dir(Gamma))