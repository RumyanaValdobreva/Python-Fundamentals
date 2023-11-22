company = {}


while True:
    command = input()
    if command == "End":
        break
    current_command = command.split(" -> ")
    if current_command[0] not in company:
        company[current_command[0]] = [current_command[1]]
    else:
        if current_command[1] in company[current_command[0]]:
            continue
        else:
            company[current_command[0]] += [current_command[1]]

for key in company.keys():
    print(f"{key}")
    for value in company[key]:
        print(f"-- {value}")