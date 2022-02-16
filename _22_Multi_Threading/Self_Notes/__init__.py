# A Python program to find the currently running thread in a Python program

import threading

print('Let us find the current thread')

print('Currently running thread: ', threading.current_thread().getName())

if threading.current_thread() == threading.main_thread():
    print('The current thread is the main thread')
else:
    print('The current thread is not main thread')

# A Python program to create a thread and use it to run a function.

from threading import *


def display():
    print('Hello I am running')


for i in range(5):
    t = Thread(target=display)

    t.start()

# A Python program to pass arguments to a function and execute it using a thread.

from threading import *


def display(str):
    print(str)


for i in range(5):
    t = Thread(target=display, args=('Hello',))
    t.start()

# A Python program to create a thread by making our class as sub class to Thread class

from threading import Thread


class MyThread(Thread):
    def run(self):
        for i in range(1, 6):
            print(i)


t1 = MyThread()

t1.start()

t1.join()

# A Python program to create a thread that accesses the instance variables of a class.

from threading import *


class MyThread(Thread):

    def __init__(self, str):
        Thread.__init__(self)
        self.str = str

    def run(self):
        print(self.str)


t1 = MyThread('Hello')

t1.start()

t1.join()

# A Python program to create a thread that acts on the object of a class that is not derived from a Thread class.

from threading import *


class MyThread:

    def __init__(self, str):
        self.str = str

    def display(self, x, y):
        print(self.str)
        print('The args are: ', x, y)


obj = MyThread('Hello')

t1 = Thread(target=obj.display, args=(1, 2))

t1.start()

# A Python program to show single tasking using a thread that prepares tea.

from threading import *
from time import *


class MyThread:
    def prepareTea(self):
        self.task1()
        self.task2()
        self.task3()

    def task1(self):
        print('Boil milk and tea powder for 5 minutes....', end='')
        sleep(5)
        print('Done')

    def task2(self):
        print('Add sugar and boil for 3 minutes....', end='')
        sleep(3)
        print('Done')

    def task3(self):
        print('Filter it and serve....', end='')
        print('Done')


obj = MyThread()

t = Thread(target=obj.prepareTea)
t.start()

# A Python program that performs two tasks using two threads simultaneously.

from threading import *
from time import *


class Theatre:

    def __init__(self, str):
        self.str = str

    def movieshow(self):
        for i in range(1, 6):
            print(self.str, " : ", i)
            sleep(0.1)


obj1 = Theatre('Cut ticket')
obj2 = Theatre('Show chair')

t1 = Thread(target=obj1.movieshow)
t2 = Thread(target=obj2.movieshow)

t1.start()
t2.start()

# A program where two threads are acting on the same method to allot a berth for the passenger.

from threading import *
from time import *


class Railway:

    def __init__(self, available):
        self.available = available

    def reserve(self, wanted):
        print('Available number of berths: ', self.available)

        if (self.available >= wanted):
            name = current_thread().getName()
            print('%d berths alloted for %s' % (wanted, name))
            sleep(1.5)
            self.available -= wanted
        else:
            print('Sorry, no berths to allot')


obj = Railway(1)

t1 = Thread(target=obj.reserve, args=(1,))
t2 = Thread(target=obj.reserve, args=(1,))

t1.setName('First Person')
t2.setName('Second Person')

t1.start()
t2.start()

# A Python program for achieving thread synchronization using locks.

from threading import *
from time import *


class Railway:

    def __init__(self, available):
        self.available = available
        self.l = Lock()

    def reserve(self, wanted):
        self.l.acquire()
        print('Available number of berths: ', self.available)

        if (self.available >= wanted):
            name = current_thread().getName()
            print('%d berths alloted for %s' % (wanted, name))
            sleep(1.5)
            self.available -= wanted
        else:
            print('Sorry, no berths to allot')
        self.l.release()


obj = Railway(1)

t1 = Thread(target=obj.reserve, args=(1,))
t2 = Thread(target=obj.reserve, args=(1,))

t1.setName('First Person')
t2.setName('Second Person')

t1.start()
t2.start()
