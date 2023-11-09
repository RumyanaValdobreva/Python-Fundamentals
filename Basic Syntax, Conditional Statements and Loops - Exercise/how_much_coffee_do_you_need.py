command = input()
coffee_qty = 0

while command != 'END':
    lowercase = command.lower()
    if lowercase == 'coding' or lowercase == 'dog' or lowercase == 'cat' or lowercase == 'movie':
        if command == command.upper():
            coffee_qty += 2
        else:
            coffee_qty += 1

    command = input()

if coffee_qty > 5:
    print("You need extra sleep")
else:
    print(coffee_qty)