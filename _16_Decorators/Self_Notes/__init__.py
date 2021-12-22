"""
@classmethod
@staticmethod
Decorator : Provides additional functionality for class or method/function
"""

"""
Decorators in Python
Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of function
or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, 
without permanently modifying it.
First Class Objects
In Python, functions are first class objects that mean that functions in Python can be used or passed as arguments.
Properties of first class functions:
A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, …
Consider the below examples for better understanding.
Example 1: Treating the functions as objects.
"""


# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()


print(shout('Hello'))

yell = shout

print(yell('Hello'))
print("-------------------------------------------------------------")
"""
In the above example_1, we have assigned the function shout to a variable. This will not call the function instead it 
takes the function object referenced by a shout and creates a second name pointing to it, yell.
Example 2: Passing the function as an argument
"""


# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print(greeting)


greet(shout)
greet(whisper)
print("-------------------------------------------------------------")

"""
In the above example_1, the greet function takes another function as a parameter (shout and whisper in this case). The 
function passed as an argument is then called inside the function greet.
Example 3: Returning functions from another functions.
"""


# Python program to illustrate functions
# Functions can return another function
def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(add_15(10))
"""
In the above example_1, we have created a function inside of another function and then have returned the function created 
inside.
The above three examples depict the important concepts that are needed to understand decorators. 
"""

"""
Decorators
As stated above the decorators are used to modify the behaviour of function or class. In Decorators, functions are taken
as the argument into another function and then called inside the wrapper function.
Syntax for Decorator:
@mcs_decorator
def hello_decorator():
    print("MCS")
'''Above code is equivalent to -
def hello_decorator():
    print("MCS")
hello_decorator = mcs_decorator(hello_decorator)'''
In the above code, gfg_decorator is a callable function, will add some code on the top of some another callable
function, hello_decorator function and return the wrapper function.
Decorator can modify the behaviour:
"""


# defining a decorator
def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behavior
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()

print("---------------------------------------------------------------------------")

# importing libraries
import time
import math


# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1


# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num_1):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num_1))


# calling the function.
factorial(5)

print("--------------------------------------------------------------------")


def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")

        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value

    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a_1, b_1):
    print("Inside the function")
    return a_1 + b_1


a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))
print("-----------------------------------------------------------------------------------")

"""
In the above example_1, you may notice a keen difference in the parameters of the inner function. The inner function takes
the argument as *args and **kwargs which means that a tuple of positional arguments or a dictionary of keyword arguments
can be passed of any length. This makes it a general decorator that can decorate a function having any number of 
arguments.
Chaining Decorators
In simpler terms chaining decorators means decorating a function with multiple decorators.
Example:
"""


# code for testing decorator chaining
def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x

    return inner


@decor1
@decor
def num():
    return 10


print(num())

# The above example_1 is similar to calling the function as     --–>     decor1(decor(num))



def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("+" * 30)
        func(*args, **kwargs)
        print("=" * 30)

    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")

print("--------------------------------------------------------------------")


def printer(msg):
    print(msg)


printer = star(percent(printer))
printer('MCS')
print("--------------------------------------------------------------------")


@percent
@star
def printer(msg):
    print(msg)


printer('Python')

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)


divide(4, 2)
print()
divide(5, 0)


def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3):
            # This is the wrapper function
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2, decorator_arg3,
                          function_arg1, function_arg2, function_arg3))
            return func(function_arg1, function_arg2, function_arg3)

        return wrapper

    return decorator


pandas = "Pandas"


@decorator_maker_with_arguments(pandas, "Numpy", "Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2, function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
          " {1}" " {2}".format(function_arg1, function_arg2, function_arg3))


decorated_function_with_arguments(pandas, "Science", "Tools")