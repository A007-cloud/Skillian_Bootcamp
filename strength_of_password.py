import re
def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8 and re.search(r"[a-z]", password) and re.search(r"[0-9]", password):
        print('password is strong')
    elif len(password) < 8:
        print('password is short')
    elif re.search(r"[a-z]", password) or re.search(r"[0-9]", password):
        print('password is weak')


password = "aditya"
check_password_strength(password);
