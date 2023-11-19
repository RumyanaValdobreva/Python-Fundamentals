list_string = input()
list_integers = [int(x) for x in list_string.split(", ")]

zeros = [x for x in list_integers if x == 0]
without_zeros = [x for x in list_integers if x != 0]

result_list = without_zeros + zeros

print(result_list)