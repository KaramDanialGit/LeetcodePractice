from collections import defaultdict

def dp(str_array, str_anagram):
    for i in range(str_array):
        str_anagram.append(str_array[i])
        dp(str_array,str_anagram)
        str_anagram.pop()

test_cases = int(input())

for i in range(test_cases):
    str_to_shuffle = input()
    myDict = {}

    for j in range(len(str_to_shuffle)):
        if str_to_shuffle[j] in myDict:
            myDict[str_to_shuffle[j]] += 1
        else:
            myDict[str_to_shuffle[j]] = 1

    if myDict[str_to_shuffle[j]] > len(str_to_shuffle)//2:
        print("Case #%s: %s" %(i + 1, "IMPOSSIBLE"))
        continue

    str_array = list(str_to_shuffle)
    str_anagram = []

    dp(str_array, str_anagram)

    print("Case #%s: %s" %(i + 1, "".join(str_array)))

