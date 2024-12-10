from collections import OrderedDict
from typing import Any, Tuple

class LRUCache:
    """Класс LRU Cache для кэширования запросов."""

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: OrderedDict[str, Any] = OrderedDict()

    @property
    def cache(self) -> OrderedDict:
        """Возвращает самый старый элемент кэша."""
        return self._cache

    @cache.setter
    def cache(self, new_elem: Tuple[str, Any]) -> None:
        """Добавляет новый элемент в кэш."""
        key, value = new_elem
        if key in self._cache:
            self._cache.move_to_end(key)
        elif len(self._cache) >= self.capacity:
            self._cache.popitem(last=False)
        self._cache[key] = value

    def get(self, key: str) -> Any:
        """Возвращает значение по ключу из кэша."""
        if key in self._cache:
            self._cache.move_to_end(key)
            return self._cache[key]
        return None

    def print_cache(self) -> None:
        """Печатает текущий кэш."""
        print("LRU Cache:")
        for key, value in self._cache.items():
            print(f"{key} : {value}")

# cache = LRUCache(3)
# cache.cache = ("key1", "value1")
# cache.cache = ("key2", "value2")
# cache.cache = ("key3", "value3")
# cache.print_cache()
# print(cache.get("key2"))
# cache.cache = ("key4", "value4")
# cache.print_cache()