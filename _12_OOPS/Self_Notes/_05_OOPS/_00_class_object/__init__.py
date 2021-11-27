# How to create the instance variables in a class.

# class Car:
#
#     def __init__(self):
#         self.brand = 'BMW'
#         self.cc = 2100
#         self.color = 'blue'
#
#
# def main():
#     c1 = Car()
#
#     print('Brand: ', c1.brand)
#     print('CC: ', c1.cc)
#     print('Color: ', c1.color)
#
#
# if __name__ == '__main__':
#     main()

# How to create a instance method in a class.

# class Car:
#
#     def __init__(self):
#         self.brand = 'BMW'
#         self.cc = 2100
#         self.color = 'blue'
#
#     def start_engine(self):
#         print(self.brand, 'Engine is starting...')
#
#     def shift_gear(self):
#         print(self.brand, 'shifting gear')
#
#     def accelerate(self):
#         print(self.brand, 'car is accelerating')
#
#
# def main():
#     c1 = Car()
#
#     print('Brand: ', c1.brand)
#     print('CC: ', c1.cc)
#     print('Color: ', c1.color)
#
#     c1.start_engine()   # c1.start_engine(c1)
#
#     c1.shift_gear()
#     c1.accelerate()
#
#
# if __name__ == '__main__':
#     main()

# Creating multiple objects in a class
# class Car:
#
#     def __init__(self):
#         self.brand = 'BMW'
#         self.cc = 2100
#         self.color = 'blue'
#
#     def start_engine(self):
#         print(self.brand, 'Engine is starting...')
#
#     def shift_gear(self):
#         print(self.brand, 'shifting gear')
#
#     def accelerate(self):
#         print(self.brand, 'car is accelerating')
#
#
# def main():
#     c1 = Car()
#
#     print('Brand: ', c1.brand)
#     print('CC: ', c1.cc)
#     print('Color: ', c1.color)
#
#     c1.start_engine()  # c1.start_engine(c1)
#     c1.shift_gear()
#     c1.accelerate()
#
#     c2 = Car()
#
#     print('Brand: ', c2.brand)
#     print('CC: ', c2.cc)
#     print('Color: ', c2.color)
#
#     c1.start_engine()  # c1.start_engine(c1)
#     c1.shift_gear()
#     c1.accelerate()
#
#
# if __name__ == '__main__':
#     main()

#
# class Footballer:
#     # State
#     def __init__(self, name, team, goals):
#         self.name = name
#         self.team = team
#         self.goals = goals
#
#     # Behaviour
#     def shooting(self):
#         print(self.name, 'is shooting')
#
#     def passing(self):
#         print(self.name, 'is passing')
#
#     def running(self):
#         print(self.name, 'is running')
#
#
# def main():
#     cr = Footballer('Ronaldo', 'Juventus',
#                     746)  # The moment there is an assignment a memory is created in stack for main()
#     print(cr.name)
#     print(cr.team)
#     print(cr.goals)
#     cr.shooting()
#     cr.passing()
#     cr.running()
#
#     ms = Footballer('Messi', 'Barcelona', 700)
#     print(ms.name)
#     print(ms.team)
#     print(ms.goals)
#     ms.shooting()
#     ms.passing()
#     ms.running()
#
#
# if __name__ == '__main__':
#     main()  # Calls the main method

# Creating a single instance method to send more than one arguement
# class Footballer:
#     # State
#     def __init__(self, name, team, goals):
#         self.name = name
#         self.team = team
#         self.goals = goals
#
#     # Behaviour
#     def shooting(self):
#         print(self.name, 'is shooting')
#
#     def passing(self):
#         print(self.name, 'is passing')
#
#     def running(self):
#         print(self.name, 'is running')
#
#     def display(self):
#         print(self.name)
#         print(self.team)
#         print(self.goals)
#
# def main():
#     cr = Footballer('Ronaldo', 'Juventus',
#                     746)  # The moment there is an assignment a memory is created in stack for main()
#     cr.display()
#     cr.shooting()
#     cr.passing()
#     cr.running()
#
#     ms = Footballer('Messi', 'Barcelona', 700)
#     ms.display()
#     ms.shooting()
#     ms.passing()
#     ms.running()
#
#
# if __name__ == '__main__':
#     main()  # Calls the main method

# Creating the instance variables post object creation
# class Footballer:
#     # State
#     def __init__(self, name, team, goals):
#         self.name = name
#         self.team = team
#         self.goals = goals
#
#     # Behaviour
#     def shooting(self):
#         print(self.name, 'is shooting')
#
#     def passing(self):
#         print(self.name, 'is passing')
#
#     def running(self):
#         print(self.name, 'is running')
#
#     def display(self):
#         print('Name: ', self.name)
#         print('Team: ', self.team)
#         print('Goals: ', self.goals)
#         print('Age: ', self.age)
#         print('Jersey No.: ', self.jersey_no)
#
# def main():
#     cr = Footballer('Ronaldo', 'Juventus',
#                     746)  # The moment there is an assignment a memory is created in stack for main()
#     cr.age = 35
#     cr.jersey_no = 7
#     cr.display()
#     cr.shooting()
#     cr.passing()
#     cr.running()
#
#
# if __name__ == '__main__':
#     main()  # Calls the main method

# Another way of creating the instance variables after object creation.
# class Footballer:
#     # State
#     def __init__(self, name, team, goals):
#         self.name = name
#         self.team = team
#         self.goals = goals
#
#     # Behaviour
#     def shooting(self):
#         print(self.name, 'is shooting')
#
#     def passing(self):
#         print(self.name, 'is passing')
#
#     def running(self):
#         print(self.name, 'is running')
#
#     def display(self):
#         print('Name: ', self.name)
#         print('Team: ', self.team)
#         print('Goals: ', self.goals)
#         print('Age: ', self.age)
#         print('Jersey No.: ', self.jersey_no)
#
# def main():
#     cr = Footballer('Ronaldo', 'Juventus',
#                     746)  # The moment there is an assignment a memory is created in stack for main()
#
#     setattr(cr, 'age', 35)      # Set Attribute
#     setattr(cr, 'jersey_no', 7) # Set Attribute
#
#     print(getattr(cr, 'name'))  # Get Attribute
#     print(getattr(cr,'team'))   # Get Attribute
#
#     print(hasattr(cr, 'name'))  # Has Attribute
#     print(hasattr(cr, 'team'))  # Has Attribute
#     print(hasattr(cr, 'gender'))    # Has Attribute
#
#     cr.display()
#     cr.shooting()
#     cr.passing()
#     cr.running()
#
#
# if __name__ == '__main__':
#     main()  # Calls the main method


class Footballer:
    # State
    def __init__(self, name, team, goals):
        self.name = name
        self.team = team
        self.goals = goals

    # Behaviour
    def shooting(self):
        print(self.name, 'is shooting')

    def passing(self):
        print(self.name, 'is passing')

    def running(self):
        print(self.name, 'is running')

    def display(self):
        print('Name: ', self.name)
        print('Team: ', self.team)
        print('Goals: ', self.goals)
        print('Age: ', self.age)
        print('Jersey No.: ', self.jersey_no)

def main():
    cr = Footballer('Ronaldo', 'Juventus',
                    746)  # The moment there is an assignment a memory is created in stack for main()

    setattr(cr, 'age', 35)      # Set Attribute
    setattr(cr, 'jersey_no', 7) # Set Attribute

    print(cr.__dict__)   #
    print(cr.display())
    print(cr.__dict__['name'])

    cr.shooting()
    cr.passing()
    cr.running()


if __name__ == '__main__':
    main()  # Calls the main method
