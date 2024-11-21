def find_key(data, key, max_depth=None, current_depth=1):
    if max_depth is not None and current_depth > max_depth:
        return None
    if key in data:
        return data[key]
    for sub_key, sub_value in data.items():
        if isinstance(sub_value, dict):
            result = find_key(sub_value, key, max_depth, current_depth + 1)
            if result is not None:
                return result
    return None

if __name__ == "__main__":
    site = {
        'html': {
            'head': {
                'title': 'Мой сайт'
            },
            'body': {
                'h2': 'Здесь будет мой заголовок',
                'div': 'Тут, наверное, какой-то блок',
                'p': 'А вот здесь новый абзац'
            }
        }
    }
    search_key = input("Введите искомый ключ: ")
    depth_choice = input("Хотите ввести максимальную глубину? Y/N: ").lower()
    max_depth = None
    if depth_choice == "y":
        max_depth = int(input("Введите максимальную глубину: "))
    result = find_key(site, search_key, max_depth)
    print(f"Значение ключа: {result}")
