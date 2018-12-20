import re

string = 'Kyrgyzstan 45, Street 23/3  123.123'

match = re.findall(r'(\d+)', string)

if match:
    print(match)
