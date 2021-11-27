'''
items() method
------------------
The items() method returns a view object. The view object contains the key-value pairs of the dictionary,
as tuples in a list.

The view object will reflect any changes done to the dictionary, see example below.

Syntax:
dictionary.items()
'''
print("--------- items() -----------")
d = {1:'C', 2:'Java', 3:'Python'}
print("The items of dictionary d: ",d.items())
print("To access the elements: ",list(d.items()))
for i in d.items():
    print("Dictionary items will be in the form of tuple: ", i)
for i,j in d.items():
    print("Unpacking tuples: ", i,j)
for i in d:
    print("The key values are: ", i)
