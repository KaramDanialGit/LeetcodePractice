# A short list of Darsh's favourite questions. Nothing sussy here, baka

# Question 1

# Return the longest consecutive good range of numbers.

# Input Constraints
# lower, upper <= 1e9
# len(badNums) <= 1e5

# Ex. solve1([2, 4, 5, 15], 1, 10). Ans = 5

def solve1(badNums, lower: int, upper: int):
    array = []
    maxLen = 0
    for i in range(lower,upper + 1):
        if (i in badNums):
            array = []
        else:
            array.append(i)
            maxLen = max(maxLen, len(array))
        print(array)
    return maxLen

ans = solve1([2, 4, 5, 15], 1, 10)
print(ans)



# Question 2

# Return the # of substrings that meet the following 2 conditions:
# 1) Consecutive groups of 1s and 0s
# 2) Equal # of 1s and 0s

# Input Constraints
# len(s) <= 1e5

# Ex. solve2("001101"). Ans = 4

def solve2(s: str):
    countdict = { "0" : 0, "1" : 0 }
    currnum = s[0]
    numgroups = 0
    for i in range(len(s)):
        if currnum != s[i]:
            numgroups += min(countdict["0"], countdict["1"])
            countdict[s[i]] = 0
            currnum = s[i]
        countdict[s[i]] += 1

    numgroups += min(countdict["0"], countdict["1"])

    return numgroups

ans2 = solve2("001")
print(ans2)