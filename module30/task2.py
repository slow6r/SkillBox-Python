from typing import Callable, Optional

class App:
    def __init__(self):
        self.routes = {}

    def callback(self, path: str):
        def decorator(func: Callable) -> Callable:
            self.routes[path] = func
            return func
        return decorator

    def get(self, path: str) -> Optional[Callable]:
        return self.routes.get(path)

# Пример использования:
app = App()

@app.callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
