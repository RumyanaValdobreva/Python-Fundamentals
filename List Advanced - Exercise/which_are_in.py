def which_are_in(current_list_, new_list_):
    for i in range(len(current_list_) -1, -1, -1):
        word = current_list_[i]
        word_in_list = False
        for new_word in new_list_:
            if word in new_word:
                word_in_list = True
        if not word_in_list:
            current_list_.remove(word)
    return current_list_


current_list = input().split(", ")
new_list = input().split(", ")
print(which_are_in(current_list, new_list))