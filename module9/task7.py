encrypted_message = input("Введите зашифрованное сообщение: ")

first_part = encrypted_message[::2]  
second_part = encrypted_message[1::2]  

decrypted_message = ""
min_len = min(len(first_part), len(second_part))

for i in range(min_len):
    decrypted_message += first_part[i] + second_part[i]

if len(first_part) > len(second_part):
    decrypted_message += first_part[-1]

print(f"Расшифрованное сообщение: {decrypted_message}")
