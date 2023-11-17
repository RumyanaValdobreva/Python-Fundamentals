money = input().split(", ")
beggars_number = int(input())
my_list = []

for element in money:
    my_list.append(int(element))

total_sum = []
start_index = 0

while start_index < beggars_number:
    sum_for_beggar = 0
    for current_index in range(start_index, len(my_list), beggars_number):
        sum_for_beggar += my_list[current_index]
    total_sum.append(sum_for_beggar)
    start_index += 1

print(total_sum)