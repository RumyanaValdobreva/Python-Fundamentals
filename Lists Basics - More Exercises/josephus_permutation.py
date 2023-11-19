number_of_people = list(map(int, input().split()))
k = int(input())

executions = []

index = k - 1
while len(number_of_people) > 0:
    index = index % len(number_of_people)
    executions.append(number_of_people.pop(index))
    index += k - 1

print("[", end="")
for i in range(len(executions) - 1):
    print(f"{executions[i]},", end="")
print(f"{executions[-1]}]", end="")