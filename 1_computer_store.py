receipt = ""
type_customer = ""
prices_wo_tax = []
flag = False
while True:
    commands = input()
    if commands == "special" or commands == "regular":
        type_customer = commands
        break
    if float(commands) < 0:
        print("Invalid price!")
        continue
    prices_wo_tax.append(float(commands))
if not sum(prices_wo_tax) == 0:
    if type_customer == "regular":
        prices_with_tax = [el * 1.2 for el in prices_wo_tax]

    elif type_customer == "special":
        flag = True
        prices_with_tax = [el * 1.2 for el in prices_wo_tax]

    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {sum(prices_wo_tax):.2f}$\n"
          f"Taxes: {(sum(prices_with_tax) - sum(prices_wo_tax)):.2f}$\n"
          f"-----------")
    if flag:
        print(f"Total price: {sum(prices_with_tax) * 0.9:.2f}$")
    else:
        print(f"Total price: {sum(prices_with_tax):.2f}$")
else:
    print("Invalid order!")

