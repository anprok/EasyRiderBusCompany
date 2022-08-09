import re

string = input()

pattern = 'ou'
replacement = 'o'
print(re.sub(pattern, replacement, string))