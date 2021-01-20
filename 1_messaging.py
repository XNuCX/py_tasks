numbers = input().split(" ")
text = input()
calculated_chars = []
number = []
word = []
for el in numbers:
    for num in el:
        number.append(num)
    characters = [int(chars) for chars in number]
    characters = sum(characters)
    calculated_chars.append(characters)
    number = []

for i in calculated_chars:
    index = i
    while index > len(text):
        index -= len(text)
    word.append(text[index])
    text = [char for char in text]
    text.pop(index)
    text = "".join(text)

print("".join(word))
