# import math
#
# x =  5
# print("The factorial of 5 is : ", end="")
# print(math.factorial(x))

def fact(n):
    prod = 1
    while n >= 1:
        prod *= n
        n -= 1
    return prod

fact_of = fact(5)
print("The factorial of given number is : ", fact_of)