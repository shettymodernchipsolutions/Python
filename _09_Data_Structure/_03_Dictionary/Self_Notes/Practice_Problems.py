# A Python program to create a dictionary with employee details and retrieve the values upon giving the keys.

# dict = {'Name':'Chandra', 'Id':10, 'Salary':9080.5}
#
# print('Name of Employee = ', dict['Name'])
# print('Id Number = ', dict['Id'])
# print('Salary = ', dict['Salary'])

# dict = {'Name': 'Suresh', 'Roll No.': 78, 'Marks': 980}
# print('No. of key-value pairs: ', len(dict))
# print(dict)
# dict['Marks'] = 950
# print(dict)
# dict['Branch'] = 'Mechanical'
# print(dict)

# A Python program to retrieve keys, values and key-value pairs from a dictionary.

# dict = {'Name':'Chandra', 'Id':10, 'Salary':9080.5}
# print(dict)
#
# print('Keys in dict = ', dict.keys())
# print('Values in dict = ', dict.values())
# print('Items in dict = ', dict.items())

# A Python program to create a dictionary and find the sum of values.

# dict = eval(input('Enter elements in { }: '))
#
# s = sum(dict.values())
# print('Sum of values in the dictionary: ', s)

# A Python program to create a dictionary from keyboard and display the elements.

# x = {}
#
# print('How many elements? ', end='')
# n = int(input())
#
# for i in range(n):
#     print('Enter key: ', end='')
#     k = input()
#     print('Enter its value: ', end='')
#     v = int(input())
#     x.update({k:v})
#
# print('The dictionary is: ', x)

# A Python program to create a dictionary with cricket players names and scores in a match.
# Also we are retreving runs by entering the player's name.

x = {}

print('How many players? ', end='')
n = int(input())

for i in range(n):
    print('Enter player name: ', end='')
    k = input()
    print('Enter runs: ', end='')
    v = int(input())
    x.update({k:v})

print('\nPlayers in this match: ')
for pname in x.keys():
    print(pname)

print('Enter player name: ', end='')
name = input()

runs = x.get(name, -1)
if runs == -1:
    print('Player not found')
else:
    print('{} made runs {}'.format(name, runs))