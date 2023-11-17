a = int(input())
b = int(input())

temp = a
a = b
b = temp

print('Before:')
print(f'a = {b}')
print(f'b = {a}')
print('After:')
print('a = {}'.format(a))
print('b = {}'.format(b))