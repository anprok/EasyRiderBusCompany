#  You can experiment here, it won’t be checked
import re

template = "ahoy,.me hearties!"
string = '''ahoy,
me hearties!'''
match = re.match(template, string, flags=re.DOTALL  )
print(match is not None)  # The output is True