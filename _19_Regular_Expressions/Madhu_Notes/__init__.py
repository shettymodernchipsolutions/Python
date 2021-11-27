import re

text = 'Python is easy'
reg = re.search('^Python.*easy$', text)
if reg:
    print('Yes')
else:
    print('No')








