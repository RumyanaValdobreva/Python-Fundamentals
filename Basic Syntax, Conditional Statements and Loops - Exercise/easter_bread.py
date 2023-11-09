budget = float(input())
price_for_1_kg_flour = float(input())

price_for_eggs = price_for_1_kg_flour * 0.75
price_for_milk = price_for_1_kg_flour * 1.25
needed_milk = price_for_milk / 4
price_for_one_loaf = price_for_1_kg_flour + price_for_eggs + needed_milk
bread_counter = 0
eggs_counter = 0

while budget > 0 and budget > price_for_one_loaf:
    budget -= price_for_one_loaf
    bread_counter += 1
    eggs_counter += 3
    if bread_counter % 3 == 0:
        eggs_counter -= bread_counter - 2

print(f"You made {bread_counter} loaves of Easter bread! Now you have {eggs_counter} eggs and {budget:.2f}BGN left.")