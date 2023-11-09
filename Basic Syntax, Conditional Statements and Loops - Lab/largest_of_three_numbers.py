first_num = int(input())
second_num = int(input())
third_num = int(input())
largest = 0

if first_num >= second_num and first_num >= third_num:
    largest = first_num
elif second_num >= first_num and second_num >= third_num:
    largest = second_num
else:
    largest = third_num

print(largest)