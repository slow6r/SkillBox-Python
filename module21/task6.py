def add_contact(contacts):
    name, surname = input("Введите имя и фамилию нового контакта (через пробел): ").split()
    phone = input("Введите номер телефона: ")
    key = (name, surname)
    if key in contacts:
        print("Такой человек уже есть в контактах.")
    else:
        contacts[key] = phone
    print(f"Текущий словарь контактов: {contacts}")

def find_contact(contacts):
    surname = input("Введите фамилию для поиска: ").strip().lower()
    results = [f"{name} {lname} {phone}" for (name, lname), phone in contacts.items() if lname.lower() == surname]
    print("\n".join(results) if results else "Контактов с такой фамилией не найдено.")

# Основной код
contacts = {}
while True:
    action = input("Введите номер действия (1 - Добавить контакт, 2 - Найти человека): ").strip()
    if action == "1":
        add_contact(contacts)
    elif action == "2":
        find_contact(contacts)
    else:
        print("Некорректное действие. Попробуйте снова.")
