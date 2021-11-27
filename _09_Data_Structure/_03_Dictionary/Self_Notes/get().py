'''
get() method
------------------
The get() method returns the value of the item with the specified key.

Syntax:
dictionary.get(keyname, value)
'''
print("---------- get() ----------")
d = {"Front-end": ["HTML5", "CSS", "JAVASCRIPT"],
     "Back-end": ["C","JAVA", "PYTHON"],
     "Database": ["SQL", "MONGODB", "ORACLE"]}

b = d.get("Front-end")
print(b)

