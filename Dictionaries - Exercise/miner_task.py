sequence = dict()

while True:
    command = input()
    if command == "stop":
        break
    next_command = int(input())
    if command not in sequence:
        sequence[command] = next_command
    else:
        sequence[command] += next_command

for key, value in sequence.items():
    print(f"{key} -> {value}")