"""
Exception handling
------------------------------

In computing and computer programming, exception handling is the process of responding to the occurrence of
exceptions – anomalous or exceptional conditions requiring special processing - during the execution of a program.

To understand in a better way let us take non-technical example first

Consider the following sentence:
A apple a day keep a doctor away.

Clearly we can see some grammatical mistakes in the above sentence.The correct form of sentence is “An apple a day
keeps the doctor away”. This follows all the set of rules which English language follows. Similar to these grammatical
mistakes in programming language one can commit some syntactical or logical mistakes.

In python we have set of tokens (identifiers, operators, delimiters, keywords). All commands in python are combination
of these tokens.
"""

# Eg:-
a = 10 + 0
b = 10 - 0
c = 10 * 0
d = 10 / 0
print(a, b, c, d)

"""Above code is perfectly fine with the syntax. But logic is not correct. Hence we get a ZeroDivionError which is 
one of the exceptions.
"""

""" Errors --> Syntax Errors, Exceptions """

"""Syntax Errors:-
-  Syntax mistakes
-  Is easily identified by the interpreter
-  Occurs before runtime 

Exceptions:-
-  Logical mistakes
-  Is Not identified by the
interpreter
-  Occurs during runtime"""

