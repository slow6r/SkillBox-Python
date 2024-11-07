def filter_videocards():
    n = int(input("Количество видеокарт: "))
    videocards = [int(input(f"Видеокарта {i+1}: ")) for i in range(n)]
    max_card = max(videocards)
    filtered_videocards = [card for card in videocards if card != max_card]
    print("Старый список видеокарт:", videocards)
    print("Новый список видеокарт:", filtered_videocards)