cells = input().split("#")
water_amount = int(input())
effort = 0
fire = 0
fire_out_cells = []
high = range(81, 125 + 1)
medium = range(51, 80 + 1)
low = range(1, 50 + 1)

for cell in cells:
    type_of_fire, cell_value = cell.split(" = ")
    cell_value = int(cell_value)
    is_cell_valid = False
    if type_of_fire == 'High':
        if cell_value in high:
            is_cell_valid = True
    elif type_of_fire == 'Medium':
        if cell_value in medium:
            is_cell_valid = True
    elif type_of_fire == 'Low':
        if cell_value in low:
            is_cell_valid = True
    if is_cell_valid:
        if water_amount >= cell_value:
            water_amount -= cell_value
            fire_out_cells.append(cell_value)
            fire += cell_value
            effort += cell_value * 0.25
print("Cells:")
for fire_out_cells in fire_out_cells:
    print(f"- {fire_out_cells}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire}")