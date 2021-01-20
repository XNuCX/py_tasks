import re
text = input()
pattern = r"(@|#)[A-za-z]{3,}\1\1[A-za-z]{3,}\1"
word_container = {}
matches = re.findall(pattern, text)
pattern_word = r""
temp_list = []
flag = False


if not matches:
    print("No word pairs found!")
else:
    valid_pairs = [el.group() for el in re.finditer(pattern, text)]
    print(f"{len(valid_pairs)} word pairs found!")
    for el in valid_pairs:
        if "@" in el:
            word = el.split("@@")
            word[0] = word[0].replace("@", "")
            word[1] = word[1].replace("@", "")
            if word[0] == word[1][-1::-1]:
                if not flag:
                    print("The mirror words are:")
                    flag = True
                temp_list.append(f"{word[0]} <=> {word[1]}")

        elif "#" in el:
            word = el.split("##")
            word[0] = word[0].replace("#", "")
            word[1] = word[1].replace("#", "")
            if word[0] == word[1][-1::-1]:
                if not flag:
                    print("The mirror words are:")
                    flag = True

                temp_list.append(f"{word[0]} <=> {word[1]}")

# if word_container:
#     print("The mirror words are:")
#     for key, value in word_container.items():
#         temp_list.append(f"{key} <=> {value}")
#     print(", ".join(temp_list))
# else:
if not flag:
    print("No mirror words!")
else:
    print(", ".join(temp_list))