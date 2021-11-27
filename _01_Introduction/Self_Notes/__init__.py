'''
Python Introduction
----------------------

1) How interpreter works in python.

a) The python compiler reads a python source code or instruction. Then it verifies that the instruction is
well-formatted, i.e. it checks the syntax of each line. If it encounters an error, it immediately halts the
translation and shows an error message.

b) If there is no error, i.e. if the python instruction or source code is well-formatted then the compiler
translates it into its equivalent form in an intermediate language called “Byte code”.

c) Byte code is then sent to the Python Virtual Machine(PVM) which is the python interpreter. PVM converts
the python byte code into machine-executable code. If an error occurs during this interpretation then the conversion
is halted with an error message.

2) What are the features of Python?

Python Features:

1. Easy Language: Python is an easy language. It is easy to read, write, learn and understand.
Python has a smooth learning curve.

2. Readable: The Python language is designed to make developers life easy. Reading a Python code is like reading
an English sentence.

3. Interpreted Language: Python is an interpreted language. It comes with the IDLE
(Interactive Development Environment). This is an interpreter and follows the REPL structure
(Read-Evaluate-Print-Loop).

4. Dynamically-Typed Language: Python is not statically-typed like Java. You dont need to declare data type while
defining a variable.

5. Object-Oriented: Python is object-oriented but supports both functional and object-oriented programming.
Everything in Python is an object.

6. Popular and Large Community Support: Python has one of the largest communities on StackOverflow and Meetup.
If you need help, the community will answer your questions.

7. Open-Source: Python is open-source and the community is always contributing to it to improve it. It is free and
its source code is freely available to the public.

8. Large Standard Library: The standard library is large and has many packages and modules with common and important
functionality.

9. Platform-Independent: Python is platform-independent. If you write a program, it will run on different platforms
like Windows, Mac and Linux.

10. Extensible and Embeddable: Python is extensible. You can use code from other languages like C++ in your Python
code. It is also embeddable.

11. GUI Support: You can use Python to create GUI (Graphical User Interfaces). You can use tkinter, PyQt, wxPython
or Pyside for this.

12. High-level Language: Python is a high-level language and C++ is mid-level. Python is easy to understand and
closer to the user.

3) Interpreter CPython IronPython Jython

1.Cpython
CPython is the default and most widely used interpreter or implementation of Python, written in C. It is the original
Python version, which users download from its official website, Python.org. It can be better described as a
mixture of both an interpreter and compiler as it converts your written Python source code into bytecode.
By bytecode, we refer to a program code that gets compiled and processed into a low-level language that can be
used as instructions for the interpreter. It is this bytecode that gets executed on the CPython Virtual Machine.

2. IronPython
Similar to how Jython has been developed for Java users, IronPython is the popular Python implementation that has
been written in C-Sharp (C#) and has been designed to run on the .NET platform. It creates a bridge between the
Python and .NET universe and allows Python users to get access to C-sharp functions and classes, as well as .NET
libraries and frameworks directly from IronPython. IronPython excels for programs that make use of threading and
can be found on the ironpython.net website.

3. Jython
Jython is another Python implementation that has been written in the Java language whose implementation can run in
Java platforms. Similar to CPython, it first converts the source code into bytecode, which, as mentioned before,
are a set of instructions that are needed by an interpreter. In Jython, these are written in Java and can run on
the Java Virtual Machine, which is the same environment that Java itself uses. Jython allows users to easily work
with Java programs since you can call, as well as utilize, your Java functions and classes directly from Jython
without any additional effort which is immensely beneficial as Python users can get access into the enormous
ecosystem of libraries and frameworks that come along with Java.

4) Dynamically typed programming language

Python don't have any problem even if we don't declare the type of variable. It states the kind of variable
in the runtime of the program. Python also take cares of the memory management which is crucial in programming.
So, Python is a dynamically typed language.

5) Environment variables importance in python

Environment variables provide a great way to configure your Python application, eliminating the need to edit your
source code when the configuration changes. Common configuration items that are often passed to application through
environment variables are third-party API keys, network ports, database servers, and any custom options that your
application may need to work properly.

6) Different ways to run python program

Here are the ways with which we can run a Python programm:

1. Interactive Mode
2. Command Line
3. Text Editor (VS Code)
4. IDE (PyCharm)

Object-oriented

Python is a great programming language that supports OOP. You will use it to define a class with attributes and
methods, which you will then call. Python offers a number of benefits compared to other programming languages like
Java, C++ or R. It's a dynamic language, with high-level data types. This means that development happens much
faster than with Java or C++. It does not require the programmer to declare types of variables and arguments.
This also makes Python easier to understand and learn for beginners, its code being more readable and intuitive.

High-level programming language.

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.
Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very
attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing
components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of
program maintenance. Python supports modules and packages, which encourages program modularity and code reuse.
The Python interpreter and the extensive standard library are available in source or binary form without charge
for all major platforms, and can be freely distributed.

Automatic garbage collection.

Python has an automated garbage collection. It has an algorithm to deallocate objects which are no longer needed.
Python has two ways to delete the unused objects from the memory.

1. Reference counting:
The references are always counted and stored in memory.

2. Generational Garbage Collection:
Generational garbage collection is a type of trace-based garbage collection. It can break cyclic references and
delete the unused objects even if they are referred by themselves.
'''