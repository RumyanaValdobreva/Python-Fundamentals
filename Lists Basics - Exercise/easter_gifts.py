names_of_gifts = input().split(" ")

while True:
    command = input()
    if command == "No Money":
        break
    else:
        current_command = command.split(" ")
        if current_command[0] == "OutOfStock":
            for current_gift in names_of_gifts:
                if current_command[1] == current_gift:
                    index_gift = names_of_gifts.index(current_gift)
                    names_of_gifts[index_gift] = "None"
        elif current_command[0] == "Required":
            for index in range(len(names_of_gifts)):
                if int(current_command[2]) == index:
                    names_of_gifts[index] = current_command[1]
        elif current_command[0] == "JustInCase":
            index_last_gift = len(names_of_gifts) - 1
            names_of_gifts[index_last_gift] = current_command[1]

while "None" in names_of_gifts:
    names_of_gifts.remove("None")

print(" ".join(names_of_gifts))