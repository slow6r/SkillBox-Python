import datetime

class Date:
    """Класс для работы с датами."""

    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_string: str) -> "Date":
        """Создаёт объект Date из строки."""
        day, month, year = map(int, date_string.split('-'))
        return cls(day, month, year)

    @staticmethod
    def is_date_valid(date_string: str) -> bool:
        """Проверяет корректность даты."""
        try:
            datetime.datetime.strptime(date_string, '%d-%m-%Y')
            return True
        except ValueError:
            return False

    def __str__(self) -> str:
        return f"День: {self.day}    Месяц: {self.month}    Год: {self.year}"

# date = Date.from_string("10-12-2077")
# print(date)
# print(Date.is_date_valid("10-12-2077"))
# print(Date.is_date_valid("40-12-2077"))