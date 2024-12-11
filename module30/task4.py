from typing import Callable

def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """Декоратор для декораторов, позволяющий передавать аргументы."""
    def wrapper(*args, **kwargs) -> Callable:
        def inner_decorator(func: Callable) -> Callable:
            return decorator(func, *args, **kwargs)
        return inner_decorator
    return wrapper

@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    def wrapper(*func_args, **func_kwargs):
        print(f"Переданные арги и кварги в декоратор: {args} {kwargs}")
        return func(*func_args, **func_kwargs)
    return wrapper

@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)

# Пример использования:
decorated_function("Юзер", 101)
