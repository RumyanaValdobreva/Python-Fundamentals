def smallest_number(num):
    if first_number < second_number and first_number < third_number:
        return first_number
    elif second_number < first_number and second_number < third_number:
        return second_number
    elif third_number < first_number and third_number < second_number:
        return third_number

first_number = int(input())
second_number = int(input())
third_number = int(input())
numbers = [first_number, second_number, third_number]

print(smallest_number(numbers))