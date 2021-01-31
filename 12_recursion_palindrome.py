def palindrome(word, index, second_word=""):

    if len(word) == len(second_word):
        if word == second_word:

            return f"{word} is a palindrome"
        else:
            return f"{word} is not a palindrome"
    second_word += word[index-1]
    result = palindrome(word, index-1, second_word)
    return result


print(palindrome("abcba", 0))
print(palindrome("peter", 0))