'''
pop() method
-----------------
The pop() method removes the specified item from the dictionary.

The value of the removed item is the return value of the pop() method.

Syntax:
dictionary.pop(keyname, defaultvalue)
'''
print("---------- pop() -----------")
d = {1:'p', 2:'y', 3:'t', 4:'h', 5:'o', 6:'n', 80:'a'}
z = d.pop(3)
print(z)
print(d.pop(3))
print(d.pop(78))
print("To avoid key error: ", d.pop(78,0))
print("To avoid key error: ", d.pop(78,'Not Found'))
d.clear()
print('To clear all the elements: ', d)
d.popitem()
print("After clearing all the item", d)
