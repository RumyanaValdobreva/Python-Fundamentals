text = input()
encrypted_text = ""

for char in text:
    current = ord(char) + 3
    encrypted_text += chr(current)

print(encrypted_text)
