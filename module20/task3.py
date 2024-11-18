goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [{'quantity': 27, 'price': 42}],
    '23456': [{'quantity': 22, 'price': 510}, {'quantity': 32, 'price': 520}],
    '34567': [{'quantity': 2, 'price': 1200}, {'quantity': 1, 'price': 1150}],
    '45678': [{'quantity': 50, 'price': 100}, {'quantity': 12, 'price': 95}, {'quantity': 43, 'price': 97}],
}

for item, code in goods.items():
    total_quantity = sum(entry['quantity'] for entry in store[code])
    total_price = sum(entry['quantity'] * entry['price'] for entry in store[code])
    print(f"{item} — {total_quantity} штук, стоимость {total_price} рублей.")
