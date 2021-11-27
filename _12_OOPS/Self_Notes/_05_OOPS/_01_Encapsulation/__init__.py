"""
Encapsulation
-------------------------
To know what is encapsulation and is it needed. Let us consider an
example:-
"""

# class Account_Holder:
#
#     def __init__(self):
#         self.bal = 10000
#
# ah = Account_Holder()
# print('Balance: ', ah.bal)
# ah.bal = -20000
# print('Balance: ', ah.bal)

"""
But balance in ones’ account is personal and should not be easily
accessible by the third person. And more importantly we shouldn’t
be allowed to mishandle the data.
"""

# We can resolve this issue in the following code

# class Account_Holder:
#
#     def __init__(self):
#         self.bal = 10000
#
#     def get_bal(self):
#         return self.bal
#
#     def set_bal(self, amount):
#         if amount > 0:
#             self.bal = amount
#         else:
#             print('Invalid Amount')
#
# ah = Account_Holder()
# print('Balance: ', ah.get_bal())
# ah.set_bal(-20000)
# print('Balance: ', ah.get_bal())

"""

Encapsulation in Python is the process of wrapping up variables andmethods into a single entity. In programming, a 
class is an example that wraps all the variables and methods defined inside it. Encapsulation acts as a protective 
layer by ensuring that, access to wrapped data is not possible by any code defined outside the class in which the 
wrapped data are defined. Encapsulation provides security by hiding the data from the outside world.

"""

# In the above code we can still access amt by calling bal and can still modify. How can we modify it?


class Account_Holder:

    def __init__(self):
        self._bal = 10000

    def get_bal(self):
        return self._bal

    def set_bal(self, amount):
        if amount > 0:
            self._bal = amount
        else:
            print('Invalid Amount')


ah = Account_Holder()
print('Balance: ', ah.get_bal())
ah.set_bal(-20000)
print('Balance: ', ah.get_bal())

"""

Although the above declaration of variable is just indication of not using directly, which means any third member can 
still aces it directly who isn’t aware of it. Which says that python doesn’t strictly enforce anything it’s more of a 
responsibility of the user and developer.

"""

# Solution for this is


class Account_Holder:

    def __init__(self):
        self._bal = 10000

    def get_bal(self):
        return self._bal

    def set_bal(self, amount):
        if amount > 0:
            self._bal = amount
        else:
            print('Invalid Amount')


ah = Account_Holder()
print('Balance: ', ah.__dict__)  # the balance is stored in the form of dictionary, but still haven't resolved yet.


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
print('Balance: ', ah.__dict__)

"""
By adding 2 underscore in front of the variable made the difference. 
Python internally changed the __bal to _AccountHolder__bal using a 
concept called as data mangling
"""

# details of employee

# class Employee:
#
#     def __init__(self, emp_name, emp_id, emp_sal):
#         self.emp_name = emp_name
#         self.emp_id = emp_id
#         self.emp_sal = emp_sal
#
#     def bhavesh(self):
#         print("Enter the details of the employee: ", 'Name:',self.emp_name,'Employee-id:', self.emp_id,'Salary:', self.emp_sal)
#
# bvs = Employee('Bhavesh V Shetty', 'MCS-0033', 32333)
# bvs.bhavesh()

# Creating a Base class


# class Base:
#     def _init_(self):
#         self.a = "GeeksforGeeks"
#         self.__c = "GeeksforGeeks"
#
#
# # Creating a derived class
# class Derived(Base):
#     def _init_(self):
#         # Calling constructor of
#         # Base class
#         Base._init_(self)
#         print("Calling private member of base class: ")
#         print(self.__c)
#
#
# # Driver code
# obj1 = Base()
# print(obj1.a)