list_of_numbers = input().split()

absolute_value = []

for num in list_of_numbers:
    absolute_value.append(abs(float(num)))

print(absolute_value)