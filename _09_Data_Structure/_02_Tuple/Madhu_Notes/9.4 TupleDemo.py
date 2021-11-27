'''
Python Tuple count()    returns occurrences of element in a tuple
Python Tuple index()    returns smallest index of element in tuple
Python any()    Checks if any Element of an Iterable is True
Python all()    returns true when all elements in iterable is true
Python ascii()    Returns String Containing Printable Representation
Python bool()    Coverts a Value to Boolean
Python enumerate()    Returns an Enumerate Object
Python filter()    constructs iterator from elements which are true
Python iter()    returns iterator for an object
Python len()    Returns Length of an Object
Python max()    returns largest element
Python min()    returns smallest element
Python map()    Applies Function and Returns a List
Python reversed()    returns reversed iterator of a sequence
Python slice()    creates a slice object specified by range()
Python sorted()    returns sorted list from a given iterable
Python sum()    Add items of an Iterable
Python tuple() Function    Creates a Tuple
Python zip()    Returns an Iterator of Tuples
'''
# CRUD OPERATIONS
#1 CREATE
from filecmp import cmp
tup0 = ()
print("---Empty tuple 1---",tup0)
tuple0_1 = tuple()
print("---Empty tuple 2---",tuple0_1)

tup1 = (50,);
print("---Tuple 1 ----",tup1)

tup2 = (12, 34.56);
print("---Tuple 2 ----",tup2)

tup2_1 = tuple([1,2,"Madhu",True])
print("---Tuple 2_1 ----",tup2_1)

tup2_2 = tuple("Python Programming")
print("---Tuple 2_2 ----",tup2_2)

# 2 RETRIEVE
print("---Tuple 2_2 ----",tup2_2)

# 3 UPDATE
tup3 = ('abc', 'xyz');
print("---Tuple 3 ----",tup3, " ----id---- ",id(tup3))
#tup3[3] = 'pqr'
tup3 = tup3 + ('pqr',)
print("---Tuple 3 ----",tup3, " ----id---- ",id(tup3))

# 4 DELETE
tup4 = ('physics', 'chemistry', 1997, 2000);
print("-----tuple4-----------",tup4);
del tup4;
print("After deleting tup : ", tup4);

# BUILT IN TUPLE FUNCTIONS
'''
cmp(tuple1, tuple2)    Compares elements of both tuples.

len(tuple)                   Gives the total length of the tuple.

max(tuple)                 Returns item from the tuple with max value.

min(tuple)                  Returns item from the tuple with min value.

tuple(seq)                  Converts a list into tuple.

'''