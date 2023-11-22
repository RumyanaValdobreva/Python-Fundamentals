phonebook = {}
number = 0

while True:
    command = input()
    if command.isdigit():
        number = int(command)
        break
    else:
        name, phone_number = command.split("-")
        if name not in phonebook:
            phonebook[name] = (phone_number)
        else:
            phonebook[name] = phone_number


for _ in range(1, number + 1):
    searched_name = input()
    if searched_name not in phonebook:
        print(f"Contact {searched_name} does not exist.")
    else:
        print(f"{searched_name} -> {phonebook[searched_name]}")
