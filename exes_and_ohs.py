def checker(text):
    text = str(text).lower()
    if "x" not in text and "o" not in text:
        return True

    if text.count("x") == text.count("o"):
        return True
    else:
        return False

print(checker("ooxx"))