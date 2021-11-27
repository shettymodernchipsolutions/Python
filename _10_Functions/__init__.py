'''
Functions
--------------------------
A function is a set of statements that takes inputs, performs some specific tasks and produces output.

How do I declare a function in python?
The four steps in defining a function in python are as follows:
* Use the keyword "def" to declare the function and follow this up the "function_name".
* Add "parameters" to the function: they should be within the parentheses of the function. End your line with a "colon".
* Add "statements" that the functions should execute.
* End your function with a "return statement" if the function should output something.

Types of Functions:
-----------------------
Python con sists of four type of functions:
1. User-defined Functions.
2. Built-in Functions.
3. Lambda Funtions.
4. Recursive Functions.

User Defined Functions: These functions are defined or created by user.
Built-in  Functions: These functions are already defined in Python libraries and we can call them directly.
Lambda Functions: A lambda functions can take any number of arguments, but can only have one expression.
Recursive Functions: A python functioin which is defined to call itself during execution is known as
python recursive function.

'''

# def scr():
#     print("'C' is number one programming language in the world")
#     print("'Java' is the second most popular language in the world")
#     print("'Python' is the third most popular language in the world ")
#
# scr()
# print("This is outside the function")
# scr()
# scr()
# scr()

def num(x):
    return 2 * x

a = num(4)
print("The multiplied value of 'a' is: ", a)

b = num(6)
print("The multiplied value of 'b' is: ", b)

c = num(8)
print("The multiplied value of 'c' is : ",c)

def add(x, y):
    return x + y

d = add(12,42)
print("The addition of two value: ", d)
