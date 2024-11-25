import os

def analyze_directory(path):
    total_size = 0
    file_count = 0
    dir_count = 0

    for root, dirs, files in os.walk(path):
        dir_count += len(dirs)
        file_count += len(files)
        for file in files:
            total_size += os.path.getsize(os.path.join(root, file))

    print(f"Размер каталога (в Кбайтах): {total_size / 1024:.2f}")
    print(f"Количество подкаталогов: {dir_count}")
    print(f"Количество файлов: {file_count}")

path = input("Введите путь к каталогу: ")
analyze_directory(path)
