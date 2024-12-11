from typing import Type

def singleton(cls: Type):
    """Декоратор для реализации паттерна Singleton."""
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Example:
    pass

# Пример использования:
my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))
print(my_obj is my_another_obj)
