from collections import deque
customers = deque([int(el) for el in input().split(", ")])
taxies = deque([int(el) for el in input().split(", ")])
total_time = 0
flag = False
while customers:
    if not taxies:
        flag = True
        break
    current_customer = customers.popleft()
    if current_customer > taxies[-1]:
        taxies.pop()
        customers.appendleft(current_customer)
    else:
        total_time += current_customer
        taxies.pop()
if flag:
    print('Not all customers were driven to their destinations')
    print(f"Customers left: {', '.join([str(el) for el in customers])}")
else:
    print("All customers were driven to their destinations")
    print(f'Total time: {total_time} minutes')