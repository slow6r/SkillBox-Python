import time
import functools

def slow_down(seconds: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Задержка на {seconds} секунд...")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@slow_down(2)
def example_function():
    print("Функция выполнена!")

example_function()
