import re

string = input()
capitalized = re.findall(r'[A-Z]\w+', string)
digits = re.findall(r'\d+', string)
print("Capitalized words: {}".format(", ".join(capitalized)))
print("Digits: {}".format(", ".join(digits)))