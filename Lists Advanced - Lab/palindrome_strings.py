def palindrome(word):
    if word == word[::-1]:
        return word

string = input().split()
searched_palindrome = input()


palindrome_list = [word for word in string if palindrome(word)]
founded_palindrome = palindrome_list.count(searched_palindrome)

print(palindrome_list)
print(f"Found palindrome {founded_palindrome} times")