string = input()
string_dict = dict()
for current_char in string:
    if current_char == " ":
        continue
    key = current_char
    value = 1
    if key not in string_dict:
        string_dict[key] = []
        string_dict[key] = value
    else:
        string_dict[key] += value

for key, value in string_dict.items():
    print(f"{key} -> {value}")
