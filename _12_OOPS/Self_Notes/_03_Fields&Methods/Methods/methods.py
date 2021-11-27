"""
There are three types of methods in python:
1. Instance Method
2. Static Method
3. Class Method
"""


# class BmwCar:
#
#     def __init__(self, name, cc, color):
#         self.name = name
#         self.cc = cc
#         self.color = color
#
#     def start_engine(self):
#         print(self.name, 'engine is starting')
#
#
# def main():
#     c = BmwCar('bmw', 2100, 'blue')
#     c.start_engine()
#     # BmwCar.start_engine(c)
#
#
# if __name__ == '__main__':
#     main()


# class BmwCar:
#
#     def __init__(self, name, cc, color):
#         self.name = name
#         self.cc = cc
#         self.color = color
#
#     def start_engine(self):
#         print(self.name, 'engine is starting')
#
#     def kms_to_miles(kms):
#         print(kms * 1.6)
#
#
# def main(): c = BmwCar('bmw', 2100, 'blue') c.start_engine() BmwCar.kms_to_miles(7924) c.kms_to_miles(7924)    #
# Error: BmwCar.kms_to_miles() takes 1 positional argument but 2 were given. BmwCar.kms_to_miles(c, 7924)
#
#
# if __name__ == '__main__':
#     main()

# We can execute the program in both instance method as well as by calling the class name using decorators
# class BmwCar:
#
#     def __init__(self, name, cc, color):
#         self.name = name
#         self.cc = cc
#         self.color = color
#
#     def start_engine(self):
#         print(self.name, 'engine is starting')
#
#     @staticmethod
#     def kms_to_miles(kms):
#         print(kms * 1.6)
#
#
# def main():
#     c = BmwCar('bmw', 2100, 'blue')
#     c.start_engine()
#     BmwCar.kms_to_miles(7924)
#     c.kms_to_miles(7924)
#
#
# if __name__ == '__main__':
#     main()


# class BmwCar:
#
#     def __init__(self, name, cc, color):
#         self.name = name
#         self.cc = cc
#         self.color = color
#
#     def x1(cls):
#         return cls('x1', 1998, 'blue')
#
#     def series5(cls):
#         return cls('5series', 2993, 'blue')
#
#     def i8(cls):
#         return cls('i8', 1499, 'blue')
#
#     def display(self):
#         print(self.name)
#         print(self.cc)
#         print(self.color)
#
# def main():
#     c1 = BmwCar.x1(BmwCar)
#     c2 = BmwCar.series5(BmwCar)
#     c3 = BmwCar.i8(BmwCar)
#
#     c1.display()
#     c2.display()
#     c3.display()
#
# if __name__ == '__main__':
#     main()


class BmwCar:

    def __init__(self, name, cc, color):
        self.name = name
        self.cc = cc
        self.color = color

    @classmethod
    def x1(cls):
        return cls('x1', 1998, 'blue')

    @classmethod
    def series5(cls):
        return cls('5series', 2993, 'blue')

    @classmethod
    def i8(cls):
        return cls('i8', 1499, 'blue')

    def display(self):
        print('Model: ', self.name)
        print('CC:', self.cc)
        print('Color: ', self.color)


def main():
    c1 = BmwCar.x1()
    c2 = BmwCar.series5()
    c3 = BmwCar.i8()

    c1.display()
    c2.display()
    c3.display()


if __name__ == '__main__':
    main()
