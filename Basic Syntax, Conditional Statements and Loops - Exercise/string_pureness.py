number = int(input())

for i in range(number):
    string = input()
    character = True
    for j in range(len(string)):
        if string[j] == ',' or string[j] == '.' or string[j] == '_':
            print(f"{string} is not pure!")
            character = False
            break
    if character:
        print(f"{string} is pure.")