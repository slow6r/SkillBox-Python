import os
from typing import Generator

def error_log_generator(file_path: str) -> Generator[str, None, None]:
    with open(file_path, 'r') as f:
        for line in f:
            if "ERROR" in line:
                yield line.strip()

# Использование:
file_path = input("Введите путь к лог-файлу: ")
for error_line in error_log_generator(file_path):
    print(error_line)
