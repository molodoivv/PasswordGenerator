import random

def generate_pass():
    password = ''
    len_pswrd = int(input("КАКОЙ ДЛИНЫ ТЫ ХОЧЕШЬ ПАРОЛЬ?(введи целое число): "))
    symbols = list('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789')
    # подумать о добавлении генерации пароля с доп символами
    symbols_plus = list('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789$.#@!^&*-_+')

    for i in range(len_pswrd):
        password += random.choice(symbols)

    return password


print(generate_pass())
