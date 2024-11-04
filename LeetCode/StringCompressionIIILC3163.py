def compressedString(word: str) -> str:
    tmpCur = 0
    tmpStr = ""
    prevChar = ""

    size = len(word)
    result = ""

    for i in range(size):
        if (prevChar != word[i] or tmpCur == 9) and tmpCur != 0:
            result += str(tmpCur) + tmpStr
            tmpStr = ""
            tmpCur = 0

        tmpStr = word[i]
        tmpCur += 1

        prevChar = word[i]

    return result + str(tmpCur) + tmpStr