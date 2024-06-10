file = open("coding_qual_input.txt", "r")
myDecoder = {}
maxIndex = 0
pyramidEndWords = []

for line in file:
    index, text = line.strip().split(' ')
    maxIndex = max(int(index), maxIndex)

    myDecoder[int(index)] = text

file.close()

wordList = [[] for _ in range(maxIndex + 1)]

for index, text in myDecoder.items():
    wordList[index - 1].append(text)

for i, row in enumerate(wordList):
    endIndex = sum(range(i + 1))
    if endIndex in myDecoder:
        pyramidEndWords.append((endIndex, myDecoder[endIndex]))

for index, word in sorted(pyramidEndWords):
    print(word, end = ' ')