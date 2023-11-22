number_of_students = int(input())
students_data = {}


for current_number in range(number_of_students):
    name = input()
    grade = float(input())
    if name not in students_data:
        students_data[name] = [grade]
    else:
        students_data[name] += [float(grade)]

for key, value in students_data.items():
    value = sum(value) / len(value)
    if value >= 4.5:
        print(f"{key} -> {value:.2f}")

