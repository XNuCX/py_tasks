import re
n = int(input())
for i in range(n):
    given_sequence = input()
    pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
    pattern_digit = r"\d"
    match = re.match(pattern, given_sequence)

    if match:
        matches = re.finditer(pattern_digit, given_sequence)
        group = [el.group() for el in matches]
        if not group:
            group = ["0", "0"]
        group = "".join(group)
        print(f"Product group: {group}")
    else:
        print("Invalid barcode")