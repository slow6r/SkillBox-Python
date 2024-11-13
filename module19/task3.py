filename = input("Название файла: ")
if filename[0] in "@№$%^&*()":
    print("Ошибка: название начинается недопустимым символом.")
elif not filename.endswith(('.txt', '.docx')):
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx.")
else:
    print("Файл назван верно.")
