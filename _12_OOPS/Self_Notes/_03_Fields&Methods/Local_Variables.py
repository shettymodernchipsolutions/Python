# Program without using Local Variable

class Citizen:
    # State
    def __init__(self, name, age, gender, state, nationality):
        self.name = name
        self.age = age
        self.gender = gender
        self.state = state
        self.nationality = nationality

    # Behaviour
    def display(self):
        print('Name: ', self.name)
        print('Age: ', self.age)
        print('Gender: ', self.gender)
        print('State: ', self.state)
        print('Nationality: ', self.nationality)


def main():
    rohith = Citizen('Rohith', 28, 'M', 'Karnataka', 'Indian')
    swathi = Citizen('Swathi', 25, 'F', 'Maharashtra', 'Indian')
    rita = Citizen('Rita', 24, 'F', 'Kerala', 'Indian')

    rohith.display()
    swathi.display()
    rita.display()


if __name__ == '__main__':
    main()

# Program after using Local Variable

# class Citizen:
#
#     nationality = 'Indian'
#     def __init__(self, name, age, gender, state):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.state = state
#
#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.gender)
#         print(self.state)
#         print(self.nationality)
#
#
# def main():
#     rohith = Citizen('Rohith', 28, 'M', 'Karnataka')
#     swathi = Citizen('Swathi', 25, 'F', 'Maharashtra')
#     rita = Citizen('Rita', 26, 'F', 'Kerala')
#
#     rohith.display()
#     swathi.display()
#     rita.display()
#
#
# if __name__ == '__main__':
#     main()

# Getting the output using dunder dict
# class Citizen:
#     nationality = 'Indian'
#
#     def __init__(self, name, age, gender, state):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.state = state
#
#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.gender)
#         print(self.state)
#         print(self.nationality)
#
#
# def main():
#     rohith = Citizen('Rohith', 28, 'M', 'Karnataka')
#     swathi = Citizen('Swathi', 25, 'F', 'Maharashtra')
#     rita = Citizen('Rita', 26, 'F', 'Kerala')
#
#     print(rohith.__dict__)
#     print(swathi.__dict__)
#     print(rita.__dict__)
#     print(Citizen.__dict__)
#
#
# if __name__ == '__main__':
#     main()

# Accesing static variable using class name
# class Citizen:
#     def __init__(self, name, age, gender, state):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.state = state
#
#     nationality = 'Indian'
#
#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.gender)
#         print(self.state)
#
#
# def main():
#     Citizen('Rohith', 28, 'M', 'Karnataka')
#     Citizen('Swathi', 25, 'F', 'Maharashtra')
#     Citizen('Rita', 26, 'F', 'Kerala')
#
#     print(Citizen.__dict__['nationality'])
#     print(Citizen.nationality)
#
#
# if __name__ == '__main__':
#     main()

# class Demo:
#     a = 10
#     b = 20
#
#
# def main():
#     print(Demo.a)  # 10
#     print(Demo.b)  # 20
#     Demo.a = 100
#     Demo.b = 200
#     print(Demo.a)  # 100
#     print(Demo.b)  # 200
#
#     d = Demo()
#     print(d.a)  # 100
#     print(d.b)  # 200
#
#     d.a = 1000
#     d.b = 2000
#     print(d.a)  # 1000
#     print(d.b)  # 2000
#     print(Demo.a)  # 100
#     print(Demo.b)  # 200
#
#
# if __name__ == '__main__':
#     main()

"""
Decorators
"""


# def fun1():
#     print('Inside fun1')
#
#
# fun1()
# print(fun1)
# fun2 = fun1
# fun2()
# print(fun2)

# Program to pass the function as input to another function
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
