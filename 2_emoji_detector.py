import re
text = input()
pattern = r"-?\d"
# emoji_pattern = r"\B(:{2}|\*{2})[A-Z][a-z]{2,}(\1)\B"
# emoji_pattern = r"(^|(?<=\s))(:{2}|\*{2})[A-Z][a-z]{2,}(\2)"
# emoji_pattern = r"(?<!:)(?<!\*)(:{2}|\*{2})[A-Z][a-z]{2,}(\1)(?!:)(?!\*)"
emoji_pattern = r"(:{2}|\*{2})[A-Z][a-z]{2,}\1"
word_pattern = r"[A-Za-z]+"
words = []
threshold = 1
count = 0
emoji = []
num = 0
matches = re.findall(pattern, text)
for match in matches:
    threshold *= int(match)
emoji_matches = re.finditer(emoji_pattern, text)
print(f"Cool threshold: {threshold}")
if re.finditer(emoji_pattern, text):
    for match in emoji_matches:
        count += 1
        emoji.append(match.group())
    # if count == 0:
    #     exit()
    print(f"{count} emojis found in the text. The cool ones are:")
    word_emoji = re.findall(word_pattern, " ".join(emoji))
    words = [el for el in word_emoji]
    for index, el in enumerate(words):
        for char in el:
            num += ord(char)
        if num > threshold:
            print(f"{emoji[index]}")
        num = 0


