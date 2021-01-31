def even_odd(*args):
    comm = args[-1]
    args = [el for el in args]
    args.pop()
    if comm == "even":
        return [el for el in args if int(el) % 2 == 0]
    elif comm == "odd":
        return [el for el in args if not int(el) % 2 == 0]
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))