"""
Data Mangling
-------------------------------

In data mangling process any identifier with two leading underscore and one trailing underscore is textually replaced
with _classname__identifier where classname is the name of the current class. It means that any identifier of the form
__geek (at least two leading underscores or at most one trailing underscore) is replaced with _classname__geek, where
classname is the current class name with leading underscore(s) stripped.

"""


class Account_Holder:

    def __init__(self):
        self.__bal = 10000

    def get_bal(self):
        return self.__bal

    def set_bal(self, amount):
        if amount > 0:
            self.__bal = amount
        else:
            print('Invalid Amount')


ah = Account_Holder()
ah.__bal = 20000
print('Balance: ', ah.__dict__)
"""
We see that new variable is created with name __bal. This is because mangling is a process which is only applied 
to instance variables which are created within the class.
"""

