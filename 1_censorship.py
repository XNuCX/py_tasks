word = input()
sentance = input()
sentance = sentance.replace(word, "*" * len(word))
print(sentance)