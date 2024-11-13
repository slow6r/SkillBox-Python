while True:
    password = input("Придумайте пароль: ")
    if len(password) >= 8 and any(c.isupper() for c in password) and sum(c.isdigit() for c in password) >= 3:
        print("Это надёжный пароль.")
        break
    else:
        print("Пароль ненадёжный. Попробуйте ещё раз.")
