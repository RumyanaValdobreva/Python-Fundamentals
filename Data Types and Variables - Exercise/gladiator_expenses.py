lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmets = lost_fights_count // 2
broken_sword = lost_fights_count // 3
broken_shield = lost_fights_count // (2 * 3)
broken_armor = broken_shield // 2

expenses = broken_helmets * helmet_price  + broken_sword * sword_price + broken_shield * shield_price + broken_armor * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")