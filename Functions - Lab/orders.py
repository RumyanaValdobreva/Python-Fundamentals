def calculate_price():
    if type_product == 'coffee':
        return qty_of_product * 1.50
    elif type_product == 'coke':
        return qty_of_product * 1.40
    elif type_product == 'water':
        return qty_of_product * 1.00
    elif type_product == 'snacks':
        return qty_of_product * 2.00
type_product = input()
qty_of_product = int(input())

print('{0:.2f}'.format(calculate_price()))