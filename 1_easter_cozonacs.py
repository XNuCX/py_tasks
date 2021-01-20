budget = float(input())
price_for_kg = float(input())
price_pack_eggs = price_for_kg * 0.75
price_milk = (price_for_kg + (price_for_kg * 0.25)) * 0.250
price_cake = price_pack_eggs + price_for_kg + price_milk
count = 0
colored_eggs = 0
while budget >= price_cake:
    count += 1
    colored_eggs += 3
    if count % 3 == 0:
        colored_eggs -= count - 2
    budget -= price_cake
print(f"You made {count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
