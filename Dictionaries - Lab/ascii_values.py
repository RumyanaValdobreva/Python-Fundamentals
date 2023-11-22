characters = input().split(", ")
dictionary_characters = {char: ord(char) for char in characters}

print(dictionary_characters)