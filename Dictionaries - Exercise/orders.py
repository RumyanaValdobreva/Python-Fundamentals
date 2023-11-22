products = {}

while True:
    command = input()
    if command == "buy":
        break
    else:
        name, price, quantity = command.split(" ")
        if name not in products:
            products[name] = [float(price), int(quantity)]
        else:
            products[name][1] += int(quantity)
            products[name][0] = float(price)

for key, value in products.items():
    value = (value[0] * value[1])
    print(f"{key} -> {value:.2f}")

