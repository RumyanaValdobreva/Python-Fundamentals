number = int(input())
synonym = {}

for i in range(number):
    word = input()
    synonym_word = input()

    if word in synonym:
        synonym[word].append(synonym_word)
    else:
        synonym[word] = [synonym_word]

for word, synonym_list in synonym.items():
    print(f"{word} - {', '.join(synonym_list)}")