import re

string = input()

word = fr"\b{input()}\b"
result = re.findall(word, string, re.IGNORECASE)

print(len(result))
