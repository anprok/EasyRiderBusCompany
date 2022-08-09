import re


# put your regex in the variable template
template = r"^((\d\d?)(/|\.)){2}(\d{4})[a-z]*$"
string = input()
match = re.match(template, string)
print(match.group(4) if match else 'None')