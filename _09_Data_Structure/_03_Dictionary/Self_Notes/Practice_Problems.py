# A Python program to create a dictionary with employee details and retrieve the values upon giving the keys.

# dict = {'Name':'Chandra', 'Id':10, 'Salary':9080.5}
#
# print('Name of the employee: ', dict['Name'])
# print('Id number: ', dict['Id'])
# print('Salary: ', dict['Salary'])

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
# print('Keys = ', dict.keys())
# print('Values = ', dict.values())
# print('Items = ', dict.items())

# A Python program to create a dictionary and find the sum of values.

# dict = eval(input('Enter the number in {}: '))
#
# s = sum(dict.values())
# print('Sum of dict: ', s)

# A Python program to create a dictionary from keyboard and display the elements.

# x = {}
#
# print('Enter the no. of elements: ', end='')
# n = int(input())
#
# for i in range(n):
#     print('Enter the keys: ', end='')
#     k = input()
#     print('Enter the values: ', end='')
#     v = int(input())
#     x.update({k: v})
#
# print('The dictionary is: ', x)

# A Python program to create a dictionary with cricket players names and scores in a match.
# Also we are retreving runs by entering the player's name.

# x = {}
#
# print('Enter the no. of players: ', end='')
# n = int(input())
#
# for i in range(n):
#     print('Enter the keys: ', end='')
#     k = input()
#     print('Enter the values: ', end='')
#     v = int(input())
#     x.update({k: v})
#
# print('Score of all the players: ', x)
#
# print('Name of all the employees: ')
# for i in x.keys():
#     print(i)
#
# print('Enter the name of the player: ', end='')
# name = input()
#
# runs = x.get(name, -1)
# if runs == -1:
#     print('Player not found.')
# else:
#     print('{} scored {} runs.'.format(name, runs))

# A Python program to show the usage of for loop to retrieve elements of dictionaries.

# colors = {'v': 'Vegetables', 'f': 'Fruits', 'j': 'Juices', 'm': 'Medicines'}
#
# for i in colors:
#     print(i)
#
# for i in colors:
#     print(colors[i])
#
# for i, j in colors.items():
#     print('Key= {} Value= {}'.format(i, j))

# A Python program to find the number of occurences of each letter in a string using dictionary.

# str = input('Enter the character: ')
#
# dict = {}
#
# for i in str:
#     dict[i] = dict.get(i, 0) + 1
#
# print(dict)
#
# for k, v in dict.items():
#     print('Key={} Occurences={}'.format(k, v))

# A Python program to sort the elements of a dictionary based on a key or value.

# colors = {10:'Red', 35:'Green', 15:'Blue', 25:'White'}
#
# c1 = sorted(colors.items(), key= lambda t: t[0])
# print(c1)
#
# c2 = sorted(colors.items(), key= lambda t: t[1])
# print(c2)