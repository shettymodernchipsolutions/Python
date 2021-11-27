'''
keys() method
------------------
The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.

The view object will reflect any changes done to the dictionary.

Syntax:
dictionary.keys()
'''
print("-------- keys() ----------")
d = {1:'C', 2:'Java', 3:'Python'}
print("The keys of dictionary d: ",d.keys())
print("To access the elements: ",list(d.keys()))
for i in d.keys():
    print("The keys of the dictionary are: ", i)
for i in d.keys():
     print("Accessing the keys with the values: ", i,d[i])