from typing import Any

class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self._head = None

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if not self._head:
            self._head = new_node
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, index: int) -> Any:
        current = self._head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        if current is None:
            raise IndexError("Index out of range")
        return current.data

    def remove(self, index: int) -> None:
        if index == 0:
            if self._head:
                self._head = self._head.next
            else:
                raise IndexError("Index out of range")
            return
        current = self._head
        for _ in range(index - 1):
            if current is None or current.next is None:
                raise IndexError("Index out of range")
            current = current.next
        if current.next is None:
            raise IndexError("Index out of range")
        current.next = current.next.next

    def __iter__(self):
        current = self._head
        while current:
            yield current.data
            current = current.next

    def __str__(self) -> str:
        return "[" + " ".join(str(data) for data in self) + "]"

# Пример использования
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
