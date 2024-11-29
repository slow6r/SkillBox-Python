def validate_registration(file_path):
    good_entries = []
    bad_entries = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, email, age = line.strip().split()
                    if not name.isalpha():
                        raise NameError("Поле «Имя» содержит НЕ только буквы")
                    if "@" not in email or "." not in email:
                        raise SyntaxError("Поле «Имейл» НЕ содержит @ и точку")
                    if not (10 <= int(age) <= 99):
                        raise ValueError("Поле «Возраст» НЕ представляет число от 10 до 99")
                    good_entries.append(line.strip())
                except (IndexError, NameError, SyntaxError, ValueError) as e:
                    bad_entries.append(f"{line.strip()}        {e}")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    finally:
        with open('registrations_good.log', 'w', encoding='utf-8') as good_file:
            good_file.write("\n".join(good_entries))

        with open('registrations_bad.log', 'w', encoding='utf-8') as bad_file:
            bad_file.write("\n".join(bad_entries))

# Запуск функции
validate_registration('registrations.txt')
