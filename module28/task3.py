import os
from typing import Generator

def count_lines_in_files(directory: str) -> Generator[int, None, None]:
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    line_count = sum(1 for line in f if line.strip() and not line.strip().startswith("#"))
                    yield line_count

# Использование:
directory = input("Введите путь к директории: ")
for count in count_lines_in_files(directory):
    print(f"Количество строк: {count}")
