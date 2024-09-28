file_size = float(input("Укажите размер файла для скачивания (Мб): "))
download_speed = float(input("Какова скорость вашего соединения (Мб/с): "))

downloaded = 0
seconds = 0

while downloaded < file_size:
    seconds += 1
    downloaded = min(downloaded + download_speed, file_size)
    percentage = (downloaded / file_size) * 100
    print(f"Прошло {seconds} сек. Скачано {downloaded:.2f} из {file_size} Мб ({percentage:.0f}%)")

print(f"Скачивание завершено за {seconds} секунд.")
