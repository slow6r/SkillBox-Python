import os
from typing import Generator

def gen_files_path(base_dir: str, target_dir: str) -> Generator[str, None, None]:
    for root, dirs, files in os.walk(base_dir):
        if target_dir in dirs:
            for file in files:
                yield os.path.join(root, file)

# Пример использования
base_directory = input("Введите базовую директорию: ")
target_directory = input("Введите название искомой директории: ")

for file_path in gen_files_path(base_directory, target_directory):
    print(file_path)
