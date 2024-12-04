class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.__stack.pop()
        else:
            raise IndexError("Стек пуст")

    def is_empty(self):
        return len(self.__stack) == 0

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def new_task(self, task, priority):
        if priority not in self.tasks:
            self.tasks[priority] = []
        self.tasks[priority].append(task)

    def __str__(self):
        result = ""
        for priority in sorted(self.tasks):
            result += f"{priority} — {', '.join(self.tasks[priority])}\n"
        return result

def main():
    manager = TaskManager()
    manager.new_task("сделать уборку", 4)
    manager.new_task("помыть посуду", 4)
    manager.new_task("отдохнуть", 1)
    manager.new_task("поесть", 2)
    manager.new_task("сдать ДЗ", 2)
    print(manager)

if __name__ == "__main__":
    main()
