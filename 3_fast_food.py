quantity_of_food = int(input())
orders = input().split(" ")
completed_orders = []
biggest_order = max([int(el) for el in orders])
while True:
    if not orders:

        print(biggest_order)
        print("Orders complete")
        break
    elif quantity_of_food - int(orders[0]) >= 0:
        completed_orders.append(orders.pop(0))
        quantity_of_food -= int(completed_orders[-1])

    else:

        print(biggest_order)
        print(f"Orders left: {' '.join(orders)}")
        break
