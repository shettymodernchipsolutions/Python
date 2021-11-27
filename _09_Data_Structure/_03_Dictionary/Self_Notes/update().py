'''
Dictionary
----------
A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written
with curly brackets, and they have keys and values. Each key will be mapped to a value.

Dictionaries are mutable – which means we can add and remove keys. A key can be removed by using pop( ).
Many other operations can be done as well, which we shall learn in future sessions

The update() method inserts the specified items to the dictionary.

The specified items can be a dictionary, or an iterable object with key value pairs.

Syntax:
dictionary.update(iterable)
'''

d = {'TWO':45, 1:92, 16:64, 22:56, 18:72, 26:88}
#print(d[2])
print(26 in d)
print(d['TWO'])

D = {1:'C', 2:'JAVA', 3:'PYTHON'}
print("_01_List of Elements:", D)
D[4] = 'C++' #Adding single element.
print("After adding single element:", D)
D.update({5:'C#', 6:'Visual Basics'}) #Adding multiple elements.
print("After using update function", D)
D.update(seven='Javascript', eight='PHP') #Adding multiple elements.
print(D)
D[2] = 'PYTHON' #Creating duplicate elements.
print("Using duplicate function", D)



d = {1:'a', 2:[10, 20, 30]}
print("The first element of dictionary: ",d[1])
x = d[1]
print("After assigning value to x: ", x)
x = 'b'
print("To check whether the first element is changed or not: ",d[1])
print("The variable element changes after assigning new element: ",x)
print("_01_List element in dictionary: ", d[2])
lst = d[2]
print("After assigning to variable: ", lst)
lst.append(99)
print("New list element is added after assigning element to lst variable: ",d[2])
print("After using append function in variable: ", lst)


