def even_odd_numbers(number):
    odd_digits = 0
    even_digits = 0
    for digit in number:
        if int(digit) % 2 == 0:
            even_digits += int(digit)
        elif int(digit) % 2 != 0:
            odd_digits += int(digit)
    return even_digits, odd_digits

numbers = input()
even_digits, odd_digits = even_odd_numbers(numbers)
print(f"Odd sum = {odd_digits}, Even sum = {even_digits}")