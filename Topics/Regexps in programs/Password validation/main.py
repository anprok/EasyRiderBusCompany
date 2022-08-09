import re

password = input()
pattern = r'^\S\w{6,15}\S$'
match = re.match(pattern, password, flags=re.ASCII)
# print(match)
print("Thank you!" if match is not None else 'Error!')