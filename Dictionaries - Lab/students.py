students = []
course_search = ''

while True:
    student_information = input()

    if ":" not in student_information:
        course_search = student_information
        break

    name, ID, course = student_information.split(":")
    students.append({'name': name, 'ID': ID, 'course': course})

for student in students:
    if course_search.startswith(student['course'][0:3]):
        print(f"{student['name']} - {student['ID']}")