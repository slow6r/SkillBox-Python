# Ввод сообщения и сдвига
message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

# Алфавит и количество букв
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_len = len(alphabet)

# Функция для шифрования текста
def caesar_cipher(text, shift_val):
    encrypted_message = [
        alphabet[(alphabet.index(char) + shift_val) % alphabet_len] if char in alphabet else char
        for char in text
    ]
    return ''.join(encrypted_message)

# Вывод зашифрованного сообщения
encrypted_message = caesar_cipher(message, shift)
print("Зашифрованное сообщение:", encrypted_message)
