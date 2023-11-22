import re

pattern = r"\d+"
string = input()

while string:
    [print(num, end=" ") for num in re.findall(pattern, string)]
    string = input()