import re

string = input()
pattern = r'^[0-3]\d/[0-1]\d/(\d){4}$'
match = re.match(pattern, string)
print(match is not None)