#loops in python:

'''Python programming language provides following types of loops to handle looping
requirements. Python provides three ways for executing the loops. While all the ways
provide similar basic functionality, they differ in their syntax and condition checking
time.'''


# While Loop:

'''1. In python, while loop is used to execute a block of statements repeatedly until a
given a condition is satisfied.
2.And when the condition becomes false, the line
immediately after the loop in program is executed.'''

 #while loop examples

'''count = 0 #state
while (count < 3): #condition
    count = count+1 #increment
    print (count)''' #business logic

#----------------------------------------------------------------------------------------------------------------------
'''count = 10;
while (count > 5):
    count = count-1
    print(count)'''

#--------------------------------------------------------------------------------------------------------------------------

# Print numbers from 1 to 10

'''num = 1             # state
while num <= 9:     # condition check each iteration(business logic)
    num = num + 1   #  increment
    print(num)      # part behaviour'''
#----------------------------------------------------------------------------------------------------------------
# print 1,2,3,4,5,......10
"""num = 0
while num <= 9:
    num = num + 1
    print(num,end=' ')
print() """
#----------------------------------------------------------------------------------------------------------------
# even number and odd numbers

"""num = 0
while num <= 10:
    num = num + 1
    if num %2 == 0:
        print("even number",num)
    else:
        print("odd number",num) """
#--------------------------------------------------------------------------------------------------------------------
# even number and odd numbers
"""
num = 0
while num <= 10:
    num = num + 1
    if num %2 == 0:
        print("even number",num)
    else:
        print("odd number",num) """
#----------------------------------------------------------------------------------------------------------------
"""
num = 0
while (num <=11):
    num = num + 1
    if num%3==0 :
        print(num,"divisible by 3")
"""
#------------------------------------------------------------------------------------------------------------------
# print numbers divisible by 3 and 5
"""num = 0
while num <= 100:
    num = num + 1
    if num % 3 == 0 and num % 5 == 0:
        print(" 3 and 5 divisibles are",num) """
#------------------------------------------------------------------------------------------------------------------------

# print numbers 20 to 40
'''a=20                     # state
while a <=40:            # defining conditional
    print(a)             # behaviour
    a+=1                 # increment'''

"""
a = int(input("enter a number"))
b = int(input("enter b number "))
if a < b:
    while a <= b:
        if a % 2 == 0:
            print(a)   """
#---------------------------------------------------------------------------------------------------------------------
# numbers between the even numbers
'''num1 = int(input("enter num1"))    # state, user input
num2 = int(input("enter num2 "))   # state   , user input
while num1 < num2:                 # defining condition (comparision num1 and num2)
    if num1 % 2 == 0:              # business logic
        print(num1)                # behaviour
    num1 = num1 +1                 # increment
print("-------------")
print("----end -----------")'''
#-------------------------------------------------------------------------------------------------
# odd numbers
'''num1 = int(input("enter number1"))
num2 = int(input("enter number2"))
while num1 <= num2:
    if num1%2 == 1:
        print("odd number is",num1)
    num1 +=1
print('------end--------')'''

#--------------------------------------------------------------------------------------------------------
# print 1 to 10
'''print("---------------------print 1 to 10----------------")
num = 1
while num <= 10:
    print(num, end=' ')
    num+=1
print('\n'"-----end ---------")'''
#--------------------------------------------------------------------------------------------------------------------------

# print 10 to 1
'''print("---------------------print 10 to 1----------------")
num = 10
while num >= 1:
    print(num, end=' ')
    num-=1
print('\n'"-----end ---------")'''

#--------------------------------------------------------------------------------------------------------------------------------------
# 8 multiples
'''print('---------------8 multiples------------------')
num = 1
while num <=100:
    if num % 8 == 0:
        print(num)
    num+=1
print("---------end--------------")'''
#--------------------------------------------------------------------------------------------------------------------------

#prime numbers
'''print("---------------prime numbers  between 1 to 100--------------")
num = 2
while num <= 100:
    if num%2 != 0 and num%3 != 0 and num%5 != 0:
        print(num)
    num+=1'''

#----------------------------------------------------------------------------------------------------------------------------------

# REQ : Print even numbers between 1 to 10
'''
  | 2  4          |   2)4(
'''
'''
# STATE    : num = 1
# BEHAVIOR : Print even numbers
             upper limit 10
'''
print("--------Print even numbers--------")
# STATE
num = 1
while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1

print("--------Print odd numbers--------")

# Print odd numbers betweeen 10 to 20
num = 10
while num <= 20:
    if num % 2 == 1:
        print(num)
    num += 1

# Print numbers between 500 to 1000 and divisible by 5

print("--Numbers divisible  with 5------")
num = 500
while num <= 600:
    if num % 5 == 0:
        print(num)
    num += 1


# Print numbers between 500 to 1000. It should be divisible by 5 and divisible by 8
print("--Numbers divisible  with 5 and 8------")
num = 500
while num <= 600:
    if num % 5 == 0 and num % 8 == 0:
        print(num)
    num += 1

# Print numbers between 500 to 1000. It should be divisible by 5 or divisible by 9
print("--Numbers divisible  with 5 or 9------")
num = 500
while num <= 600:
    if num % 5 == 0 or num % 9 == 0:
        print(num)
    num += 1


'''
S1 : REQUIREMENT : Print numbers which are divisible by 4 between 0 to 100
S2,S3 :Analysis,Design:
-----------------------
Step1: Take the user input,iterate till upper limit
Step2: Check whether the value divisible by 4 or not
Step3: If True, print the value
'''

# 0 1 2 3 4 5 6 7 8 9 10... 100
print("--------Numbers between 0 to 100---------")
x = 0
while x <= 100:
    if x % 4 == 0:
        print(x)
    x += 1


'''
# S1: REQUIREMENT : Print numbers which are divisible by 
                    either 3 or 8 between 1 to 1000
'''
print("-------------either 3 or 8 between 1 to 1000-------------")
x = 1
while x <= 1000:
    if x % 3 == 0 or x % 8 == 0:
        print(x)
    x += 1



'''
# S1: REQUIREMENT : Print numbers which are 
                    divisible by 5 and 10 between 1 to 100
'''
print("---------either 5 and 7 between 1 to 100-------------")
x = 1
while x <= 100:
    if x % 5 == 0 and x % 10 == 0:
        print(x)
    x += 1

x = 10
y = 20
print(x > y and y < 100)


# Program to add natural
# numbers up to
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)


'''Example to illustrate
the use of else statement
with the while loop'''

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")

# Prints all letters except 'e' and 's'
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue

    print('Current Letter :', a[i])
    i += 1

#for loop:
'''For loops are used for sequential traversal.'''

'''1 A for loop is used for iterating over a sequence 
(that is either a list, a tuple, a dictionary, a set, or a string).
2 This is less like the for keyword in other programming languages, and works more like
 an iterator method as found in other object-orientated programming languages.
3 With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.'''
#---------------------------------------------------------------------------------------------------------
'''a = 15
for i in range(a, 0, -1):
    print(i)
if True : print("true") ; print('hello') ;'''
#---------------------------------------------------------------------------------------------------------
"""# print 1 to 100 using for loop
for i in range(10):
    print("sequence numbers ",i)
#---------------------------------------------------------------------------------------------------------------
#direct given input
a=10
for i in range(a):
    print(i)
#---------------------------------------------------------------------------------------------------------------
# user give input
a = int(input("you enter only integer numbers"))
for num in range(a):
    print(num)
#---------------------------------------------------------------------------------------------------------------
# two user inputs
a=int(input("enter a number"))
b=int(input("enter b number"))
for num in range(a,b+1):
    print(num)
#-------------------------------------------------------------------------------------------------------------------
# string
for i in "kumar":
    print("sequnece of name",i)
print('-----------using for in list------------------')
for i in [1,2,3,4,5,6]:
    print(i)
print('--------for loop using numbers in string--------------')
for i in "12345":
    print(i)
print("---------using for loop in tuple -----------------------")
for i in (1,2,3,4,5,6):
    print(i)
print("------using for loop in set------------------------------")
for i in {10,20,30,40,50}:
    print(i)
#----------------------------------------------------------------------------------------------------------
print("---------------using for loop in dictionary------------------------------")
for i in {'name':'satish','id':27,'company':'MCS','location':'banglure'}:
    print(i)  # only gives keys
data = {'name': 'satish','id': 27,'company': 'MCS','location': 'banglure'}
for i in data:
    print(i)  # only gives keys
for key, value in data.items():
    print(key,value)
print(data['name'])
#------------------------------------------------------------------------------------------------------------
print('---------for loop using list----------------')
list =[1,2.0,"satish",4,8,90.20]
print(list)
for i in list:
    print(i)
#------------------------------------------------------------------------------------------------------------
print("----------for loop using tuple-------------")
data = (1,2,3,10.08,'yuvi',20,145)
for tup in data:
    print(tup)
#---------------------------------------------------------------------------------------------------------------
print("----------for loop using set--------------------")
data = {1,4,9,'kiran','sai',50.09}
for i in data:
    print(i)
#-------------------------------------------------------------------------------------------------------------
print('--------print even numbers using for loop---------------')
num = int(input("enter any number:"))
for i in range(num+1):
    if i%2==0:
        print("even number is ",i)
print()
#--------------------------------------------------------------------------------------------------------------
print("-------------print even numbers and store in list----------")
list = []
num = int(input("enter any number:"))
for i in range(num):
    if i%2 == 0:
        list.append(i)
print("even numbers",list)
#--------------------------------------------------------------------------------------------------------------
print('----------print odd numbers and store in  list--------------')
list =[]
num = int(input("enter any number:"))
for i in range(num+1):
    if i%2==1:
        list.append(i)
print("odd numbers ",list)
#------------------------------------------------------------------------------------------------------------
print('--------print odd and even numbers and store in list---------')
even = []
odd =[]
prime = []
num = int(input("enter any number:"))
for i in range(num):
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
        if i%5!=0 and i%3!=0:
            prime.append(i)
print("even numbers",even)
print("odd numbers ",odd)
print("prime numbers",prime)
#-----------------------------------------------------------------------------------------------------------
print('---------membership in list(compare two list--------------')
list = [1,2,3,4,5]
list1 =[1,2,3,4,5,6,9]
for i in list:
    for j in list1:
        if i==j:
            print("same",i)
else:
    print("not same",i)
#--------------------------------------------------------------------------------------------------------------
print("--------print table----------------")
num = int(input("which table do you want:"))
num1 = int(input('enter range of a number'))
for i in range(1,num1+1):
    print(num,'x',i,'=',(num * i))
for i in [1,2,23]:
    print(i,end=' ')
#---------------------------------------------------------------------------------------------------------------
print('-----------------using for loop in dictionary-------------------')
data = {'name':'yuvi','id':12,'location':'hyd'}
print(data)
for i in data:
   # print(i)    # its print only keys
   # print(data[i])  # its print only values
    print(i,':',data[i])
marks = {'telugu':80,'english':60,'maths':80}
student = ['kumar','yuvi','kiran']
for s in student:
    for key,values in marks.items():
            print(s,key,values)
#--------------------------------------------------------------------------------------------------------
print("----------nested if and for loop----------------")
name = input("enter your name:")
roll_no = int(input("enter your roll number: "))
if name == "satish":
    if roll_no == 27:
        print("your ssc marks ")
        list = []
        marks = {'telugu': 80, 'hindi': 68, 'english': 60, 'maths': 80, 'social': 88, 'science': 95}
        for key, value in marks.items():
            print(key, value)
            list.append(value)
        print("your percentage :", sum(list)//6)
    else:
        print("your roll number is not matched")
else:
    print("please enter valid name")    """
#------------------------------------------------------------------------------------------------------------



nums = [1, 2, 3, 4, 5, 6]

n = 2

found = False
for num in nums:
    if n == num:
        found = True
        break

print(f'List contains {n}: {found}')


def print_sum_even_nums(even_nums):
    total = 0

    for x in even_nums:
        if x % 2 != 0:
            break

        total += x
    else:
        print("For loop executed normally")
        print(f'Sum of numbers {total}')


# this will print the sum
print_sum_even_nums([2, 4, 6, 8])

# this won't print the sum because of an odd number in the sequence
print_sum_even_nums([2, 4, 5, 8])

# Python program to demonstrate
# break statement

# Python program to
# demonstrate break statement

s = 'geeksforgeeks'
# Using for loop
for letter in s:

    print(letter)
    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
        break

print("Out of for loop")
print()

for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print ('Current Letter :', letter)

my_list = ['Siya', 'Tiya', 'Guru', 'Daksh', 'Riya', 'Guru']

for i in range(len(my_list)):
    print(my_list[i])
    if my_list[i] == 'Guru':
        print('Found the name Guru')
        break
        print('After break statement')

print('Loop is Terminated')

for i in range(4):
    for j in range(4):
        if j==2:
            break
        print("The number is ",i,j);

# Use of break statement inside the loop

for val in "string":
    if val == "i":
        break
    print(val)

print("The end")


numbers = [10, 40, 120, 230]
for i in numbers:
    if i > 100:
        break
    print('current number', i)

for i in range(1, 11):
    print('Multiplication table of', i)
    for j in range(1, 11):
        # condition to break inner loop
        if i > 5 and j > 5:
            break
        print(i * j, end=' ')
    print('')
for i in range(1, 11):
    # condition to break outer loop
    if i > 5:
        break
    print('Multiplication table of', i)
    for j in range(1, 11):
        print(i * j, end=' ')
    print('')

x = 0
for x in range(10):
    if x == 4:
        break
    print(x)


nums = [1, 2, -3, 4, -5, 6]

sum_positives = 0

for num in nums:
    if num < 0:
        continue
    sum_positives += num

print(f'Sum of Positive Numbers: {sum_positives}')

# Python program to
# demonstrate continue
# statement

# loop from 1 to 10
for i in range(1, 11):

    # If i is equals to 6,
    # continue to next iteration
    # without printing
    if i == 6:
        continue
    else:
        # otherwise print the value
        # of i
        print(i, end=" ")
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print('Current Letter :', letter)

for i in range(10):
    if i == 7:
        continue
    print("The Number is :" , i)

# Program to show the use of continue statement inside loops

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")
#continue statement in for loop
numbers = [2, 3, 11, 7]
for i in numbers:
    print('Current Number is', i)
    # skip below statement if number is greater than 10
    if i > 10:
        continue
    square = i * i
    print('Square of a current number is', square)
#Continue Statement in Nested Loop:?
for i in range(1, 11):
    print('Multiplication table of', i)
    for j in range(1, 11):
        # condition to skip current iteration
        if j == 5:
            continue
        print(i * j, end=' ')
    print('')

#Continue Statement in Outer loop:?

for i in range(1, 11):
    # condition to skip iteration
    # Don't print multiplication table of even numbers
    if i % 2 == 0:
        continue
    print('Multiplication table of', i)
    for j in range(1, 11):
        print(i * j, end=' ')
    print('')

x = 0
for x in range(10):
    if x == 4:
        continue
    print(x)


# Python program to demonstrate
# pass statement


s = "geeks"

# Empty loop
for i in s:
	# No error will be raised
	pass

# Empty function
def fun():
	pass

# No error will be raised
fun()

# Pass statement
for i in s:
	if i == 'k':
		print('Pass executed')
		pass
	print(i)


for letter in 'Python':
   if letter == 'h':
      pass
      print ('This is pass block')
   print ('Current Letter :', letter)

print ("Good bye!")


def my_func():
    print('pass inside function')
    pass
my_func()


# Pass statement in for-loop
test = "Guru"
for i in test:
    if i == 'r':
        print('Pass executed')
        pass
    print(i)


a=1
if a==1:
    print('pass executed')
    pass


months = ['January', 'June', 'March', 'April']
for mon in months:
    pass
print(months)


x = 0
for x in range(10):
    if x == 4:
        pass
    print(x)