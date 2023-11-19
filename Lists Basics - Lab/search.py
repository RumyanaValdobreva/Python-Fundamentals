number = int(input())
word = input()

my_list = []

for line in range(number):
    string = input()
    my_list.append(string)

print(my_list)

filtered_list = []

for string in my_list:
    if word in string:
        filtered_list.append(string)

print(filtered_list)