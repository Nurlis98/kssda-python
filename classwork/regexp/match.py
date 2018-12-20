import re

# string = 'Kyrgyzstan 45, Street 23/3'
#
#
# match = re.match(r'\d+', string)
# if match:
#     print(match.group())

streets = [
    'Kyrgyzstan 45, Street 23/3',
    '45, Street 23/3',
]

_re = re.compile(r'\d+')
for s in streets:
    # match = re.match(r'\d+', s)
    match = _re.match(s)
    if match:
        print(match.group())
