
n = int(input())
capacity = 255
liters = 0
for i in range(0, n):
    lit = int(input())
    liters += lit
    if capacity - liters > 0 or capacity - liters < 0:

        if capacity - liters < 0:
            liters -= lit
            print("Insufficient capacity!")
    else:
        if capacity - liters != 0:
            print(capacity - liters)
        break
print(liters)
