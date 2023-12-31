rooms = int(input())
needed_chairs = False
free_chairs = 0

for room in range(rooms):
    needed_chairs = 0
    current_room = input().split()
    chairs = current_room[0].count("X")
    people = int(current_room[1])
    if chairs > people:
        free_chairs += (chairs - people)
    elif people > chairs:
        needed_chairs = True
        print(f"{people - chairs} more chairs needed in room {room+1}")

if not needed_chairs:
    print(f"Game On, {free_chairs} free chairs left")