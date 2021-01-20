product_with_price = {}
product_with_quantity = {}
inputs = input()
while not inputs == "buy":
    prod_price_quant = inputs.split(" ")
    product_name = prod_price_quant[0]
    product_price = float(prod_price_quant[1])
    product_quantity = int(prod_price_quant[2])
    product_with_price.update({product_name: product_price})
    if product_name not in product_with_quantity:
        product_with_quantity.update({product_name: product_quantity})
    else:
        product_with_quantity[product_name] += product_quantity
    inputs = input()
for name, value in product_with_price.items():
    print(f"{name} -> {(value * product_with_quantity[name]):.2f}")
