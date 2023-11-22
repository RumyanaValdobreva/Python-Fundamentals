food_qty = input().split()

stock = {}

for i in range(0, len(food_qty), 2):
    food = food_qty[i]
    qty = int(food_qty[i + 1])
    stock[food] = qty

print(stock)