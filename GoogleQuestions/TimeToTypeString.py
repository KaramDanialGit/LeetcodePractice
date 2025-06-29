"""
Imagine you have a special keyboard with all keys in a single row. The layout of characters on a keyboard is denoted
by a string keyboard of length 26. Initially your finger is at index 0. To type a character, you have to move your
finger to the index of the desired character. The time taken to move your finger from index i to index j is abs(j - i).

Given a string keyboard that describe the keyboard layout and a string text, return an integer denoting the time taken to type string text.
"""

def timeToType(keyboard, word):
    time = 0
    mapper = {}

    for i in range(len(keyboard)):
        mapper[keyboard[i]] = i

    prevIdx = 0
    for i in range(len(word)):
        time += abs(mapper[word[i]] - prevIdx)
        prevIdx = mapper[word[i]]

    return time


keyboard = "abcdefghijklmnopqrstuvwxy"
text = "cba"
timeToType(keyboard, text)