def calculate(first_string, second_string):
    total_sum = 0
    for first_char, second_char in zip(first_string, second_string):
        total_sum += ord(first_char) * ord(second_char)

    remaining_chars1 = first_string[len(second_string):]
    remaining_chars2 = second_string[len(first_string):]

    for char in remaining_chars1:
        total_sum += ord(char)

    for char in remaining_chars2:
        total_sum += ord(char)

    return total_sum


str1, str2 = input().split()

result = calculate(str1, str2)
print(result)
