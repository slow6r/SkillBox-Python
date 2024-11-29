def count_characters(file_path):
    total_characters = 0
    errors = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                line_content = line.strip()  # Убираем лишние символы \n, пробелы
                if len(line_content) < 3:
                    error_message = f"Ошибка: менее трёх символов в строке {line_number}."
                    print(error_message)
                    errors.append(error_message)
                total_characters += len(line_content)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    finally:
        print(f"Общее количество символов: {total_characters}")

        # Записываем ошибки в errors.log
        if errors:
            with open('errors.log', 'w', encoding='utf-8') as error_file:
                for error in errors:
                    error_file.write(error + '\n')

# Запуск функции
count_characters('people.txt')
