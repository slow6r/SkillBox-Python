class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, index: int) -> int:
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1
        raise IndexError("Index out of bounds")

    def remove(self, index: int):
        current = self.head
        if index == 0:
            self.head = current.next
            return
        count = 0
        while current:
            if count == index - 1:
                current.next = current.next.next
                return
            current = current.next
            count += 1
        raise IndexError("Index out of bounds")

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

# Использование:
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print("Текущий список:", list(my_list))
print("Получение третьего элемента:", my_list.get(2))
my_list.remove(1)
print("Новый список:", list(my_list))
