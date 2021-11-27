"""
Single Inheritance
-------------------------

Single inheritance enables a derived class to inherit properties from
a single parent class, thus enabling code reusability.

"""


class Alpha:

    def fun(self):
        print('Alpha class fun()')


class Beta(Alpha):
    pass


b = Beta()
b.fun()


"""
Interesting fact: If a class is not inherited from another class explicitly then automatically the class is inherited 
by Object class.

Let us understand with an example
"""


class Alpha:

    def fun(self):
        print('Alpha was fun()')


print(dir(Alpha))