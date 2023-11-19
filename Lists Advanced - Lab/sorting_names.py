def sort_names():
    names = input().split(", ")
    sorted_names = sorted(names, key=lambda x: (-len(x), x))
    return sorted_names

result = sort_names()
print(result)