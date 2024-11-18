def parse_orders(n):
    orders = {}
    for i in range(1, n + 1):
        order = input(f"{i}-й заказ: ").split()
        customer, pizza, quantity = order[0], order[1], int(order[2])
        if customer not in orders:
            orders[customer] = {}
        orders[customer][pizza] = orders[customer].get(pizza, 0) + quantity
    return orders

def print_orders(orders):
    for customer in sorted(orders):
        print(f"{customer}:")
        for pizza, quantity in sorted(orders[customer].items()):
            print(f"    {pizza}: {quantity}")

n = int(input("Введите количество заказов: "))
orders = parse_orders(n)
print_orders(orders)
