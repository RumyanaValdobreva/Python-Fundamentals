def is_perfect(num:int) -> str:
    divisor_sum = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            divisor_sum += divisor
    if num == divisor_sum:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

number = int(input())
print(is_perfect(number))