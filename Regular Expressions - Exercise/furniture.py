import re

command = input()
items = []
total_price = 0

pattern = r">>([a-zA-Z]+)<<(\d+\.?\d+)!(\d+)"

while command != "Purchase":
    result = re.findall(pattern, command)
    if result:
        items.append(result[0][0])
        total_price += float(result[0][1]) * int(result[0][2])

    command = input()


if items:
    print("Bought furniture:")
    print("\n".join(items))
    print(f"Total money spend: {total_price:.2f}")
