'''
Abstraction
--------------
Abstraction is used to hide the internal functionality of the function from the users. The users only interact with the
basic implementation of the function, but inner working is hidden. User is familiar with that "what function does" but
they don't know "how it does."
'''


'''
if we remove methods from parent class, we can change the names of
methods in derived classes. Let us see if we can get the same output'''


class VoiceAssistant:
    pass


class Siri(VoiceAssistant):
    def activate_assistant(self):
        print('Hey Siri, Activates Siri')

    def perform_task(self):
        print('Siri is performing the task using apple servers')

    def use_builtin_apps(self):
        print('Siri uses the builtin_apps of ios')


class Alexa(VoiceAssistant):
    def activate_assistant(self):
        print('Hey Alexa, Activates Alexa')

    def perform_task(self):
        print('Alexa is performing the task using amazon servers')

    def use_builtin_apps(self):
        print('Alexa uses the builtin_apps of fire-os')


class GoogleAssistant(VoiceAssistant):
    def activate_assistant(self):
        print('Ok Google, Activates GA')

    def perform_task(self):
        print('GA is performing the task using google servers')

    def use_builtin_apps(self):
        print('Google uses the builtin_apps of an-os')


def use_assistant(ref):
    ref.activate_assistant()
    ref.perform_task()
    ref.use_builtin_apps()


def main():
    s = Siri()
    a = Alexa()
    ga = GoogleAssistant()

    use_assistant(s)
    use_assistant(a)
    use_assistant(ga)


if __name__ == '__main__':
    main()


'''Rules of abstract method

Rule 1: An abstract class can contain combination of both abstract as well as concrete method.
'''

from abc import ABC, abstractmethod


class VoiceAssistant(ABC):

    @abstractmethod
    def activate_assistant(self):
        pass

    @abstractmethod
    def perform_task(self):
        pass

    @abstractmethod
    def use_builin_apps(self):
        pass

    def fun(self):
        print('inside fun()')


'''
Rule 2: You cannot be creating an object of a class which contains an abstract method.
'''
from abc import ABC, abstractmethod


class VoiceAssistant(ABC):

    @abstractmethod
    def activate_assistant(self):
        pass

    @abstractmethod
    def perform_task(self):
        pass

    @abstractmethod
    def use_builin_apps(self):
        pass

    def fun(self):
        print('inside fun()')


va = VoiceAssistant()
va.activate_assistant()

"""
Rule 3: A child class, if inherited from a parent class that it abstracts, it can only create an object of itself if in
case it overrides all the abstract method inherited from the parent class.
"""
from abc import ABC, abstractmethod


class VoiceAssistant(ABC):

    @abstractmethod
    def activate_assistant(self):
        pass

    @abstractmethod
    def perform_task(self):
        pass

    @abstractmethod
    def use_builin_apps(self):
        pass

    def fun(self):
        print('inside fun()')


class Siri(VoiceAssistant):
    def activate_assistant(self):
        print('Hey Siri')

    def perform_task(self):
        print('Perform task')

    def use_builin_apps(self):
        print('Using Builtin_apps')


S = Siri()

S.activate_assistant()
S.perform_task()
S.use_builin_apps()
S.fun()

'''
Let us take an example of shapes and try to understand when a method must be abstract, incomplete or a concrete method

Program to calculate the area of different shape using abstract method.
'''

from math import pi
from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self):
        self.area = 0

    @abstractmethod
    def take_input(self):
        pass

    @abstractmethod
    def find_area(self):
        pass

    @abstractmethod
    def disp_area(self):
        pass


class Circle(Shape):

    def __init__(self):
        self.r = 0
        super().__init__()

    def take_input(self):
        self.r = int(input('Enter the radius:\n'))

    def find_area(self):
        self.area = pi * self.r ** 2

    def disp_area(self):
        print(f'circle area = {self.area}')


class Rectangle(Shape):

    def __init__(self):
        self.l = 0
        self.b = 0
        super().__init__()

    def take_input(self):
        self.l = int(input('Enter the length:\n'))
        self.b = int(input('Enter the breadth:\n'))

    def find_area(self):
        self.area = self.l * self.b

    def disp_area(self):
        print(f'Rectangle area = {self.area}')


class Triangle(Shape):

    def __init__(self):
        self.h = 0
        self.b = 0
        super().__init__()

    def take_input(self):
        self.h = int(input('Enter the length:\n'))
        self.b = int(input('Enter the breadth:\n'))

    def find_area(self):
        self.area = (self.h * self.b) / 2

    def disp_area(self):
        print(f'Triangle area = {self.area}')


def geometric_shape(ref):
    ref.take_input()
    ref.find_area()
    ref.disp_area()


def main():
    c = Circle()
    r = Rectangle()
    t = Triangle()

    geometric_shape(c)
    geometric_shape(r)
    geometric_shape(t)


main()


