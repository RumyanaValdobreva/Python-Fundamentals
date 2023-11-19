def check_happiness():
    employees_happiness = list(map(int, input().split()))
    factor = int(input())

    happiness = [x * factor for x in employees_happiness]

    average_happiness = sum(happiness) / len(happiness)
    happy_count = sum(x >= average_happiness for x in happiness)
    total_count = len(happiness)

    if happy_count >= total_count / 2:
        return f"Score: {happy_count}/{total_count}. Employees are happy!"
    else:
        return f"Score: {happy_count}/{total_count}. Employees are not happy!"

print(check_happiness())