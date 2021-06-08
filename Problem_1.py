from collections import deque
orders = deque(input().split(", "))
pizza_makers_capacity = deque(input().split(", "))
count = 0
flag_compleate = False
while True:
    if not orders:
        flag_compleate = True
        # pizza_makers_capacity.append(str(empl_cap))
        break
    if not pizza_makers_capacity:
        orders.appendleft(str(pizzas))
        break
    pizzas = int(orders.popleft())
    if pizzas > 10 or pizzas <= 0:
        continue
    empl_cap = int(pizza_makers_capacity.pop())

    if not pizza_makers_capacity and empl_cap - pizzas < 0:
        orders.appendleft(str(abs(empl_cap - pizzas)))
        break

    if empl_cap - pizzas >= 0:
        count += pizzas
        continue
    else:
        left_pizzas = str(abs(empl_cap - pizzas))
        count += pizzas - int(left_pizzas)
        orders.appendleft(left_pizzas)

if flag_compleate:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {count}")
    print(F"Employees: {', '.join(pizza_makers_capacity)}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(orders)}")