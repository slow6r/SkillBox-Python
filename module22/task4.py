def advanced_sum(*args):
    total = 0
    for item in args:
        if isinstance(item, (list, tuple)):
            total += advanced_sum(*item)
        elif isinstance(item, int):
            total += item
    return total

if __name__ == "__main__":
    print(advanced_sum([[1, 2, [3]], [1], 3]))  # Ответ: 10
    print(advanced_sum(1, 2, 3, 4, 5))         # Ответ: 15
