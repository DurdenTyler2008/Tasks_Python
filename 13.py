# подбор пароля

from random import choice

correctPassword = "1234"
wrongPasswords = set()

length = len(correctPassword)
chars = "123456789"
run = True

while run:
    password = ''
    for i in range(length):
        password += choice(chars)

    if password not in wrongPasswords:
        if password != correctPassword:
            wrongPasswords.add(password)
        else:
            run = False

print(password + 'это корректный пароль')
