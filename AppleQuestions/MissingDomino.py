"""
Given an array of dominos of the format "X-Y" where X and Y are numbers ranging from 1-6, find a combination that is
not in the array (multiple answers are possible). Also, if "X-Y" is found in the array than "Y-X" is also considered
to be a 'seen' pair.
"""

def findMissingPair(dominos):
    allPairs = set()
    dominoSet = set()

    for domino in dominos:
        dominoSet.add(domino)
        dominoSet.add(domino[::-1])

    for i in range(1, 7):
        for j in range(1, 7):
            allPairs.add("{}-{}".format(i, j))

    for pair in allPairs:
        if pair not in dominoSet:
            return pair

    return "All pairs found"

test = ["2-0", "1-2", "6-6", "4-5"]
print(findMissingPair(test))