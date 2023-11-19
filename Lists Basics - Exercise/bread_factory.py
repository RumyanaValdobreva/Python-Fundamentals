events = input().split("|")
coins = 100
energy = 100
factory_is_closed = False

for event in events:
    event_items = event.split("-")
    type_event = event_items[0]
    value_event = int(event_items[1])
    if type_event == 'rest':
        current_energy = energy
        energy += value_event
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif type_event == 'order':
        if energy >= 30:
            energy -= 30
            coins += value_event
            print(f"You earned {value_event} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= value_event:
            coins -= value_event
            print(f"You bought {type_event}.")
        else:
            factory_is_closed = True
            break

if factory_is_closed:
    print(f"Closed! Cannot afford {type_event}.")
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")