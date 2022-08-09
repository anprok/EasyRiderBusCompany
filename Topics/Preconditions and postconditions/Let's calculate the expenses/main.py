import re

string = input()
pattern = r'(?<=\$)\d+'
res = [int(item) for item in re.findall(pattern, string)]
print("This week you have spent: {} dollars".format(sum(res)))
