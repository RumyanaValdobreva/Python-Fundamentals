import re

names = input()

regex = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"
result = re.findall(regex, names)

for name in result:
    print(name, end=" ")