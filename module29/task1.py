import os
from typing import Optional

class File:
    """Контекстный менеджер для работы с файлами."""

    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file: Optional[object] = None

    def __enter__(self):
        if 'r' in self.mode and not os.path.exists(self.filename):
            self.mode = 'w'
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if self.file:
            self.file.close()
        return True  # Подавляем все исключения

# with File("test.txt", "r") as f:
#     f.write("Hello, World!")