import re

names = input()
result = re.split(r'\d+', names)
print(result)
