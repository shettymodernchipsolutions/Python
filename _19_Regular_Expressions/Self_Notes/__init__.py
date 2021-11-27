'''
Regular Expression
----------------------
'''
import re

# text = 'Python is super easy'
# regex = r'Python'
# match = re.match(regex, text)
# print('Matching regex with text: ', match)

# text = 'Python is super easy'
# regex = r'Python'
# match1 = re.match(regex, text)
# print(match1)
# print(match1.span())
# start, end = match1.span()
# print(text[start:end:])
# print(text[match1.start(): match1.end():])


text = 'Python is super easy'
regex = r'\W'
match = re.compile(regex)
matches = match.finditer(text)
for i in matches:
    print(i)
print(matches)

# Program to check whether the string begins and ends as declared in the variable

text = 'The best language in the world is Python'
reg = re.search('^The.*Python$', text)
if reg:
    print('Yes')
else:
    print('No')


