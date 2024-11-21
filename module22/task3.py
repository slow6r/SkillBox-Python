from copy import deepcopy

def create_sites():
    base_site = {
        'html': {
            'head': {
                'title': 'Куплю/продам телефон недорого'
            },
            'body': {
                'h2': 'У нас самая низкая цена на iPhone',
                'div': 'Купить',
                'p': 'Продать'
            }
        }
    }
    sites = []
    num_sites = int(input("Сколько сайтов: "))
    for _ in range(num_sites):
        product = input("Введите название продукта для нового сайта: ")
        new_site = deepcopy(base_site)
        new_site['html']['head']['title'] = f'Куплю/продам {product} недорого'
        new_site['html']['body']['h2'] = f'У нас самая низкая цена на {product}'
        sites.append(new_site)
        for site in sites:
            print(site)

if __name__ == "__main__":
    create_sites()
