file_path = input().split('\\')
result = file_path[-1].split(".")

print(f"File name: {result[0]}")
print(f"File extension: {result[1]}")