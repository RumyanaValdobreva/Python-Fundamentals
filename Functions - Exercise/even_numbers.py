# def is_even(num):
#     if num % 2 == 0:
#         return num
#
# numbers = input().split()
# numbers_digits = []
# for number in numbers:
#     numbers_digits.append(int(number))
#
# result = list(filter(is_even, numbers_digits))
# print(result)

numbers = input().split()
numbers_digits = []
for number in numbers:
    numbers_digits.append(int(number))

is_even = lambda x: x % 2 == 0
result = list(filter(is_even, numbers_digits))
print(result)