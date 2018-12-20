import re

string = 'Some, string. with; Any wth: chars? For # slpit@'

res = re.split(r'[A-Z]', string)
print(res)

string.split(';')
