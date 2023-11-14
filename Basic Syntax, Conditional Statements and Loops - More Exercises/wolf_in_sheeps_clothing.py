animals = input().split(", ")

if animals[len(animals) - 1] == "sheep":
    count_sheep = animals.count("sheep")
    print(f"Oi! Sheep number {count_sheep}! You are about to be eaten by a wolf!")
elif animals[len(animals) - 1] == "wolf":
    print("Please go away and stop eating my sheep")
