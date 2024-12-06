import os
from typing import Generator

def error_log_generator(log_file_path: str) -> Generator[str, None, None]:
    with open(log_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if "ERROR" in line:
                yield line.strip()

# Пример использования
log_file_path = input("Введите путь к файлу логов: ")
output_file_path = "error_logs.txt"

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for error_line in error_log_generator(log_file_path):
        output_file.write(error_line + "\n")

print(f"Строки с ошибками записаны в файл {output_file_path}.")
