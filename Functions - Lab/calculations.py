def calculation_result(type_operator, number1, number2):
    if type_operator == 'multiply':
        return number1 * number2
    elif type_operator == 'divide':
        return int(number1 / number2)
    elif type_operator == 'add':
        return number1 + number2
    elif type_operator == 'subtract':
        return number1 - number2


type_operator = input()
number1 = int(input())
number2 = int(input())

print(calculation_result(type_operator, number1, number2))
