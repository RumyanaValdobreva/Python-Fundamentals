sequence_of_numbers = list(map(float, input().split()))

left_time = 0
right_time = 0

for racer in range(len(sequence_of_numbers)):
    if racer == len(sequence_of_numbers) // 2:
        break

    if sequence_of_numbers[racer] != 0:
        left_time += sequence_of_numbers[racer]

    if sequence_of_numbers[-racer - 1] != 0:
        right_time += sequence_of_numbers[-racer - 1]

    if sequence_of_numbers[racer] == 0:
        left_time *= 0.8

    if sequence_of_numbers[-racer - 1] == 0:
        right_time *= 0.8

winner = "left" if left_time <= right_time else "right"
total_time = min(left_time, right_time)

print(f"The winner is {winner} with total time: {total_time:.1f}")