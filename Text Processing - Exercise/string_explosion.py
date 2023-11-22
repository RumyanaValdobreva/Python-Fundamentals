string = input().split(">")
result = []
explosion = 0

for element in string:
    if element[0].isdigit():
        explosion += int(element[0])
        if len(element) <= explosion:
            explosion -= len(element)
            element = ">"
        else:
            element = ">" + "".join(list(element[explosion::]))
            explosion = 0
    result.append(element)
    
print(f"{''.join(result)}")