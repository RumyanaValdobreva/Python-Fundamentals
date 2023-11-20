text = input().split()

result = [word for word in text if len(word) % 2 == 0]

for word in result:
    print(word)