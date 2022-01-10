n = input()


def password_validator(password):
    if 6 <= len(password) <= 10 and password.isalnum():
        digits = 0
        for char in range(0, len(password)):
            if password[char].isnumeric():
                digits += 1
        if digits >= 2:
            print("Password is valid")
        else:
            print("Password must have at least 2 digits")
    elif not password.isalnum():
        digits = 0
        for char in range(0, len(password)):
            if password[char].isnumeric():
                digits += 1
        if digits >= 2:
            print("Password must consist only of letters and digits")
        else:
            print("Password must consist only of letters and digits")
            print("Password must have at least 2 digits")
    elif len(password) < 6 or len(password) > 10 and password.isalnum():
        digits = 0
        for char in range(0, len(password)):
            if password[char].isnumeric():
                digits += 1
        if digits >= 2:
            print("Password must be between 6 and 10 characters")
        else:
            print("Password must be between 6 and 10 characters")
            print("Password must have at least 2 digits")


password_validator(n)