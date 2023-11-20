numbers = [int(x) for x in input.split(", ")]
group = 10

while len(numbers) > 0:
    list_ = []
    index = 0
    while index < len(numbers):
        num = numbers[index]
        if num <= group:
            list_.append(num)
            numbers.remove(numbers[index])
            continue
        index += 1

    print(f"Group of {group}'s: {list_}")
    group += 10