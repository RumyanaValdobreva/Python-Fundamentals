def all_characters(first, second):
    characters = []
    for char in range(ord(first) + 1, ord(second)):
        characters.append(chr(char))
    return characters

first_char = input()
second_char = input()
result = all_characters(first_char, second_char)
print(" ".join(result))