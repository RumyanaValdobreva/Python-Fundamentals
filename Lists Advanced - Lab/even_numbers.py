numbers = list(map(int, input().split(", ")))

even_numbers = [num for num in range(len(numbers)) if numbers[num] % 2 == 0]

print(even_numbers)