def favorite_movies():
    films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 
    'Город грехов', 'Мементо', 'Отступники', 'Деревня']
    fav_count = int(input("Сколько фильмов хотите добавить? "))
    favorites = []
    for _ in range(fav_count):
        movie = input("Введите название фильма: ")
        if movie in films:
            favorites.append(movie)
        else:
            print(f"Ошибка: фильма {movie} у нас нет :(")
    print("Ваш список любимых фильмов:", ", ".join(favorites))