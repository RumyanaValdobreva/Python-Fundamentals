def min_number(number):
    minimum_number = min(numbers)
    return f"The minimum number is {minimum_number}"

def max_number(number):
    maximum_number = max(numbers)
    return f"The maximum number is {maximum_number}"

def sum_numbers(number):
    sum_of_numbers = sum(numbers)
    return f"The sum number is: {sum_of_numbers}"


numbers = [int(x) for x in input().split()]

print(min_number(numbers))
print(max_number(numbers))
print(sum_numbers(numbers))