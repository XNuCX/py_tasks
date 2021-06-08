def stock_availability(*args):
    from collections import deque

    stock, command, *rest = args
    stock = deque(stock)
    if command == "delivery":
        for el in rest:
            stock.append(el)
    elif command == "sell":
        if len(rest) > 0:
            if str(rest[0]).isdigit():
                for _ in range(int(rest[0])):
                    stock.popleft()
            else:
                for el in rest:
                    count = stock.count(el)
                    if count != 0:
                        for _ in range(count):
                            stock.remove(el)
        else:
            stock.popleft()
    return list(stock)



print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
