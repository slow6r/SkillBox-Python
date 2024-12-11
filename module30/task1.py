from typing import Callable

user_permissions = ['admin']

def check_permission(required_permission: str) -> Callable:
    """Декоратор для проверки прав доступа."""
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            if required_permission in user_permissions:
                return func(*args, **kwargs)
            raise PermissionError(f"У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}")
        return wrapper
    return decorator

@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')

# Пример использования:
delete_site()  # Успех
add_comment()  # Ошибка: PermissionError
