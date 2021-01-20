import re
line = input()
names = []
total_price = 0.0
while not line == "Purchase":
    pattern = rf">>(?P<name>.+)<<(?P<price>\d+\.?\d+)!(?P<quantity>\d+)"
    if re.fullmatch(pattern, line, re.IGNORECASE):
        matches = re.match(pattern, line, re.IGNORECASE)
        names.append(matches.group("name"))
        total_price += float(matches.group("price")) * int(matches.group("quantity"))
    line = input()
# names = "\n".join(names)
# print(f"Bought furniture:\n{names}\nTotal money spend: {total_price:.2f}")
print("Bought furniture:")
for i in names:
    print(i)
print(f"Total money spend: {total_price:.2f}")