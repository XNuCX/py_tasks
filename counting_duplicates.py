def counting_duplicates(text):
    text = str(text).lower()
    passed_list = []
    count = 0
    for char in text:
        if char in passed_list:
            continue
        if text.count(char) > 1:
            passed_list.append(char)
            count += 1

    return count
print(counting_duplicates("ABBA"))