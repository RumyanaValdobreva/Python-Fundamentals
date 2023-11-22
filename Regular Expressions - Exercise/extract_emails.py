import re

string = input()

pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-z]+-?[a-z]+(\.[a-z]+)+"
valid_emails = re.finditer(pattern, string)

for email in valid_emails:
    print(email.group())

