sequence = input()

digits = ''
letters = ''
characters = ''

for char in sequence:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    elif char != char.isdigit() and char != char.isalpha():
        characters += char

print(digits)
print(letters)
print(characters)