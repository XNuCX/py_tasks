import re
text = input()
pattern = r"((=+)|(/+))(?P<text>[A-Z][A-Za-z]{2,})\1"
travel_points = 0
matches = re.finditer(pattern, text)
collection = [el.group("text") for el in matches]
for el in collection:
    travel_points += len(el)
print(f"Destinations: {', '.join(collection)}")
print(f"Travel Points: {travel_points}")
