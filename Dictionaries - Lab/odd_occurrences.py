words = input().split()
dict = {}

for word in words:
    word = word.lower()

    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1

filtered_words = {key:values for (key, values) in dict.items() if values % 2 != 0}

print(" ".join(filtered_words.keys()))