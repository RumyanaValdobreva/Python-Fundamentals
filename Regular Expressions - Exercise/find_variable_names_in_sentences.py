import re

string = input()
result = []

pattern = r"((?<=\s_)|(?<=^_))[a-zA-Z0-9]+((?=\s)|(?=$))"
regex_result = re.finditer(pattern, string, )


for i in regex_result:
    result.append(i.group())

print(",".join(result))