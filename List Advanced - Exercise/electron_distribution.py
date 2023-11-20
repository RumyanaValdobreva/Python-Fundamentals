number_of_electrons = int(input())
result = []
shell = 1

while True:
    number = 2 * (shell ** 2)
    if number_of_electrons - number > 0:
        result.append(number)
        number_of_electrons -= number
    else:
        result.append(number_of_electrons)
        number_of_electrons -= number_of_electrons
    shell += 1

print(result)