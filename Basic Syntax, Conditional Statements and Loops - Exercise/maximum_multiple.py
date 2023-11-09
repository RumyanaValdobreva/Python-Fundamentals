divisor = int(input())
bound = int(input())

number = (bound // divisor) * divisor

if number <= 0:
    number = divisor

print(number)