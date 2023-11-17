number_of_lines = int(input())
total_sum = 0

for line in range(number_of_lines):
    character = input()
    total_sum += ord(character)

print(f"The sum equals: {total_sum}")