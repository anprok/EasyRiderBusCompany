import re

pets = input()
pattern = "(dog|cat|parrot|hamster)"
print(re.findall(pattern, pets, flags=re.IGNORECASE))