# str1 = "abc"
# str2 = "defg"
# str3 = str1 + str2
# print("First String: ", str1)
# print("Second String: ", str2)
# print("Output: ", str3)
#
# # str1 = "z34ggk"
#  # print all the repeated characters and count occurences of that character
# string = input("Enter a string: ")
# lst1 = []
# for i in string:
#         if i not in lst1:
#             lst1.append(i)
# for item in lst1:
#     print("The occurences of all the character: ", item,string.count(item), sep = ":")

# input: A list contains group of strings. Convert each word to capital letter and print

# lst = ['c', 'java', 'python']
# caps = [i.upper() for i in lst ]
# print("Before converting to uppercase: ", lst)
# print("Strings are converted to uppercase", caps)

# input: a python program to convert month name to a number of days

#
#  #input: Get the maximum and minimum value in a dictionary.
#
# dict = {"a": 100, "b": 200, "c": 300}
#
# values = dict.values()
# max_value = max(values)
# min_value = min(values)
#
#
# print("The maximum value : ", max_value)
# print("The minimum value : ", min_value)
#
#
#  #input: Find the highest 3 values in a dictionary.
# dict = {"A":3,"B":4,"H":1,"K":8,"T":0}
#
# values = sorted(dict, key = dict.get, reverse=True)[:3]
# for value in values:
#     print("The highest values in the dictionary are: ", dict[value])
# num=int(input("Enter a number: "))
# Behavior

# def check(num): #Function Definition
# # Function body
#  if num>0:
#   print(num,"is +ve number")
#  else:
#   print(num,"is -ve number")
#
# check(num)


# def multiplication(n):
#  i = 1
#  while i<11:
#   res = i * n
#   i += 1
#   print(res)
#
# n = int(input("Enter the value: "))
# multiplication(n)
#
# def multi(n): #Function Definition
#  print("Table of ", n ,"is")
#  i=1
#  while i<11:
#   result=i*n
#   i += 1
#   print(result)
# #State
# num = int(input("Enter a no"))
# multi(num)     # calling function
#
# def multi(n): #Function Definition
#  print(n)
#  i=1
#  while i<11:
#   result=i*n
#   i += 1
#   print("Table of",n, "is =",result)
# #State
# num = int(input("Enter a no"))
# multi(num)

# def multiplication(n):  # Function Definition
#  i = 1
#
#  while i < 11:
#   res = i * n
#   i += 1
#   print(res)
# # State
# n = int(input("Enter a number: "))
# multiplication(n)

# def full_name(fn,ln): #Function Definition
#  full_name = fn +" "+ ln
#  print("Full Name:",full_name)
# #State
# fname= input("Enter first name: ")
# lname= input("Enter last name: ")
# full_name(fname,lname)

# def full_name(fname,lname):
#  full_name = fname+" "+lname
#  print("Full name :", full_name)
#
# fn = input("Enter the first name: ")
# ln = input("Enter the last name: ")
# full_name(fn,ln)

# def sum_even(lst):
#     sum = 0
#     for i in lst:
#         if i % 2 == 0:
#             sum += i
#     return sum
#
#
# def main():
#     lst = list(map(int, input().split()))
#     res = sum_even(lst)
#     print('Sum: ', res)
#
#
# if __name__ == '__main__':
#     main()


# import logging
#
#
# def sum_even(lst):
#     logging.info("sum_even() started execution")
#     sum = 0
#     for i in lst:
#         if i % 2 == 0:
#             sum += i
#     logging.info("sum_even() finished execution")
#     return sum
#
#
# def main():
#     logging.basicConfig(filename='log.txt', level=logging.INFO)
#     logging.info("main() started execution")
#     lst = list(map(int, input().split()))
#     logging.info("input taken from the user")
#     logging.info("calling sum_even()")
#     result = sum_even(lst)
#     print('Result: ', result)
#     logging.info("main() finished execution")
#
#
# main()


# import logging
#
# def add(x, y):
#     return x + y
#
#
# def sub(x, y):
#     return x - y
#
#
# def mul(x, y):
#     return x * y
#
#
# def div(x, y):
#     return x / y
#
#
# def main():
#     logging.basicConfig(filename='log.txt', level= logging.DEBUG)
#     a = int(input())
#     b = int(input())
#     logging.debug(f'a = {a}')
#     logging.debug(f'b = {b}')
#
#     res1 = add(a, b)
#     logging.debug(f'res1 = {res1}')
#     res2 = sub(a, b)
#     logging.debug(f'res2 = {res2}')
#     res3 = mul(a, b)
#     logging.debug(f'res3 = {res3}')
#     res4 = div(a, b)
#     logging.debug(f'res4 = {res4}')
#
#
# main()


# import logging
#
# logging.basicConfig(filename='log.txt', level=logging.WARNING, filemode='w')
#
#
# def validate(num):
#     if len(num) == 10:
#         print('Valid mobile number')
#     else:
#         logging.warning('Mobile number validation failed')
#         print('Invalid mobile number')
#
#
# def main():
#     num = (input('Enter the mobile number: '))
#     validate(num)
#
#
# main()


# import logging
#
# logging.basicConfig(filename='log.txt', level=logging.ERROR, filemode='w')
#
#
# def div():
#     try:
#         num = int(input('Enter the numerator: '))
#         den = int(input('Enter the denominator: '))
#         Div = num / den
#         print(Div)
#     except:
#         logging.error('Exception Occured', exc_info=True)
#
#
# def main():
#     div()
#
#
# if __name__ == '__main__':
#     main()


# def fun():
#     lst = [0, 20, 30, 40, 50]
#     d = {1: 'C', 2: 'Java', 3: 'Python', 4: 'C++'}
#
#     try:
#         r = int(input("Enter the rank of the language: "))
#         print(d[r])
#         num = int(input("Enter the index of numerator: "))
#         den = int(input("Enter the index of denominator: "))
#         print(lst[num] / lst[den])
#     except KeyError:
#         print('Key value does not exist')
#     except IndexError:
#         print('Index out of bound')
#     except ZeroDivisionError:
#         print('Division by zero')
#     except:
#         print('Hey, some issue occured')
#
#
# def main():
#     fun()
#
#
# main()

# import logging
#
# logging.basicConfig(filename='log.txt', level=logging.ERROR, filemode='w', format='%(levelname)s:%(name)s:%(
# asctime)s:\ %(filename)s:%(msg)s')
#
#
# def fun():
#     lst = [10, 20, 30, 40, 50]
#     d = {1: 'C', 2: 'Java', 3: 'Python', 4: 'C++'}
#
#     try:
#         r = int(input('Enter the rank of the language: '))
#         print(d[r])
#         num = int(input('Enter the index of the numerator: '))
#         den = int(input('Enter the index of the denominator: '))
#         print(lst[num] / lst[den])
#     except KeyError:
#         print('key value does not exist')
#     except IndexError:
#         print('Index out of bound')
#     except ZeroDivisionError:
#         print('Division by zero')
#     except ValueError:
#         print('Invalid value')
#     except:
#         print('Hey, some issues occured')
#         logging.error('Exception occured', exc_info=True)
#
#
# def main():
#     fun()
#
#
# main()


# import csv
#
# csv_data = []
#
# with open("phone_dataset.csv", 'r') as phone_data:
#     my_csv = csv.reader(phone_data, delimiter=',')
#     for i in my_csv:
#         csv_data.append(i)
#
# with open("query.txt", "r") as query_data:
#     input_data = query_data.read()
#     input_data = input_data.splitlines()
#
# inpt:
# for inpt in input_data:
#     count = 1
#     matches = False
#     print(f"matches for {inpt}")
# for csv_d in csv_data:
#     temp_csv = csv_d
#     csv_d = csv_d[0].split(',')
#     if csv_d[0].strip() == inpt or csv_d[1].strip() == inpt:
#         print(f"Result {count} : {temp_csv}")
#         count = count + 1
#         matches = True
#         if matches == False:
#             print("No Result Found")


# import threading
# import time
#
# l = threading.Lock()
#
#
# class Customer:
#     balance = 5000
#
#
# def withdrawal(s, amt):
#     l.acquire()
#     if Customer.balance >= amt:
#         for i in range(1):
#             print('withdrawing the amount through ', s)
#             time.sleep(0.4)
#         Customer.balance = Customer.balance - amt
#     else:
#         print('Insufficient balance')
#     l.release()
#
#
# def main():
#     Customer()
#
#     print('Balance = ', Customer.balance)
#
#     t1 = threading.Thread(target=withdrawal, args=('payTM', 4000))
#     t2 = threading.Thread(target=withdrawal, args=('PhonePe', 4000))
#     t3 = threading.Thread(target=withdrawal, args=('Google Pay', 4000))
#
#     t1.start()
#     t2.start()
#     t3.start()
#
#     t1.join()
#     t2.join()
#     t3.join()
#
#     print('Balance = ', Customer.balance)
#
#
# if __name__ == '__main__':
#     main()

# import threading
# import time
#
# class Customer:
#
#     balance = 5000
#
#     def withdrawal(self, source, amount):
#         l.acquire()
#         if Customer.balance >= amount
#             for i in range(3):
#                 print('withdrawing the amount through ', s)
#                 time.sleep(0.4)
#             Customer.balance = Customer.balance - amount
#         else:
#             print('Insufficient balance')
#         l.release()
#
#
# def main():
#     c = Customer()
#
#     t1 = threading.Thread(target=c.withdrawal, args=('PayTM', 4000))
#     t2 = threading.Thread(target=c.withdrawal, args=('PhonePe', 4000))
#
#
#
#
#
#


# import threading
# import time
#
# l = threading.Lock()
#
#
# class Customer:
#     balance = 5000
#
#
# def withdrawal(source, amount):
#     l.acquire()
#     if Customer.balance >= amount:
#         for i in range(1):
#             print('withdrawal through', source)
#             time.sleep(0.4)
#         Customer.balance = Customer.balance - amount
#     else:
#         print('Insufficient Balance')
#     l.release()
#
#
# def main():
#
#     Customer()
#
#     print('Balance: ', Customer.balance)
#
#     t1 = threading.Thread(target=withdrawal, args=('PayTM', 4000))
#     t2 = threading.Thread(target=withdrawal, args=('Phonepe', 4000))
#     t3 = threading.Thread(target=withdrawal, args=('Google Pay', 4000))
#
#     t1.start()
#     t2.start()
#     t3.start()
#
#     t1.join()
#     t2.join()
#     t3.join()
#
#     print('Balance: ', Customer.balance)
#
#
# main()


# import threading
# import time
#
#
# l = threading.Lock()
#
#
# class Customer:
#     balance = 5000
#
#
# def withdrawal(source, amount):
#     l.acquire()
#     if Customer.balance >= amount:
#         for i in range(3):
#             print('withdrawal through', source)
#             time.sleep(0.4)
#         Customer.balance = Customer.balance - amount
#     else:
#         print('Insufficient balance')
#     l.release()
#
#
# def main():
#     Customer()
#
#     print('Balance: ', Customer.balance)
#
#     t1 = threading.Thread(target=withdrawal, args=('PayTM', 4000))
#     t2 = threading.Thread(target=withdrawal, args=('PhonePe', 4000))
#     t3 = threading.Thread(target=withdrawal, args=('Google Pay', 4000))
#
#     t1.start()
#     t2.start()
#     t3.start()
#
#     t1.join()
#     t2.join()
#     t3.join()
#
#     print('Balance: ', Customer.balance)
#
#
# main()


# import threading
# import time
#
# l = threading.Semaphore(2)
#
#
# class Customer:
#     balance = 15000
#
#
# def withdrawal(source, amount):
#     l.acquire()
#     if Customer.balance >= amount:
#         for i in range(2):
#             print('withdrawal through', source)
#             time.sleep(0.4)
#         Customer.balance = Customer.balance - amount
#     else:
#         print('Insufficient balance')
#     l.release()
#
#
# def main():
#     Customer()
#
#     print('Balance: ', Customer.balance)
#
#     t1 = threading.Thread(target=withdrawal, args=('PayTM', 4000))
#     t2 = threading.Thread(target=withdrawal, args=('PhonePe', 4000))
#     t3 = threading.Thread(target=withdrawal, args=('Google Pay', 4000))
#     t4 = threading.Thread(target=withdrawal, args=('Amazon Pay', 4000))
#
#     t1.start()
#     t2.start()
#     t3.start()
#     t4.start()
#
#     t1.join()
#     t2.join()
#     t3.join()
#     t4.join()
#
#     print('Balance: ', Customer.balance)
#
#
# main()


# import threading
# import time
#
# l = threading.Event()
#
#
# def producer():
#     print('Producer thread creating chocolate')
#     time.sleep(4)
#     print('Producer thread created chocolate')
#     l.set()
#
#
# def consumer():
#     print('Consumer thread waiting for producer')
#     l.wait()
#     print('Consumer thread consuming chocolate')
#
#
# def main():
#     t1 = threading.Thread(target=producer)
#     t2 = threading.Thread(target=consumer)
#
#     print('Producer started its job')
#     t1.start()
#     print('Consumer started its job')
#     t2.start()
#
#
# main()


# import threading
# import time
#
# l = threading.Event()
#
#
# def producer():
#     print('Producer thread creating chocolate')
#     time.sleep(4)
#     print('Producer thread created chocalate')
#     l.set()
#
#
# def consumer():
#     print('Consumer thread waiting for producer')
#     l.wait()
#     print('Consumer thread consuming chocolate')
#
#
# def main():
#     t1 = threading.Thread(target=producer)
#     t2 = threading.Thread(target=consumer)
#
#     print('Producer thread started its job')
#     t1.start()
#     print('Consumer thread started its job')
#     t2.start()
#
#
# main()


# import threading
# import time
#
# l = threading.Condition()
#
#
# def producer():
#     while True:
#         l.acquire()
#         print('Producer thread creating chocolate')
#         l.notify()
#         print('Producer thread created chocolate')
#         l.release()
#         time.sleep(1)
#
#
# def consumer():
#     while True:
#         l.acquire()
#         print('Consumer thread waiting for producer')
#         l.wait()
#         print('Consumer thread consuming chocolate')
#         l.release()
#         time.sleep(1)
#
#
# def main():
#     t1 = threading.Thread(target=producer)
#     t2 = threading.Thread(target=consumer)
#
#     print('Producer started its job')
#     t1.start()
#     print('Consumer started its job')
#     t2.start()
#
#
# main()

'''
File Handling
-----------------------------------------------
'''
# readline() method
# f = open(r"C:\Users\bhave\PycharmProjects\Python Core\0033_MCS_Bhavesh_CorePython\sample.txt", 'r')
#
# for i in range(7):
#     data = f.readline()
#     print(data)
#
# f.close()

# readlines() method
# Printing all the lines in the file.
# f = open(r"C:\Users\bhave\PycharmProjects\Python Core\0033_MCS_Bhavesh_CorePython\sample.txt", 'r')
#
# lst = f.readlines()
# for i in lst:
#     print(i)
#
# f.close()

# Printing only the speicified lines using readlines().
# f = open(r"C:\Users\bhave\PycharmProjects\Python Core\0033_MCS_Bhavesh_CorePython\sample.txt", 'r')
#
# lst = f.readlines()
# for i in range(5):
#     print(lst[i])
#
# f.close()

# Reading the line in the reverse order using readlines() method
# f = open(r"C:\Users\bhave\PycharmProjects\Python Core\0033_MCS_Bhavesh_CorePython\sample.txt", 'r')
#
# lst = f.readlines()
#
# for i in lst[::-1]:
#     print(i)
#
# f.close()

# Different properties in File handling
# with open(r"D:\Personal File\sample.txt", 'w') as f:
#     print(f.name)
#     print(f.mode)
#     print(f.closed)
#     print(f.readable())
#     print(f.writable())

# Transferring data in one txt file to another

# f1 = open(r"C:\Users\bhave\PycharmProjects\Python Core\0033_MCS_Bhavesh_CorePython\sample.txt", 'r')
# f2 = open(r"D:\Personal File\simple.txt", 'w')
#
# data = f1.read()
# f2.write(data)
#
# f1.close()
# f2.close()


# f1 = open('sample.txt', 'r')
# f2 = open('simple.txt', 'w')
#
# Data = f1.read()
# f2.write(Data)
#
# f1.close()
# f2.close()


# import json
# from urllib.request import urlopen
#
# url = 'https://www.gov.uk/bank-holidays.json'
#
# info = urlopen(url)
# data = json.loads(info.read())
#
# print(data)
#
# info.close()



import json
from urllib.request import urlopen

resp = "http://www.webcode.me"

print(resp.text)