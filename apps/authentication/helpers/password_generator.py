import string
import random

upper = string.ascii_uppercase
lower = string.ascii_lowercase
digit = string.digits
symbols = string.punctuation


def password_generator(n=8):
    pass_choice = upper + lower + digit + symbols
    password = ""

    for i in range(n):
        password += random.choice(pass_choice)
    return password
