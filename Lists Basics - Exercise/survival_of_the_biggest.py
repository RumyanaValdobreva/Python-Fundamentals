list_of_numbers = input().split(" ")
numbers_to_remove = int(input())
my_list = []
small_numbers = 0

for num in list_of_numbers:
    my_list.append(int(num))

for number in range(len(my_list)):
    smallest = min(my_list)
    my_list.remove(smallest)
    small_numbers += 1
    if small_numbers >= numbers_to_remove:
        break

if small_numbers >= numbers_to_remove:
    print(*my_list, sep=", ")