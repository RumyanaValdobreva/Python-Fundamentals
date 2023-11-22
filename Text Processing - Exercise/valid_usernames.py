import re


def is_valid_username(username):
    if 3 <= len(username) <= 16:
        if re.match("^[a-zA-Z0-9_-]+$", username):
            return True
    return False


usernames = input().split(", ")

valid_usernames = [username for username in usernames if is_valid_username(username)]

if valid_usernames:
    for valid_username in valid_usernames:
        print(valid_username)

