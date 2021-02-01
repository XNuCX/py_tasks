import re
from collections import deque
pattern_letter = r"[A-Za-z]"
pattern_punctuation = r"[^A-Za-z0-9]"
pattern_space = r"\s"
letter_count = []
punctuation_count = []
with open("text_1.txt", "r") as file_1:
    for i, el in enumerate(file_1.readlines()):
        letter_count.append(len(re.findall(pattern_letter, el)))
        punctuation_count.append(abs(len(re.findall(pattern_punctuation, el)) - len(re.findall(pattern_space, el))))
        with open("text_2.txt", "a") as file_2:
            temp = deque(el)
            temp.appendleft(f"Line {i+1}: ")
            temp.insert(-1, f" ({letter_count[i]})({punctuation_count[i]})")
            file_2.writelines(temp)


