'''

Calling a function is executing the function that we have defined.
Either directly from python prompt or through another function.

'''

def add(n1, n2):
    print("The addition of two numbers: ", n1+n2)

addition_of = add(432,343)
#Calling a Function


# To call a function, use the function name followed by parenthesis:
# Requirement: Add two no
#function defination

def add(n1,n2):    # function signature
  "#function body"
  n3= n1+n2
  print("sum of a no", n3)
add(87,52)   # Function calling
------------------------------------------------

#Requirement :  Check the entered number is +ve or -ve
#State
num=int(input("Enter a number: "))
# Behavior

def check(num): #Function Definition
# Function body
 if num >= 0:
  print(num,"is +ve number")
 else:
  print(num,"is -ve number")

check(num)     # calling function
------------------------------------------
#Requirement :  print table
# Behavior
def multi(n): #Function Definition
 print(n)
 i = 1
 while i < 11:
  result = i * n
  i += 1
  print("Table of",n, "is =",result)
#State
num = int(input("Enter a no"))
multi(num)     # calling function

-------------------------------------------------

#Requirement :  print table
# Behavior
def multiplication(n): #Function Definition
  i = 1
 while i < 11:
  res =i * n
  i += 1
  print(res)
#State
n = int(input("Enter a number: "))
multiplication(n)     # calling function
-------------------------------------------------
#Requirement :  Concatinate name enter name
# Behavior
def full_name(fname,lname):
 full_name = fname+" "+lname
 print("Full name :", full_name)

fn = input("Enter the first name: ")
ln = input("Enter the last name: ")
full_name(fn,ln) # calling function
