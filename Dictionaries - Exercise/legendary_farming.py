items_dictionary = {"shards": 0, "fragments": 0, "motes": 0}
key_materials = input().lower().split(" ")
flag = False

while key_materials:
    for index in range(0, len(key_materials), 2):
        value = int(key_materials[index])
        key = key_materials[index + 1]
        if key not in items_dictionary:
            items_dictionary[key] = value
        else:
            items_dictionary[key] += value
            if items_dictionary["shards"] >= 250:
                print("Shadowmourne obtained!")
                items_dictionary["shards"] -= 250
                flag = True
            elif items_dictionary["fragments"] >= 250:
                print("Valanyr obtained!")
                items_dictionary["fragments"] -= 250
                flag = True
            elif items_dictionary["motes"] >= 250:
                print("Dragonwrath obtained!")
                items_dictionary["motes"] -= 250
                flag = True
        if flag:
            break
    if flag:
        break
    key_materials = input().lower().split(" ")

for key, value in items_dictionary.items():
    print(f"{key}: {value}")