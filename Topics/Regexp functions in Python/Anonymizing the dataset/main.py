import re

string = input()

pattern = r'@\w+'
replace_author = '<AUTHOR>'
replace_handle = '<HANDLE>'

string = re.sub(pattern, replace_author, string, count=1)
string = re.sub(pattern, replace_handle, string)
print(string)
