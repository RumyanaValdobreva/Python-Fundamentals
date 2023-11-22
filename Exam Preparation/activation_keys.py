def contains(activation_key, command):
    substring = command[1]
    if substring in activation_key:
        return f"{activation_key} contains {substring}"
    else:
        return "Substring not found!"

def flip(raw_activation_key, command):
    actions = command[1]
    start_index = int(command[2])
    end_index = int(command[3])
    before_substring = raw_activation_key[:start_index]
    after_substring = raw_activation_key[end_index:]
    substring = raw_activation_key[start_index: end_index]
    if actions == "Upper":
        substring = substring.upper()
    elif actions == "Lower":
        substring = substring.lower()
    raw_activation_key = before_substring + substring + after_substring
    return raw_activation_key

def slice(raw_activation_key, command):
    start_index = int(command[1])
    end_index = int(command[2])
    before_substring = raw_activation_key[:start_index]
    after_substring = raw_activation_key[end_index:]
    raw_activation_key = before_substring + after_substring
    return raw_activation_key


text = input()
command = input()

while command != "Generate":
    command = command.split(">>>")
    action = command[0]
    if action == "Contains":
        print(contains(text, command))
    elif action == "Flip":
        text = flip(text, command)
        print(text)
    elif action == "Slice":
        text = slice(text, command)
        print(text)
    command = input()

print(f"Your activation key is: {text}")