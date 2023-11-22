student_info = input()
courses = {}


while student_info != "end":
    command = student_info.split(" : ")
    if command[0] not in courses:
        courses[command[0]] = [command[1]]
    else:
        courses[command[0]] += [command[1]]

    student_info = input()

for course in courses.keys():
    print(f"{course}: {len(courses[course])}")
    for student in courses[course]:
        print(f"-- {student}")