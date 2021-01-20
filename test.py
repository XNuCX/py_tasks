product = input()
city = input()
quantity = float(input())
price = 0.0
result = 0.0

if city == "Sofia":
    if product == "coffee":
        price = 0.50
        result = price * quantity
    elif product == "water":
        price = 0.80
        result = price * quantity
    elif product == "beer":
        price = 1.20
        result = price * quantity
    elif product == "sweets":
        price = 1.45
        result = price * quantity
    elif product == "peanuts":
        price = 1.60
        result = price * quantity

elif city == "Plovdiv":
    if product == "coffee":
        price = 0.40
        result = price * quantity
    elif product == "water":
        price = 0.70
        result = price * quantity
    elif product == "beer":
        price = 1.15
        result = price * quantity
    elif product == "sweets":
        price = 1.30
        result = price * quantity
    elif product == "peanuts":
        price = 1.50
        result = price * quantity

elif city == "Varna":
    if product == "coffee":
        price = 0.45
        result = price * quantity
    elif product == "water":
        price = 0.70
        result = price * quantity
    elif product == "beer":
        price = 1.10
        result = price * quantity
    elif product == "sweets":
        price = 1.35
        result = price * quantity
    elif product == "peanuts":
        price = 1.55
        result = price * quantity

print(result)