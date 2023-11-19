def rounded_numbers(numbers):
    list_of_numbers = numbers.split()
    rounded_list = []
    for number in list_of_numbers:
        rounded_list.append(round(float(number)))
    return rounded_list


numbers = input()
print(rounded_numbers(numbers))