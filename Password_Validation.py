# email and password validation

import re

email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

while True:

    email_id = input('Enter email address : ')
    email_id_object = email_pattern.search(email_id)
    if email_id_object is None:
        print('Enter correct email address : ')
        continue
    else:
        print('Email registered')
        break

# password validation which is at least 8 characters long, has signs @#$% and ends with a number

pwd_pattern = re.compile(r"([a-zA-Z0-9$%#@]{7,}[0-9])")

while True:

    pwd = input('Strong Password of at least 8 characters, numbers, @#$%: ')
    pwd_object = pwd_pattern.fullmatch(pwd)
    if pwd_object is None:
        print("Enter correct password of at least 8 characters, numbers, @#$% :")
        continue
    else:
        print("Welcome !!")
        break
