menu_input = input("Доступное меню: ")
menu_items = menu_input.split(';')
formatted_menu = ", ".join(menu_items)
print("Сейчас в меню есть:", formatted_menu)
