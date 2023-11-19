def password_valiidator(some_password):
    is_valid = True
    if len(some_password) < 6 or len(some_password) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    counter_digits = 0
    for char in password:
        if char.isdigit():
            counter_digits += 1
    if counter_digits < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    return is_valid

password = input()
is_valid = password_valiidator(password)
if is_valid:
    print("Password is valid")