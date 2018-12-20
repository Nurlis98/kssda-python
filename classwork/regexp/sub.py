import re

string = 'Some, string. with; Any wth: chars? For # slpit@'
print(string)
res = re.sub(r'\W+', '*', string)
print(res)
