import re
n = int(input())
text = ""
temp = []
pattern = r"^(\$|%)(?P<name>[A-Z][a-z]{2,})\1: \[(?P<first>\d+)\]\|\[(?P<second>\d+)\]\|\[(?P<third>\d+)\]\|$"
for _ in range(n):
    text = input()
    matches = re.finditer(pattern, text)
    temp = [el.group() for el in matches]
    if temp == []:
        print("Valid message not found!")
        temp = []
    else:
        for match in re.finditer(pattern, text):
            name = match.group("name")
            first = chr(int(match.group("first")))
            second = chr(int(match.group("second")))
            third = chr(int(match.group("third")))
            string = first + second + third
            print(f"{name}: {string}")
        temp = []
