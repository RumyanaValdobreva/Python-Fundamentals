products = input().split()

stock = {}

for i in range(0, len(products), 2):
    product = products[i]
    qty = int(products[i + 1])
    stock[product] = qty

searched = input().split()

for element in searched:
    if element in stock:
        print(f"We have {stock[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")