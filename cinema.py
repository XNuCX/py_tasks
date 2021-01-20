type = (str(input())).lower()
r = int(input())
c = int(input())
premiere = 12.00
normal = 7.50
discount = 5.00
seats = r * c
if type == "premiere":
    income = premiere * seats
else:
    if type == "normal":
        income = normal * seats
    else:
        if type == "discount":
            income = discount * seats

print(f"{income:.2f} leva")
