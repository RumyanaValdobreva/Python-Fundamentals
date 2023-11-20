def positive_numbers(current_numbers):
    return ", ".join([number for number in current_numbers if int(number) >= 0])


def negative_numbers(current_numbers):
    return ", ".join([number for number in current_numbers if int(number) < 0])


def even_numbers(current_numbers):
    return ", ".join([number for number in current_numbers if int(number) % 2 == 0])


def odd_numbers(current_numbers):
    return ", ".join([number for number in current_numbers if int(number) % 2 != 0])


numbers = input().split(", ")

print(f"Positive: {positive_numbers(numbers)}\nNegative: {negative_numbers(numbers)}"
      f"\nEven: {even_numbers(numbers)}\nOdd: {odd_numbers(numbers)}")