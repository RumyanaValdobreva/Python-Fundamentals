key = int(input())
number_of_lines = int(input())

message = ''

for i in range(number_of_lines):
    letter = ord(input())
    decrypted_letters = chr(letter + key)
    message += decrypted_letters

print(message)