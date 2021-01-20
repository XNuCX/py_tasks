word_1, word_2 = input().split()
result = 0
count = 0
if len(word_1) == len(word_2):
    while count in range(len(word_1)) and count in range(len(word_2)):
        result += ord(word_1[count]) * ord(word_2[count])
        count += 1
    print(result)
else:
    if len(word_1) > len(word_2):
        while count in range(len(word_1)) and count in range(len(word_2)):
            result += ord(word_1[count]) * ord(word_2[count])
            count += 1
        while count in range(len(word_1)):
            result += ord(word_1[count])
            count += 1
        print(result)
    else:
        while count in range(len(word_1)) and count in range(len(word_2)):
            result += ord(word_1[count]) * ord(word_2[count])
            count += 1
        while count in range(len(word_2)):
            result += ord(word_2[count])
            count += 1
        print(result)


