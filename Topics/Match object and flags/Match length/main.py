import re

template = r'are you ready??.?.?'
new = input()
match_result = re.match(template, new)
if match_result:
    print(len(match_result.group()) or "0")
else:
    print("0")