numbers = input().split()
text = input()

message = ''

for number in numbers:
    sum_of_numbers_digits = sum(int(digit) for digit in number)
    if sum_of_numbers_digits >= len(text):
        sum_of_numbers_digits %= len(text)

    character = text[sum_of_numbers_digits]
    message += character
    text = text[:sum_of_numbers_digits] + text[sum_of_numbers_digits + 1:]

print(message)