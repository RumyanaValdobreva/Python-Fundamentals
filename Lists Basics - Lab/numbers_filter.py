n = int(input())
numbers = []

for n in range(n):
    number = int(input())
    numbers.append(number)

type_number = input()
filtered_numbers = []
if type_number == 'even':
    for i in numbers:
        if i % 2 == 0:
            filtered_numbers.append(i)
elif type_number == 'odd':
    for i in numbers:
        if i % 2 != 0:
            filtered_numbers.append(i)
elif type_number == 'positive':
    for i in numbers:
        if i >= 0:
            filtered_numbers.append(i)
elif type_number == 'negative':
    for i in numbers:
        if i < 0:
            filtered_numbers.append(i)

print(filtered_numbers)