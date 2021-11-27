'''
values() method
----------------------
The values() method returns a view object. The view object contains the values of the dictionary, as a list.

The view object will reflect any changes done to the dictionary.

Syntax:
dictionary.values()
'''
print("------------ values() -------------")
d = {1:'C', 2:'Java', 3:'Python'}
print("The values of dictionary d: ",d.values())
print("To access the elements: ",list(d.values()))
for i in d.values():
    print("The values of the dictionary are: ", i)
