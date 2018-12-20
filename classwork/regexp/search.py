import re

string = 'Kyrgyzstan 45, Street 23/3'

match = re.search(r'(?P<build>\d+)/(?P<flat>\d+)', string)

if match:
    print(match.group())
    print(match.groupdict())
