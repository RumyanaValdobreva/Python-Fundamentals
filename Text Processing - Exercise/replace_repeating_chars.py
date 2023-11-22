word = input()
result = []

for current_char in range(len(word)):
    if current_char == 0:
        result.append(word[current_char])
    elif result[-1] != word[current_char]:
        result.append(word[current_char])

print(f"{''.join(result)}")