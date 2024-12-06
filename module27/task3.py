import os
from typing import Generator

def count_lines_in_py_files(directory: str) -> Generator[int, None, None]:
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = [line for line in f if line.strip() and not line.strip().startswith('#')]
                    yield len(lines)

# Пример использования
directory = input("Введите директорию для анализа: ")
for lines_count in count_lines_in_py_files(directory):
    print(f"Файл содержит {lines_count} строк.")
