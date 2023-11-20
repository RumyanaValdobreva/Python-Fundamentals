def pokemon_go(sequence_of_integers):
    result = 0
    while len(sequence_of_integers) > 0:
        index = int(input())
        current_result = 0
        if index < 0:
            current_result += sequence_of_integers[0]
            sequence_of_integers[0] = sequence_of_integers[-1]

        elif index >= len(sequence_of_integers):
            current_result += sequence_of_integers[-1]
            sequence_of_integers[-1] = sequence_of_integers[0]
        else:
            current_result += sequence_of_integers.pop(index)
        result += current_result

        for index, number in enumerate(sequence_of_integers):
            if current_result < number:
                sequence_of_integers[index] -= current_result
            else:
                sequence_of_integers[index] += current_result

    return result


numbers = list(map(int, input().split()))
print(pokemon_go(numbers))