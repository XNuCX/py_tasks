def concatenate(*text):
    txt = ""
    for el in text:
        txt += el
    return txt
print(concatenate("Soft", "Uni", "Is", "Great", "!"))