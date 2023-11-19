def sorted_numbers(num):
    sorted_num = sorted(list_of_numbers)
    return sorted_num

numbers = input().split()
list_of_numbers = []
for number in numbers:
    list_of_numbers.append(int(number))

print(sorted_numbers(list_of_numbers))