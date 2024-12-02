def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    for index, word in enumerate(sentence.split(" ")):
        for i in range(len(word)):
            if searchWord == word[:i + 1]:
                return index + 1

    return -1