words = input.split()

for word in words:
    first_number = ""
    second_part = ""
    for el in word:
        if el.isdigit():
            first_number += el
        else:
            second_part += el
    first_letter = chr(int(first_number))
    half_part = first_letter + second_part
    current_list = [value for index, value in enumerate(half_part)]
    current_list[1], current_list[-1] = current_list[-1], current_list[1]
    print("".join(current_list), end=" ")