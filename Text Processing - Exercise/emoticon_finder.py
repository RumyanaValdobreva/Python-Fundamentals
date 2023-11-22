text = input()
result = []

for i in range(0, len(text)):
    if ":" in text[i]:
        result.append(text[i + 1])

for current in result:
    print(f":{current}")