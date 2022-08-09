import re

string = input()
pattern = '(?<=<li>).*?(?=</li>)'
print(*re.findall(pattern, string), sep='\n')