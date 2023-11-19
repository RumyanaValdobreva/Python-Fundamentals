numbers = input().split()

opposite_numbers = []

for element in numbers:
    num = -int(element)
    opposite_numbers.append(num)

print(opposite_numbers)