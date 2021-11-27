'''
popitem() method
--------------------
The popitem() method removes the item that was last inserted into the dictionary.

The removed item is the return value of the popitem() method, as a tuple.

Syntax:
dictionary.popitem()
'''
print("------------ popitem() --------------")
d = {1:'p', 2:'y', 3:'t', 4:'h', 5:'o', 6:'n', 80:'a'}
print("Dictionary elements are: ", d)
d.pop(3)
print("After popping: ", d)
d.popitem()
print("After using popitem: ", d)
del d[4]
print("After deletion: ", d)
