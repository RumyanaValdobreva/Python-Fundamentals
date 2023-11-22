numbers = int(input())
owner = {}

for current_number in range(numbers):
    command = input().split(' ')
    if command[0] == "register":
        if command[1] not in owner:
            owner[command[1]] = [command[2]]
            print(f"{command[1]} registered {command[2]} successfully")
        else:
            if command[2] in owner[command[1]]:
                print(f"ERROR: already registered with plate number {owner[command[1]][0]}")
    elif command[0] == "unregister":
        if command[1] not in owner:
            print(f"ERROR: user {command[1]} not found")
        else:
            print(f"{command[1]} unregistered successfully")
            owner.pop(command[1])

for key, value in owner.items():
    print(f"{key} => {''.join(value)}")