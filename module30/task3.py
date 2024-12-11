import datetime
import time
from typing import Callable

def log_methods(time_format: str):
    """Декоратор для логирования методов класса."""
    def decorator(cls):
        for attr_name in dir(cls):
            if not attr_name.startswith('__'):
                attr = getattr(cls, attr_name)
                if callable(attr):
                    def logged_method(method):
                        def wrapper(*args, **kwargs):
                            start_time = time.time()
                            date_time = datetime.datetime.now().strftime(time_format)
                            print(f"Запускается '{cls.__name__}.{method.__name__}'. Дата и время запуска: {date_time}.")
                            result = method(*args, **kwargs)
                            end_time = time.time()
                            print(f"Завершение '{cls.__name__}.{method.__name__}', время работы = {end_time - start_time:.3f} s.")
                            return result
                        return wrapper
                    setattr(cls, attr_name, logged_method(attr))
        return cls
    return decorator

@log_methods("%b %d %Y — %H:%M:%S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = sum([i_num ** 2 for i_num in range(number)])
        return result

# Пример использования:
my_obj = A()
my_obj.test_sum_1()
