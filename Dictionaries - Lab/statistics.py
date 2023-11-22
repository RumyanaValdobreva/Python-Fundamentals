stock = {}

while True:
    pairs = input()

    if pairs == 'statistics':
        break

    product, qty = pairs.split(": ")
    qty = int(qty)

    if product in stock:
        stock[product] += qty
    else:
        stock[product] = qty

product_count = len(stock)
total_qty = sum(stock.values())

print("Products in stock:")
for product, quantity in stock.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {product_count}")
print(f"Total Quantity: {total_qty}")