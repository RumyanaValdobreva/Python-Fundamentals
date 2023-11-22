sequence_of_strings = input().split()
new_sequence = [sequence * len(sequence) for sequence in sequence_of_strings]

print(''.join(new_sequence))