import re

def valid_destination(destination):
    pattern = r'(\=|\/)([A-Z][A-Za-z]{2,})\1'
    matches = re.finditer(pattern, destination)
    travel_points = 0
    valid_locations = []

    if not matches:
        print("Destinations:")
        print("Travel Points: 0")
    else:
        for current_location in matches:
            valid_locations.append(current_location.group(2))
            travel_points += len(current_location.group(2))
        print(f"Destinations: {', '.join(valid_locations)}")
        print(f"Travel Points: {travel_points}")

text = input()
valid_destination(text)