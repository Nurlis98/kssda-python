import re

string = 'Some 25/4, Foo 34/56, Bar 56/11'

print([
    r.groupdict()
    for r in re.finditer(
        r'(?P<street>[A-Za-z]+)\s(?P<house>\d+)/(?P<flat>\d+)',
        string
    )])

_re = re.compile(r'(?P<street>[A-Za-z]+)\s(?P<house>\d+)/(?P<flat>\d+)')
for r in _re.finditer(string):
    print(r.groupdict())

_re = re.compile(r'(?P<street>[A-Za-z]+)\s(?P<house>\d+)/(?P<flat>\d+)')
# _re = re.compile(r'([A-Za-z]+)\s(\d+)/(\d+)')
for r in _re.finditer(string):
    print(r.group(1), r.group(2), r.group(3))
    print(r.group('street'), r.group('house'), r.group('flat'))
    print('-----------------')
