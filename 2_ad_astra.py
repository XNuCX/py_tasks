import re
from math import floor
text = input()
pattern = r"(\||#)(?P<name>[A-Za-z ]+)\1(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{2})\1(?P<calories>\d?\d?\d?\d)\1"
matches = [el.group() for el in re.finditer(pattern, text)]
calories = [int(el.group("calories")) for el in re.finditer(pattern, text)]
total_calories = sum(calories)
days = floor(total_calories / 2000)

print(f"You have food to last you for: {days} days!")
if matches:
    for match in re.finditer(pattern, text):
        print(f"Item:"
              f" {match.group('name')}, Best before:"
              f" {match.group('day')}/{match.group('month')}/{match.group('year')},"
              f" Nutrition: {match.group('calories')}")
