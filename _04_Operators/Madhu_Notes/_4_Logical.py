# Boolean   True 1   False 0
print(10+20)
print(10 != 'Madhu')

x = True
print("Value of x: ", x)
x = False
print("Value of x: ", x)

# Logical gate ===> and or not

# OR operator:
# Guest   Coffee or Tea
print("OR 1 :", True or False)
print("OR 2 :", True or True)
print("OR 3 :", False or True)
print("OR 4 :", False or False)

print("-----------------------")
# Guest Water and Coffee
print("AND 1 :", True and False)  # False
print("AND 2 :", True and True)   # True
print("AND 3 :", False and True)  # False  # False* and True
print("AND 4 :", False and False)  # False # False and False

# C1 or C2 or C3 or C4
# C1 and C2 and C3 and C4
# C1 and C2 or C3 and C4 or C5 or C6


# not
not True  # False
not False  # True

'''
condition1   AND/OR    condition2   AND/OR  condition3

condition
not condition

'''
print("Cond 1:", 10 > 20 and 5 < 2)  # False and False ==> False
print("Cond 2:", 10 < 20 and 5 > 2)  # True and True  ==> True
print("Cond 3:", not 5>2)
