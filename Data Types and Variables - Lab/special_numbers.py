n = int(input())

for number in range(1, n + 1):
    sum_of_digits = 0
    number = str(number)
    for i in range(len(number)):
        digit = number[i]
        sum_of_digits += int(digit)

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")